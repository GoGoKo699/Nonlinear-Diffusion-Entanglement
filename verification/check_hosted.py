"""Capture actual GitHub-rendered pages; automated checks are not visual review.

Read-only public browser requests. Run with SOURCE_REF set to a full commit SHA.
Based on the repository's earlier hosted-capture verification branch.
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
         ('science/model.md', True), ('science/fixed_input.md', True)]
ERROR_TEXT = re.compile(r'The following macros are not allowed|Unable to render|ParseError|MathJax error', re.I)


def main():
    ref = os.environ['SOURCE_REF']
    if not re.fullmatch(r'[0-9a-f]{40}', ref):
        raise ValueError('SOURCE_REF must be a full commit SHA')
    output = Path(__file__).resolve().parent/'local_results/hosted'
    output.mkdir(parents=True, exist_ok=True)
    report = {'status': 'running', 'all_pages_passed': False,
              'source_revision': ref, 'repository': REPOSITORY,
              'observed_at_utc': datetime.now(timezone.utc).isoformat(),
              'scope': 'Automated hosted checks; saved screenshots still require visual review.',
              'pages': []}
    def save():
        tmp = output/'manifest.tmp'
        tmp.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
        tmp.replace(output/'manifest.json')
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
                    response = page.goto(url, wait_until='domcontentloaded', timeout=60000)
                    if response is None or response.status != 200:
                        status = response.status if response is not None else None
                        raise RuntimeError(f'Hosted page unavailable ({status}): {url}')
                    article = page.locator('.markdown-body').first
                    article.wait_for(state='visible', timeout=45000)
                    if requires_math:
                        article.locator('mjx-container, .katex, math').first.wait_for(state='attached', timeout=45000)
                    page.wait_for_timeout(1500)
                    page.evaluate('window.scrollTo(0, 0)')
                    page.screenshot(path=str(output/f'{index:02}-top.png'))
                    article.screenshot(path=str(output/f'{index:02}.png'), timeout=60000)
                    text = article.inner_text()
                    (output/f'{index:02}.txt').write_text(text, encoding='utf-8')
                    errors = article.locator('mjx-merror, .katex-error, [data-mjx-error]').count()
                    text_errors = ERROR_TEXT.findall(text)
                    math_count = article.locator('mjx-container, .katex, math').count()
                    if errors or text_errors or (requires_math and not math_count):
                        raise RuntimeError(f'Math rendering check failed: {path}; text errors: {text_errors}')
                    if not text.strip():
                        raise RuntimeError(f'Empty rendered article: {path}')
                    report['pages'].append({'path': path, 'url': url, 'math_nodes': math_count,
                                            'math_errors': errors, 'error_text': text_errors,
                                            'screenshot': f'{index:02}.png', 'top_screenshot': f'{index:02}-top.png'})
                    save()
                except BaseException:
                    (output/f'{index:02}-failure.html').write_text(page.content(), encoding='utf-8')
                    page.screenshot(path=str(output/f'{index:02}-failure.png'), full_page=True)
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
