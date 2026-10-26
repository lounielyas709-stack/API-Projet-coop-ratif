import pytest
from fastapi.testclient import TestClient

from app.erreurs import MDP_VIDE, PARAMETRE_INVALIDE, ErreurEntree
from app.main import app
from app.outils.validation import mdp_robuste

client = TestClient(app)


# --- la fonction ---

def test_mdp_robuste_normal():
    assert mdp_robuste("Abc12345!") is True
    assert mdp_robuste("abc") is False


def test_mdp_robuste_limite_8_caracteres():
    assert mdp_robuste("Abcd123!") is True


def test_mdp_robuste_limite_7_caracteres():
    assert mdp_robuste("Abcd12!") is False


def test_mdp_robuste_sans_majuscule():
    assert mdp_robuste("abcdefg1!") is False


def test_mdp_robuste_sans_minuscule():
    assert mdp_robuste("ABCDEFG1!") is False


def test_mdp_robuste_sans_chiffre():
    assert mdp_robuste("Abcdefgh!") is False


def test_mdp_robuste_sans_caractere_special():
    assert mdp_robuste("Abcdefg12") is False


def test_mdp_robuste_erreur():
    with pytest.raises(ErreurEntree):
        mdp_robuste("")


# --- la route ---

def test_route_mdp_robuste_normal():
    r = client.get("/mdp_robuste", params={"mdp": "Abc12345!"})
    assert r.status_code == 200
    assert r.json() == {"mdp": "Abc12345!", "resultat": True}


def test_route_mdp_robuste_faible():
    r = client.get("/mdp_robuste", params={"mdp": "abc"})
    assert r.status_code == 200
    assert r.json() == {"mdp": "abc", "resultat": False}


def test_route_mdp_robuste_vide():
    r = client.get("/mdp_robuste", params={"mdp": ""})
    assert r.status_code == 400
    assert r.json() == {"detail": MDP_VIDE}


def test_route_mdp_robuste_sans_parametre():
    r = client.get("/mdp_robuste")
    assert r.status_code == 400
    assert r.json() == {"detail": PARAMETRE_INVALIDE}