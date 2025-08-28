"""
Utility helpers for Study Subject 01.
"""

from typing import Iterable, List
import re
import math

def slugify(names: Iterable[str]) -> List[str]:
    """
    Lowercases, strips punctuation, and replaces whitespace with underscores.
    Example: ["First Name", "Total$ Cost"] -> ["first_name", "total_cost"]
    """
    out = []
    for n in names:
        s = n.strip().lower()
        s = re.sub(r"[^a-z0-9\s]+", "", s)
        s = re.sub(r"\s+", "_", s)
        out.append(s)
    return out


def rolling_std(values: Iterable[float], window: int) -> List[float]:
    """
    Rolling standard deviation (population) without numpy.
    For the first window-1 positions, returns math.nan.
    """
    vals = list(values)
    res = []
    for i in range(len(vals)):
        if i+1 < window:
            res.append(math.nan)
            continue
        chunk = vals[i+1-window:i+1]
        m = sum(chunk)/window
        var = sum((x-m)**2 for x in chunk) / window
        res.append(var**0.5)
    return res
