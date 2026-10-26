from app.erreurs import (
    DISTANCE_NEGATIVE,
    TEMPERATURE_SOUS_ZERO_ABSOLU,
    ErreurEntree,
)


def km_miles(km: float) -> float:
    if km < 0:
        raise ErreurEntree(DISTANCE_NEGATIVE)
    return round(km / 1.609344, 2)


def celsius_fahrenheit(celsius: float) -> float:
    if celsius < -273.15:
        raise ErreurEntree(TEMPERATURE_SOUS_ZERO_ABSOLU)
    return round(celsius * 9 / 5 + 32, 2)
