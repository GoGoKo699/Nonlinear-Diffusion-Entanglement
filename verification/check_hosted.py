"""Inspect actual public GitHub rendering and save evidence; not a local preview."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
from playwright.sync_api import sync_playwright

REPOSITORY = 'GoGoKo699/Nonlinear-Diffusion-Entanglement'
PAGES = ['README.md', 'learning/README.md', 'learning/RIVAS_HUELGA_BRIDGE.md',
         'learning/MILESTONES.md', 'science/conditional_gaussian.md',
         'science/exact_threshold.md', 'science/cubic_distance.md']


def main():
    ref = os.environ['SOURCE_REF']
    if not re.fullmatch(r'[0-9a-f]{40}', ref):
        raise ValueError('SOURCE_REF must be a full commit SHA')
    output = Path(__file__).resolve().parent/'local_results/hosted'
    output.mkdir(parents=True, exist_ok=True)
    report = {'status': 'running', 'all_pages_passed': False,
              'source_revision': ref, 'repository': REPOSITORY,
              'observed_at_utc': datetime.now(timezone.utc).isoformat(), 'pages': []}
    def save():
        (output/'manifest.json').write_text(json.dumps(report, indent=2)+'\n')
    save()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={'width': 1440, 'height': 1080}, device_scale_factor=1)
            for index, path in enumerate(PAGES):
                url = f'https://github.com/{REPOSITORY}/blob/{ref}/{path}'
                response = page.goto(url, wait_until='domcontentloaded', timeout=60000)
                if response is None or response.status != 200:
                    raise RuntimeError(f'Hosted page unavailable: {url}')
                article = page.locator('.markdown-body').first
                article.wait_for(state='visible', timeout=45000)
                page.wait_for_function("document.querySelectorAll('mjx-container, .katex, math').length > 0", timeout=45000)
                article.screenshot(path=str(output/f'{index:02}.png'), timeout=60000)
                text = article.inner_text()
                (output/f'{index:02}.txt').write_text(text, encoding='utf-8')
                errors = article.locator('mjx-merror, .katex-error, [data-mjx-error]').count()
                math_count = article.locator('mjx-container, .katex, math').count()
                if errors or not math_count:
                    raise RuntimeError(f'Math rendering check failed: {path}')
                report['pages'].append({'path': path, 'url': url, 'math_nodes': math_count,
                                        'math_errors': errors, 'screenshot': f'{index:02}.png'})
                save()
            browser.close()
        report.update(status='passed', all_pages_passed=True)
    except BaseException as error:
        report.update(status='failed', error=f'{type(error).__name__}: {error}')
        save()
        raise
    save()
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
