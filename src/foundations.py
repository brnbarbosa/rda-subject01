from typing import Iterable, List

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