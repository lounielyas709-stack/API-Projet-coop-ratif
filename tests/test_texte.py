import pytest
from fastapi.testclient import TestClient

from app.erreurs import TEXTE_VIDE, ErreurEntree
from app.main import app
from app.outils.texte import est_palindrome

client = TestClient(app)


# --- la fonction ---

def test_palindrome_normal():
    assert est_palindrome("kayak") is True
    assert est_palindrome("bonjour") is False


def test_palindrome_limite():
    assert est_palindrome("a") is True
    assert est_palindrome("A man, a plan, a canal: Panama") is True


def test_palindrome_erreur():
    with pytest.raises(ErreurEntree):
        est_palindrome("   ")


# --- la route ---

def test_route_palindrome_normal():
    r = client.get("/est_palindrome/kayak")
    assert r.status_code == 200
    assert r.json() == {"texte": "kayak", "resultat": True}


def test_route_palindrome_erreur():
    r = client.get("/est_palindrome/%20%20")
    assert r.status_code == 400
    assert r.json() == {"detail": TEXTE_VIDE}