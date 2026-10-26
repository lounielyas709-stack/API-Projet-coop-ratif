import pytest
from fastapi.testclient import TestClient

from app.erreurs import (
    DISTANCE_NEGATIVE,
    TEMPERATURE_SOUS_ZERO_ABSOLU,
    ErreurEntree,
)
from app.main import app
from app.outils.conversion import celsius_fahrenheit, euros_devise, km_miles


def test_celsius_fahrenheit_zero():
    assert celsius_fahrenheit(0) == 32


def test_celsius_fahrenheit_cent():
    assert celsius_fahrenheit(100) == 212


def test_celsius_fahrenheit_moins_quarante():
    assert celsius_fahrenheit(-40) == -40


def test_celsius_fahrenheit_zero_absolu():
    assert celsius_fahrenheit(-273.15) == -459.67


def test_celsius_fahrenheit_temperature_trop_basse():
    with pytest.raises(ErreurEntree) as exc_info:
        celsius_fahrenheit(-300)

    assert str(exc_info.value) == TEMPERATURE_SOUS_ZERO_ABSOLU


client = TestClient(app)

# Tests de la fonction euros_devise


def test_euros_devise_usd():
    assert euros_devise(100, "USD") == 110.0


def test_euros_devise_zero_en_minuscules():
    assert euros_devise(0, "usd") == 0.0


def test_euros_devise_montant_negatif():
    try:
        euros_devise(-10, "USD")
        assert False, "Une ErreurEntree était attendue"
    except ValueError as erreur:
        assert str(erreur) == "le montant ne doit pas être négatif"


def test_euros_devise_devise_inconnue():
    try:
        euros_devise(100, "XYZ")
        assert False, "Une ErreurEntree était attendue"
    except ValueError as erreur:
        assert str(erreur) == "la devise est inconnue"


# Tests de la route HTTP


def test_route_euros_devise_succes():
    reponse = client.get("/euros_devise/100?devise=USD")

    assert reponse.status_code == 200
    assert reponse.json() == {
        "montant": 100,
        "devise": "USD",
        "resultat": 110.0,
    }


def test_route_euros_devise_montant_negatif():
    reponse = client.get("/euros_devise/-10?devise=USD")

    assert reponse.status_code == 400
    assert reponse.json()["detail"] == "le montant ne doit pas être négatif"


def test_route_euros_devise_devise_inconnue():
    reponse = client.get("/euros_devise/100?devise=XYZ")

    assert reponse.status_code == 400
    assert reponse.json()["detail"] == "la devise est inconnue"


def test_route_euros_devise_devise_absente():
    reponse = client.get("/euros_devise/100")

    assert reponse.status_code == 400


def test_km_miles_dix():
    assert km_miles(10) == 6.21


def test_km_miles_marathon():
    assert km_miles(42.195) == 26.22


def test_km_miles_zero():
    assert km_miles(0) == 0


def test_km_miles_negatif():
    with pytest.raises(ErreurEntree) as exc_info:
        km_miles(-5)

    assert str(exc_info.value) == DISTANCE_NEGATIVE


def test_route_km_miles():
    reponse = client.get("/km_miles/10")

    assert reponse.status_code == 200
    assert reponse.json() == {"km": 10.0, "resultat": 6.21}


def test_route_km_miles_negatif():
    reponse = client.get("/km_miles/-5")

    assert reponse.status_code == 400
    assert reponse.json() == {"detail": DISTANCE_NEGATIVE}


def test_route_celsius_fahrenheit():
    reponse = client.get("/celsius_fahrenheit/100")

    assert reponse.status_code == 200
    assert reponse.json() == {"celsius": 100.0, "resultat": 212.0}


def test_route_celsius_fahrenheit_temperature_trop_basse():
    reponse = client.get("/celsius_fahrenheit/-300")

    assert reponse.status_code == 400
    assert reponse.json() == {"detail": TEMPERATURE_SOUS_ZERO_ABSOLU}
