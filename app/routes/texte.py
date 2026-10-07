from fastapi import APIRouter

from app.outils.texte import est_palindrome

router = APIRouter(tags=["texte"])


@router.get("/est_palindrome/{texte}")
def verifier_palindrome(texte: str):
    return {
        "texte": texte,
        "resultat": est_palindrome(texte)
    }