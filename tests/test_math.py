import pytest
from fastapi.testclient import TestClient

from app.erreurs import N_NEGATIF, ErreurEntree
from app.main import app
from app.outils.math import factorielle

client = TestClient(app)


def test_factorielle_de_5():
    assert factorielle(5) == 120


def test_factorielle_de_0():
    assert factorielle(0) == 1


def test_factorielle_negative():
    with pytest.raises(ErreurEntree):
        factorielle(-1)


def test_route_factorielle_de_5():
    reponse = client.get("/factorielle/5")
    assert reponse.status_code == 200
    assert reponse.json() == {"n": 5, "resultat": 120}


def test_route_factorielle_negative():
    reponse = client.get("/factorielle/-1")
    assert reponse.status_code == 400
    assert reponse.json() == {"detail": N_NEGATIF}
