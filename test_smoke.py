# sentinel:skip-file — this test's regex literals intentionally contain the
# placeholder-token strings it scans for; they are search patterns, not leftovers.
"""Minimal smoke test for the Icosapent Ethyl living meta-analysis dashboard.

Run from the repo root:  python -m pytest -q   (or)  python test_smoke.py

Validates the shipped single-file HTML artifacts for structural integrity:
balanced <script> tags, no BOM, no leftover template tokens, no hardcoded
local paths, and a resolvable redirect target. This is a structural smoke
check, not a numerical-engine validation.
"""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
MAIN = os.path.join(ROOT, "ICOSAPENT_ETHYL_REVIEW.html")
INDEX = os.path.join(ROOT, "index.html")


def _read(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    assert not raw.startswith(b"\xef\xbb\xbf"), f"{path} has a UTF-8 BOM"
    return raw.decode("utf-8")


def test_artifacts_exist_and_nonempty():
    for p in (MAIN, INDEX):
        assert os.path.exists(p), f"missing artifact: {p}"
        assert os.path.getsize(p) > 0, f"empty artifact: {p}"


def test_script_tags_balanced():
    for p in (MAIN, INDEX):
        s = _read(p)
        opens = len(re.findall(r"<script\b", s))
        closes = len(re.findall(r"</script\s*>", s))
        assert opens == closes, f"{p}: <script> {opens} != </script> {closes}"


def test_no_unfilled_template_tokens():
    pat = re.compile(r"\{\{[^}]+\}\}|REPLACE_ME|__PLACEHOLDER__|TODO_FILL")
    for p in (MAIN, INDEX):
        hits = pat.findall(_read(p))
        assert not hits, f"{p}: unfilled tokens {hits[:5]}"


def test_no_hardcoded_local_paths():
    pat = re.compile(r"C:\\Users|/home/[a-z]")
    for p in (MAIN, INDEX):
        assert not pat.search(_read(p)), f"{p}: hardcoded local path"


def test_index_redirect_target_resolves():
    s = _read(INDEX)
    m = re.search(r"url=\./([A-Za-z0-9_.\-]+\.html)", s)
    assert m, "index.html has no meta-refresh redirect target"
    target = os.path.join(ROOT, m.group(1))
    assert os.path.exists(target), f"redirect target missing: {target}"


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"PASS {fn.__name__}")
    print(f"\n{len(fns)} passed")
