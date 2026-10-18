from fastapi import APIRouter

from app.outils.validation import email_valide

router = APIRouter(tags=["validation"])


@router.get("/email_valide")
def route_email_valide(email: str):
    return {"email": email, "resultat": email_valide(email)}
