import math

from app.erreurs import (
    A_B_NEGATIF,
    A_B_NULS,
    N_NEGATIF,
    N_TROP_GRAND,
    PREMIER_TROP_GRAND,
    ErreurEntree,
)

# Au-delà de 1558, le résultat dépasse 4300 chiffres et Python refuse de le convertir en JSON
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


def pgcd(a: int, b: int) -> int:
    if a < 0 or b < 0:
        raise ErreurEntree(A_B_NEGATIF)
    if a == 0 and b == 0:
        raise ErreurEntree(A_B_NULS)

    return math.gcd(a, b)
