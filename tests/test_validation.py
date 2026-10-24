
from fastapi.testclient import TestClient

from app.main import app
from app.outils.validation import code_postal

client = TestClient(app)


# Tests de la fonction code_postal

def test_code_postal_valide():
    assert code_postal("94220") is True
    assert code_postal("75001") is True


def test_code_postal_formats_invalides():
    assert code_postal("123") is False
    assert code_postal("7500A") is False
    assert code_postal("999999") is False


def test_code_postal_vide():
    try:
        code_postal("")
        assert False, "Une ErreurEntree était attendue"
    except ValueError as erreur:
        assert str(erreur) == "le code postal ne doit pas être vide"


# Tests de la route HTTP

def test_route_code_postal_succes():
    reponse = client.get("/code_postal?code=94220")

    assert reponse.status_code == 200
    assert reponse.json() == {
        "code": "94220",
        "resultat": True,
    }


def test_route_code_postal_invalide():
    reponse = client.get("/code_postal?code=7500A")

    assert reponse.status_code == 200
    assert reponse.json() == {
        "code": "7500A",
        "resultat": False,
    }


def test_route_code_postal_vide():
    reponse = client.get("/code_postal?code=")

    assert reponse.status_code == 400
    assert reponse.json()["detail"] == "le code postal ne doit pas être vide"

