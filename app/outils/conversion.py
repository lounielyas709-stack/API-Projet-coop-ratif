from app.erreurs import TEMPERATURE_SOUS_ZERO_ABSOLU, ErreurEntree


def celsius_fahrenheit(celsius: float) -> float:
    if celsius < -273.15:
        raise ErreurEntree(TEMPERATURE_SOUS_ZERO_ABSOLU)
    return round(celsius * 9 / 5 + 32, 2)
