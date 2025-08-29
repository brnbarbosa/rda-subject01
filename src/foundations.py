from typing import Iterable, List
import re

def basic_normalize(seq: Iterable[str]) -> List[str]:
    out: List[str] = []
    for s in seq:
        s = s.strip()
        s = s.rstrip()
        s = s.lower()    
        out.append(s)
    return out

assert basic_normalize([" First Name "]) == ["first name"]
assert basic_normalize(["  HELLO  ", "World "]) == ["hello", "world"]
print("basic_normalize: OK")


def normalize_names(seq: Iterable[str]) -> List[str]:
    out: List[str] = []
    for s in seq:
        s = s.strip().rstrip().lower()
        s = re.sub(r"[^a-z0-9\s]+", "", s)
        s = re.sub(r"\s+", "_", s)
        out.append(s)
    return out

def _expect(got: List[str], want: List[str]):  # tiny helper for clearer errors
    assert got == want, f"Got {got}, expected {want}"

# basic cases
_expect(normalize_names([" First Name "]), ["first_name"])
_expect(normalize_names(["Total$ Cost", "O'Connor  Jr."]), ["total_cost", "oconnor_jr"])

# edge-ish cases
_expect(normalize_names(["  a  b   c  "]), ["a_b_c"])
_expect(normalize_names(["ABC-123"]), ["abc123"])
print("normalize_names: OK")