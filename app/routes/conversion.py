from fastapi import APIRouter

from app.outils.conversion import celsius_fahrenheit

router = APIRouter(tags=["conversion"])

@router.get("/celsius_fahrenheit/{celsius}")
def route_celsius_fahrenheit(celsius: float):
    return {
        "celsius": celsius,
        "resultat": celsius_fahrenheit(celsius),
    }
