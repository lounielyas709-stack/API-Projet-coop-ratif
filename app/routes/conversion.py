from fastapi import APIRouter

from app.outils.conversion import euros_devise

router = APIRouter(tags=["conversion"])

@router.get("/euros_devise/{montant}")
def route_euros_devise(montant: float, devise: str):
    return {
        "montant": montant,
        "devise": devise.upper(),
        "resultat": euros_devise(montant, devise),
    }