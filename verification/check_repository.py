"""Check shared learning structure and local Markdown routes, not proof truth."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def anchors(text):
    found = set(re.findall(r'<a\s+id=[\"\']([^\"\']+)', text))
    counts = {}
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*$', text, re.M):
        title = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', title)
        slug = re.sub(r'[^\w\s-]', '', title.lower()).replace(' ', '-')
        count = counts.get(slug, 0); counts[slug] = count + 1
        found.add(slug if count == 0 else f'{slug}-{count}')
    return found


def run_checks():
    milestone_path = ROOT/'learning/MILESTONES.md'
    text = milestone_path.read_text(encoding='utf-8')
    chunks = re.split(r'^### (M\d{2})[^\n]*\n', text, flags=re.M)
    ids = chunks[1::2]; bodies = chunks[2::2]
    expected = [f'M{i:02}' for i in range(1, 31)]
    assert ids == expected, f'Milestones are not exactly M01 through M30: {ids}'
    edge_count = 0
    for number, (mid, body) in enumerate(zip(ids, bodies), 1):
        for field in ('Question', 'Target', 'Dependencies', 'Connection', 'Sources'):
            assert f'**{field}:**' in body, (mid, field)
        deps = re.search(r'\*\*Dependencies:\*\* (.*?)(?:\n\n|$)', body, re.S).group(1)
        for dep in re.findall(r'\bM(\d{2})\b', deps):
            assert 1 <= int(dep) < number, (mid, dep)
            edge_count += 1
        sources = body.split('**Sources:**', 1)[1]
        assert '](' in sources, f'{mid} has no retrievable project source'
    phase = text.split('## Narrative/innovation', 1)
    assert len(re.findall(r'^### M\d{2}', phase[0], re.M)) == 12
    assert len(re.findall(r'^### M\d{2}', phase[1], re.M)) == 18
    assert '1104.5242v2' in text
    for name in ('README.md', 'llms.txt'):
        contents = (ROOT/name).read_text(encoding='utf-8')
        assert 'learning/MILESTONES.md' in contents
        assert 'learning/RIVAS_HUELGA_BRIDGE.md' in contents
    required_science = ['model', 'conditional_gaussian', 'exact_threshold',
                        'cubic_distance', 'fixed_input', 'interpretation']
    for name in required_science:
        assert (ROOT/f'science/{name}.md').is_file()
    assert not (ROOT/'manuscript/main.md').exists()
    assert not (ROOT/'COACHING.md').exists()
    assert 'Direct momentum diffusion restores' not in (ROOT/'README.md').read_text()
    checked = 0
    documents = sorted(p for p in ROOT.rglob('*.md')
                       if '.git' not in p.parts and 'local_results' not in p.parts)
    for document in documents:
        contents = document.read_text(encoding='utf-8')
        assert contents.count('```') % 2 == 0, f'Unpaired fence in {document}'
        for link in re.findall(r'\[[^\]\n]*\]\(([^\s)]+)\)', contents):
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            path = unquote(parsed.path)
            dest = (document.parent/path).resolve() if path else document
            assert dest.is_relative_to(ROOT), (document, link, 'outside repository')
            assert dest.exists(), (document, link, 'missing file')
            if parsed.fragment and dest.suffix == '.md':
                fragment = unquote(parsed.fragment)
                assert fragment in anchors(dest.read_text(encoding='utf-8')), (document, link, 'missing anchor')
            checked += 1
    return {'all_assertions_passed': True, 'milestones': len(ids),
            'background': 12, 'narrative': 18, 'dependency_edges': edge_count,
            'markdown_documents': len(documents), 'local_links_checked': checked,
            'scope': 'Structure and navigation; no hosted-rendering or proof certification.'}


if __name__ == '__main__':
    import json
    print(json.dumps(run_checks(), indent=2))
