from app.erreurs import DEVISE_INCONNUE, MONTANT_NEGATIF, ErreurEntree

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