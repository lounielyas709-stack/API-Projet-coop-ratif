from fastapi import APIRouter

from app.outils.conversion import celsius_fahrenheit, euros_devise, km_miles

router = APIRouter(tags=["conversion"])


@router.get("/euros_devise/{montant}")
def route_euros_devise(montant: float, devise: str):
    return {
        "montant": montant,
        "devise": devise.upper(),
        "resultat": euros_devise(montant, devise),
    }


@router.get("/km_miles/{km}")
def route_km_miles(km: float):
    return {
        "km": km,
        "resultat": km_miles(km),
    }


@router.get("/celsius_fahrenheit/{celsius}")
def route_celsius_fahrenheit(celsius: float):
    return {
        "celsius": celsius,
        "resultat": celsius_fahrenheit(celsius),
    }
