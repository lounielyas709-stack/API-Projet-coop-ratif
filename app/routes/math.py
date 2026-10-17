from fastapi import APIRouter

from app.outils.math import est_premier, factorielle

router = APIRouter(tags=["math"])


@router.get("/factorielle/{n}")
def route_factorielle(n: int):
    return {"n": n, "resultat": factorielle(n)}


@router.get("/est_premier/{n}")
def route_est_premier(n: int):
    return {"n": n, "resultat": est_premier(n)}
