import math

from app.erreurs import N_NEGATIF, N_TROP_GRAND, ErreurEntree

FACTORIELLE_MAX = 1000


def factorielle(n: int) -> int:
    if n < 0:
        raise ErreurEntree(N_NEGATIF)
    if n > FACTORIELLE_MAX:
        raise ErreurEntree(N_TROP_GRAND)
    return math.factorial(n)
