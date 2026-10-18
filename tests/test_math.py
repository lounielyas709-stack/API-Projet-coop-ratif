import pytest
from fastapi.testclient import TestClient

from app.erreurs import (
    A_B_NEGATIF,
    A_B_NULS,
    N_NEGATIF,
    N_TROP_GRAND,
    PREMIER_TROP_GRAND,
    ErreurEntree,
)
from app.main import app
from app.outils.math import FACTORIELLE_MAX, PREMIER_MAX, est_premier, factorielle, pgcd

client = TestClient(app)


def test_factorielle_de_5():
    assert factorielle(5) == 120


def test_factorielle_de_0():
    assert factorielle(0) == 1


def test_factorielle_negative():
    with pytest.raises(ErreurEntree):
        factorielle(-1)


def test_factorielle_a_la_limite():
    assert factorielle(FACTORIELLE_MAX) > 0


def test_factorielle_trop_grand():
    with pytest.raises(ErreurEntree):
        factorielle(FACTORIELLE_MAX + 1)


def test_route_factorielle_de_5():
    reponse = client.get("/factorielle/5")
    assert reponse.status_code == 200
    assert reponse.json() == {"n": 5, "resultat": 120}


def test_route_factorielle_negative():
    reponse = client.get("/factorielle/-1")
    assert reponse.status_code == 400
    assert reponse.json() == {"detail": N_NEGATIF}


def test_route_factorielle_trop_grand():
    reponse = client.get("/factorielle/1001")
    assert reponse.status_code == 400
    assert reponse.json() == {"detail": N_TROP_GRAND}


def test_est_premier_7():
    assert est_premier(7)


def test_est_premier_9():
    assert not est_premier(9)


def test_est_premier_0_1():
    assert not est_premier(0)
    assert not est_premier(1)


def test_est_premier_negatif():
    with pytest.raises(ErreurEntree):
        est_premier(-1)


def test_est_premier_trop_grand():
    with pytest.raises(ErreurEntree):
        est_premier(PREMIER_MAX + 1)


def test_route_est_premier_7():
    reponse = client.get("/est_premier/7")
    assert reponse.status_code == 200
    assert reponse.json() == {"n": 7, "resultat": True}


def test_route_est_premier_negatif():
    reponse = client.get("/est_premier/-1")
    assert reponse.status_code == 400
    assert reponse.json() == {"detail": N_NEGATIF}


def test_route_est_premier_trop_grand():
    reponse = client.get("/est_premier/1000000000001")
    assert reponse.status_code == 400
    assert reponse.json() == {"detail": PREMIER_TROP_GRAND}


def test_pgcd_12_et_18():
    assert pgcd(12, 18) == 6


def test_pgcd_5_et_7():
    assert pgcd(5, 7) == 1


def test_pgcd_0_et_5():
    assert pgcd(0, 5) == 5


def test_pgcd_negatif():
    with pytest.raises(ErreurEntree):
        pgcd(-4, 6)


def test_pgcd_deux_nuls():
    with pytest.raises(ErreurEntree):
        pgcd(0, 0)


def test_route_pgcd():
    reponse = client.get("/pgcd/12/18")
    assert reponse.status_code == 200
    assert reponse.json() == {"a": 12, "b": 18, "resultat": 6}


def test_route_pgcd_negatif():
    reponse = client.get("/pgcd/-4/6")
    assert reponse.status_code == 400
    assert reponse.json() == {"detail": A_B_NEGATIF}


def test_route_pgcd_nuls():
    reponse = client.get("/pgcd/0/0")
    assert reponse.status_code == 400
    assert reponse.json() == {"detail": A_B_NULS}
