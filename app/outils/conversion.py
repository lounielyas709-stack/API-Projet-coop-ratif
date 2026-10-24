from app.erreurs import DISTANCE_NEGATIVE, ErreurEntree


def km_miles(km: float) -> float:
    if km < 0:
        raise ErreurEntree(DISTANCE_NEGATIVE)
    return round(km / 1.609344, 2)