"""Módulo simples para identificar a UF a partir de um CEP brasileiro.

Função principal:
    uf_from_cep(cep: str | int) -> str
"""
from __future__ import annotations
from typing import List, Tuple, Union
import bisect

_CEP_INTERVALS: List[Tuple[int, int, str]] = [
    (1000000, 19999999, "SP"),
    (20000000, 28999999, "RJ"),
    (29000000, 29999999, "ES"),
    (30000000, 39999999, "MG"),
    (40000000, 48999999, "BA"),
    (49000000, 49999999, "SE"),
    (50000000, 56999999, "PE"),
    (57000000, 57999999, "AL"),
    (58000000, 58999999, "PB"),
    (59000000, 59999999, "RN"),
    (60000000, 63999999, "CE"),
    (64000000, 64999999, "PI"),
    (65000000, 65999999, "MA"),
    (66000000, 68899999, "PA"),
    (68900000, 68999999, "AP"),
    (69000000, 69299999, "AM"),
    (69300000, 69399999, "RR"),
    (69400000, 69899999, "AM"),
    (69900000, 69999999, "AC"),
    (70000000, 72799999, "DF"),
    (72800000, 73699999, "GO"),
    (73700000, 76799999, "GO"),
    (76800000, 76999999, "RO"),
    (77000000, 77999999, "TO"),
    (78000000, 78899999, "MT"),
    (78900000, 78999999, "RO"),
    (79000000, 79999999, "MS"),
    (80000000, 87999999, "PR"),
    (88000000, 89999999, "SC"),
    (90000000, 99999999, "RS"),
]
_STARTS = [r[0] for r in _CEP_INTERVALS]

class CEPFormatoInvalido(ValueError):
    pass

class CEPNaoEncontrado(LookupError):
    pass

def _normalize_cep(cep: Union[str, int]) -> int:
    if isinstance(cep, int):
        s = f"{cep:08d}"
    else:
        s = "".join(ch for ch in str(cep) if ch.isdigit())
    if len(s) != 8:
        return -1
    return int(s)

def uf_from_cep(cep: Union[str, int]) -> str:
    n = _normalize_cep(cep)
    idx = bisect.bisect_right(_STARTS, n) - 1
    if idx < 0:
        return 'XX'
    start, end, uf = _CEP_INTERVALS[idx]
    if start <= n <= end:
        return uf
    return 'XX'

__all__ = ["uf_from_cep", "CEPFormatoInvalido", "CEPNaoEncontrado"]

if __name__ == "__main__":
    for t in [59064330, "01001-000", "69900-000", "88000000", "90010-320"]:
        try:
            print(t, "->", uf_from_cep(t))
        except Exception as e:
            print(t, "ERRO:", e)
