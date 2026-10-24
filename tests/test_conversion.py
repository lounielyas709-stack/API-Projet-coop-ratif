
from fastapi.testclient import TestClient

from app.main import app
from app.outils.conversion import euros_devise

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

