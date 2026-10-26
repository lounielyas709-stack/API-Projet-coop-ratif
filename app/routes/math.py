from fastapi import APIRouter

from app.outils.math import factorielle

router = APIRouter(tags=["math"])


@router.get("/factorielle/{n}")
def route_factorielle(n: int):
    return {"n": n, "resultat": factorielle(n)}
