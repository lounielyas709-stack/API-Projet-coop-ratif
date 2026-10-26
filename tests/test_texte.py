import pytest
from fastapi.testclient import TestClient

from app.erreurs import PARAMETRE_INVALIDE, TEXTE_VIDE, ErreurEntree
from app.main import app
from app.outils.texte import est_palindrome, inverser
from app.outils.texte import compter_voyelles, est_palindrome

client = TestClient(app)


# --- est_palindrome : la fonction ---

def test_est_palindrome_normal():
    assert est_palindrome("kayak") is True
    assert est_palindrome("bonjour") is False


def test_est_palindrome_limite():
    assert est_palindrome("a") is True
    assert est_palindrome("A man, a plan, a canal: Panama") is True


def test_est_palindrome_erreur():
    with pytest.raises(ErreurEntree):
        est_palindrome("   ")


# --- est_palindrome : la route ---

def test_route_est_palindrome_normal():
    r = client.get("/est_palindrome", params={"texte": "kayak"})
    assert r.status_code == 200
    assert r.json() == {"texte": "kayak", "resultat": True}


def test_route_est_palindrome_erreur():
    r = client.get("/est_palindrome", params={"texte": "!!"})
    assert r.status_code == 400
    assert r.json() == {"detail": TEXTE_VIDE}


def test_route_est_palindrome_sans_texte():
    r = client.get("/est_palindrome")
    assert r.status_code == 400
    assert r.json() == {"detail": PARAMETRE_INVALIDE}


# --- inverser : la fonction ---

def test_inverser_normal():
    assert inverser("bonjour") == "ruojnob"


def test_inverser_limite():
    assert inverser("a") == "a"
    assert inverser("a b") == "b a"


def test_inverser_erreur():
    with pytest.raises(ErreurEntree):
        inverser("   ")


# --- inverser : la route ---

def test_route_inverser_normal():
    r = client.get("/inverser", params={"texte": "bonjour"})
    assert r.status_code == 200
    assert r.json() == {"texte": "bonjour", "resultat": "ruojnob"}


def test_route_inverser_erreur():
    r = client.get("/inverser", params={"texte": " "})
# --- compter_voyelles : la fonction ---

def test_compter_voyelles_normal():
    assert compter_voyelles("bonjour") == 3


def test_compter_voyelles_limite():
    assert compter_voyelles("bcdfg") == 0
    assert compter_voyelles("ÉCOLE") == 3


def test_compter_voyelles_erreur():
    with pytest.raises(ErreurEntree):
        compter_voyelles("   ")


# --- compter_voyelles : la route ---

def test_route_compter_voyelles_normal():
    r = client.get("/compter_voyelles", params={"texte": "bonjour"})
    assert r.status_code == 200
    assert r.json() == {"texte": "bonjour", "resultat": 3}


def test_route_compter_voyelles_erreur():
    r = client.get("/compter_voyelles", params={"texte": " "})
    assert r.status_code == 400
    assert r.json() == {"detail": TEXTE_VIDE}


def test_route_inverser_sans_texte():
    r = client.get("/inverser")
def test_route_compter_voyelles_sans_texte():
    r = client.get("/compter_voyelles")
    assert r.status_code == 400
    assert r.json() == {"detail": PARAMETRE_INVALIDE}