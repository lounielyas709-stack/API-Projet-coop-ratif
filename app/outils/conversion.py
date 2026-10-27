from app.erreurs import (
    DEVISE_INCONNUE,
    DISTANCE_NEGATIVE,
    MONTANT_NEGATIF,
    TEMPERATURE_SOUS_ZERO_ABSOLU,
    ErreurEntree,
)

TAUX_DEVISE = {
    "USD": 1.10,
    "GBP": 0.85,
}


def euros_devise(montant: float, devise: str) -> float:
    if montant < 0:
        raise ErreurEntree(MONTANT_NEGATIF)

    devise = devise.upper()

    if devise not in TAUX_DEVISE:
        raise ErreurEntree(DEVISE_INCONNUE)

    return round(montant * TAUX_DEVISE[devise], 2)


def km_miles(km: float) -> float:
    if km < 0:
        raise ErreurEntree(DISTANCE_NEGATIVE)
    return round(km / 1.609344, 2)


def celsius_fahrenheit(celsius: float) -> float:
    if celsius < -273.15:
        raise ErreurEntree(TEMPERATURE_SOUS_ZERO_ABSOLU)
    return round(celsius * 9 / 5 + 32, 2)
