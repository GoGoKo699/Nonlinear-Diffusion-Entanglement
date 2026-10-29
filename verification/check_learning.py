"""Check the common learning map, local navigation and worked examples.

This validates structure and selected numerical identities, not understanding,
research novelty, universal proofs, or the hosted GitHub renderer.
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def heading_ids(text: str) -> set[str]:
    """GitHub-style identifiers for the plain-text headings used in this route."""
    ids: set[str] = set()
    counts: dict[str, int] = {}
    for heading in re.findall(r'^#{1,6}\s+(.+)$', text, flags=re.M):
        heading = re.sub(r'<[^>]*>', '', heading).strip().lower()
        slug = ''.join(c for c in heading if c in '-_' or c.isspace()
                       or unicodedata.category(c)[0] in 'LN')
        slug = re.sub(r'\s', '-', slug)
        number = counts.get(slug, 0)
        counts[slug] = number + 1
        ids.add(slug if not number else f'{slug}-{number}')
    ids.update(re.findall(r'<a\s+(?:id|name)="([^"]+)"', text))
    return ids


def check_structure() -> dict:
    text = (ROOT / 'learning/MILESTONES.md').read_text(encoding='utf-8')
    parts = re.split(r'^### M(\d{2}) — ([^\n]+)\n', text, flags=re.M)
    records = [(int(parts[i]), parts[i+1], parts[i+2]) for i in range(1, len(parts), 3)]
    assert [r[0] for r in records] == list(range(1, 31))
    assert text.index('Background and preliminaries') < text.index('### M01')
    assert text.index('### M14') < text.index('Narrative and innovation') < text.index('### M15')
    for number, title, body in records:
        assert title.strip()
        for field in ('Central question', 'Understanding target', 'Dependencies',
                      'Story role', 'Conceptual connection', 'Sources'):
            assert f'**{field}:**' in body, (number, field)
        dependencies = re.search(r'\*\*Dependencies:\*\* ([^\n]+)', body).group(1)
        assert all(0 < int(d) < number for d in re.findall(r'M(\d{2})', dependencies))
        assert 'Holevo' in body
        assert any(route in body for route in ('../science/', 'PRIMER.md', 'HOLEVO_BRIDGE.md'))
    learning = '\n'.join(p.read_text(encoding='utf-8') for p in (ROOT / 'learning').glob('*.md'))
    assert not re.search(r'Rivas|Huelga|Serafini|Watrous|Revise\s*→\s*Learn', learning)
    assert '2019' in learning
    links = 0
    files = sorted(ROOT.rglob('*.md'))
    for path in files:
        source = path.read_text(encoding='utf-8')
        assert len(re.findall(r'^```', source, re.M)) % 2 == 0, path
        prose = re.sub(r'```[\s\S]*?```', '', source)
        prose = re.sub(r'\$`[\s\S]*?`\$', '', prose)
        prose = re.sub(r'`[^`]*`', '', prose)
        for target in re.findall(r'\]\(([^\s)]+)\)', prose):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            assert destination.is_relative_to(ROOT.resolve()), (path, target)
            assert destination.exists(), (path, target)
            if parsed.fragment and destination.suffix == '.md':
                assert unquote(parsed.fragment) in heading_ids(destination.read_text(encoding='utf-8')), (path, target)
            links += 1
    return {'milestones': len(records), 'background': 14, 'narrative': 16,
            'local_markdown_links_checked': links, 'markdown_files_checked': len(files),
            'single_anchor': 'Holevo, second revised and expanded edition, 2019'}


def check_examples() -> dict:
    cases = []
    for q in (0., .1, .5, 1.):
        rho = np.array([[1,0,0,q],[0,0,0,0],[0,0,0,0],[q,0,0,1]], dtype=float)/2
        partial = rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
        actual = np.linalg.eigvalsh(partial)
        expected = np.sort([.5,.5,q/2,-q/2])
        assert np.allclose(actual, expected, atol=1e-14)
        v = np.array([0,1,-1,0], dtype=float)/np.sqrt(2)
        witness = np.outer(v,v).reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
        assert abs(np.linalg.norm(witness, 2)-.5)<1e-14
        assert abs(np.trace(witness@rho)+q/2)<1e-14
        cases.append({'q':q, 'partial_transpose_eigenvalues':actual.tolist()})
    determinant_cases = 0
    for D, eta, omega in ((1.,.25,1.),(2.,.125,.7),(1.,0.,-1.)):
        for t in (.2,.8,1.,1.4):
            V = 2*D*np.array([[omega**2*t**3/3,-omega*t*t/2],[-omega*t*t/2,t]])
            V[0,0] += 2*eta*t
            expected = 4*D*eta*t*t + D*D*omega*omega*t**4/3
            assert abs(np.linalg.det(V)-expected)<1e-12
            determinant_cases += 1
    t_gaussian = np.sqrt((np.sqrt(21)-3)/2)
    assert abs(t_gaussian**2+t_gaussian**4/3-1)<1e-14
    return {'qubit_cases':cases,'gaussian_determinant_cases':determinant_cases,
            'primer_gaussian_cutoff':float(t_gaussian),'positive_kinetic_cutoff':1.0}


if __name__ == '__main__':
    print(json.dumps({'status':'passed', 'structure':check_structure(),
                      'examples':check_examples(),
                      'scope':'Structural and finite-example checks, not hosted rendering or proof certification.'},
                     indent=2, allow_nan=False))
