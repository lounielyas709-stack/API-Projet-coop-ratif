from fastapi import APIRouter

from app.outils.validation import email_valide, mdp_robuste

router = APIRouter(tags=["validation"])


@router.get("/mdp_robuste")
def route_mdp_robuste(mdp: str):
    return {"mdp": mdp, "resultat": mdp_robuste(mdp)}


@router.get("/email_valide")
def route_email_valide(email: str):
    return {"email": email, "resultat": email_valide(email)}
