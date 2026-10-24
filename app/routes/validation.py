from fastapi import APIRouter

from app.outils.validation import code_postal

router = APIRouter(tags=["validation"])

@router.get("/code_postal")
def route_code_postal(code: str):
    return {
        "code":code,
        "resultat": code_postal(code),
    }