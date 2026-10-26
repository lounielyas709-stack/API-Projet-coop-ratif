from fastapi import APIRouter

from app.outils.texte import compter_voyelles, est_palindrome

router = APIRouter(tags=["texte"])


@router.get("/est_palindrome")
def route_est_palindrome(texte: str):
    return {
        "texte": texte,
        "resultat": est_palindrome(texte)
    }


@router.get("/compter_voyelles")
def route_compter_voyelles(texte: str):
    return {
        "texte": texte,
        "resultat": compter_voyelles(texte)
    }