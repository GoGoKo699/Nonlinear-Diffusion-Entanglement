"""Capture and check actual GitHub pages; screenshots still need visual review.

Public read-only browser requests, pinned by SOURCE_REF to a full commit SHA.
"""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
from playwright.sync_api import sync_playwright

REPOSITORY = 'GoGoKo699/Nonlinear-Diffusion-Entanglement'
PAGES = [('README.md', True), ('learning/README.md', False),
         ('learning/HOLEVO_BRIDGE.md', True), ('learning/PRIMER.md', True),
         ('learning/MILESTONES.md', False), ('science/conditional_gaussian.md', True),
         ('science/exact_threshold.md', True), ('science/cubic_distance.md', True),
         ('science/model.md', True), ('science/fixed_input.md', True),
         ('science/interpretation.md', True), ('science/README.md', False),
         ('references/RELATED_WORK.md', True), ('verification/README.md', True),
         ('verification/SANITY_CHECK.md', False)]
ERROR_TEXT = re.compile(r'The following macros are not allowed|Unable to render|ParseError|MathJax error', re.I)
ROOT = Path(__file__).resolve().parents[1]


def main():
    ref = os.environ['SOURCE_REF']
    if not re.fullmatch(r'[0-9a-f]{40}', ref):
        raise ValueError('SOURCE_REF must be a full commit SHA')
    output = ROOT / 'verification/local_results/hosted'
    output.mkdir(parents=True, exist_ok=True)
    report = {'status': 'running', 'all_pages_passed': False,
              'source_revision': ref, 'repository': REPOSITORY,
              'observed_at_utc': datetime.now(timezone.utc).isoformat(),
              'scope': 'Automated hosted checks; saved screenshots require visual review.',
              'pages': []}

    def save():
        tmp = output / 'manifest.tmp'
        tmp.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
        tmp.replace(output / 'manifest.json')

    save()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={'width': 1440, 'height': 1080}, device_scale_factor=1)
            for index, (path, requires_math) in enumerate(PAGES):
                url = f'https://github.com/{REPOSITORY}/blob/{ref}/{path}'
                report['active_page'] = path
                save()
                try:
                    # Literal less-than plus a letter can be silently sanitized as HTML.
                    source = (ROOT / path).read_text(encoding='utf-8')
                    for equation in re.findall(r'```math\n([\s\S]*?)```', source):
                        if re.search(r'<[A-Za-z]', equation):
                            raise ValueError(f'Use \\lt for HTML-like comparison in {path}')
                    response = page.goto(url, wait_until='domcontentloaded', timeout=60000)
                    if response is None or response.status != 200:
                        status = response.status if response is not None else None
                        raise RuntimeError(f'Hosted page unavailable ({status}): {url}')
                    article = page.locator('.markdown-body').first
                    article.wait_for(state='visible', timeout=45000)
                    if requires_math:
                        article.locator('mjx-container, .katex, math').first.wait_for(state='attached', timeout=45000)
                    page.evaluate('document.fonts.ready')
                    page.wait_for_timeout(1500)
                    page.evaluate('window.scrollTo(0, 0)')
                    page.screenshot(path=str(output / f'{index:02}-top.png'))
                    page.screenshot(path=str(output / f'{index:02}.png'), full_page=True)
                    text = article.inner_text()
                    (output / f'{index:02}.txt').write_text(text, encoding='utf-8')
                    errors = article.locator('mjx-merror, .katex-error, [data-mjx-error]').count()
                    text_errors = ERROR_TEXT.findall(text)
                    math_count = article.locator('mjx-container, .katex, math').count()
                    prose = article.evaluate('''root => {
                        const copy = root.cloneNode(true);
                        copy.querySelectorAll('pre, code, mjx-container, math, .katex').forEach(n => n.remove());
                        return copy.textContent;
                    }''')
                    exposed_dollars = prose.count('$')
                    if errors or text_errors or exposed_dollars or (requires_math and not math_count):
                        raise RuntimeError(f'Rendering failed: {path}; errors={text_errors}; exposed dollars={exposed_dollars}')
                    regression_ok = None
                    if path == 'science/cubic_distance.md':
                        equations = article.locator('mjx-container').all_text_contents()
                        regression_ok = any('Pr' in re.sub(r'\s+', '', s) and s.count('<') >= 2 and '≤' in s for s in equations)
                        if not regression_ok:
                            raise RuntimeError('Probability comparison lost operators in hosted rendering')
                    if not text.strip():
                        raise RuntimeError(f'Empty rendered article: {path}')
                    report['pages'].append({'path': path, 'url': url, 'math_nodes': math_count,
                                            'math_errors': errors, 'error_text': text_errors,
                                            'exposed_dollars': exposed_dollars,
                                            'probability_regression': regression_ok,
                                            'screenshot': f'{index:02}.png',
                                            'top_screenshot': f'{index:02}-top.png'})
                    save()
                except BaseException:
                    (output / f'{index:02}-failure.html').write_text(page.content(), encoding='utf-8')
                    page.screenshot(path=str(output / f'{index:02}-failure.png'), full_page=True)
                    raise
            browser.close()
        report.pop('active_page', None)
        report.update(status='passed', all_pages_passed=True)
    except BaseException as error:
        report.update(status='failed', error=f'{type(error).__name__}: {error}')
        save()
        raise
    save()
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
