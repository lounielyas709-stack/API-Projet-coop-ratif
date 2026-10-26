from fastapi import APIRouter

from app.outils.math import est_premier, factorielle, pgcd

router = APIRouter(tags=["math"])


@router.get("/factorielle/{n}")
def route_factorielle(n: int):
    return {"n": n, "resultat": factorielle(n)}


@router.get("/est_premier/{n}")
def route_est_premier(n: int):
    return {"n": n, "resultat": est_premier(n)}


@router.get("/pgcd/{a}/{b}")
def route_pgcd(a: int, b: int):
    return {"a": a, "b": b, "resultat": pgcd(a, b)}
