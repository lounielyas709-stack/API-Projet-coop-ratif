import pytest
from fastapi.testclient import TestClient

from app.erreurs import DISTANCE_NEGATIVE, ErreurEntree
from app.main import app
from app.outils.conversion import km_miles

client = TestClient(app)


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