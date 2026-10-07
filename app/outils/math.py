import math

from app.erreurs import N_NEGATIF, ErreurEntree


def factorielle(n: int) -> int:
    if n < 0:
        raise ErreurEntree(N_NEGATIF)
    return math.factorial(n)
