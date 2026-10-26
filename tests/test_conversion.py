import pytest
from fastapi.testclient import TestClient

from app.erreurs import TEMPERATURE_SOUS_ZERO_ABSOLU, ErreurEntree
from app.main import app
from app.outils.conversion import celsius_fahrenheit


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


def test_route_celsius_fahrenheit():
    reponse = client.get("/celsius_fahrenheit/100")

    assert reponse.status_code == 200
    assert reponse.json() == {"celsius": 100.0, "resultat": 212.0}


def test_route_celsius_fahrenheit_temperature_trop_basse():
    reponse = client.get("/celsius_fahrenheit/-300")

    assert reponse.status_code == 400
    assert reponse.json() == {"detail": TEMPERATURE_SOUS_ZERO_ABSOLU}