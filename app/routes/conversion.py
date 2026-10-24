from fastapi import APIRouter

from app.outils.conversion import km_miles

router = APIRouter(tags=["conversion"])


@router.get("/km_miles/{km}")
def route_km_miles(km: float):
    return {
        "km": km,
        "resultat": km_miles(km),
    }