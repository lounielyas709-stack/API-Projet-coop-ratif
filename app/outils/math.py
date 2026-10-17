import math

from app.erreurs import N_NEGATIF, N_TROP_GRAND, PREMIER_TROP_GRAND, ErreurEntree

FACTORIELLE_MAX = 1000
PREMIER_MAX = 10**12


def factorielle(n: int) -> int:
    if n < 0:
        raise ErreurEntree(N_NEGATIF)
    if n > FACTORIELLE_MAX:
        raise ErreurEntree(N_TROP_GRAND)
    return math.factorial(n)


def est_premier(n: int) -> bool:
    if n < 0:
        raise ErreurEntree(N_NEGATIF)
    if n < 2:
        return False
    if n > PREMIER_MAX:
        raise ErreurEntree(PREMIER_TROP_GRAND)
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            return False

    return True
