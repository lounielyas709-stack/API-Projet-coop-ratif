import pytest
from fastapi.testclient import TestClient

from app.erreurs import EMAIL_VIDE, ErreurEntree
from app.main import app
from app.outils.validation import email_valide

client = TestClient(app)


def test_email_valide():
    assert email_valide("alex@mail.fr")


def test_email_valide_sans_arobase():
    assert not email_valide("alex.mail.com")


def test_email_valide_avec_deux_arobase():
    assert not email_valide("alex@@mail.com")


def test_email_valide_rien_avant_arobase():
    assert not email_valide("@mail.fr")


def test_email_valide_sans_point_apres_arobase():
    assert not email_valide("alex@mail")


def test_email_valide_point_au_bord():
    assert not email_valide("alex@.fr")
    assert not email_valide("alex@mail.")


def test_email_valide_espace():
    assert not email_valide("alex@ma il.fr")


def test_email_valide_tabulation():
    assert not email_valide("alex@ma\til.fr")


def test_email_valide_points_consecutifs():
    assert not email_valide("alex@ma..fr")


def test_email_valide_vide():
    with pytest.raises(ErreurEntree):
        email_valide("")


def test_route_email_valide():
    reponse = client.get("/email_valide?email=alex@mail.fr")
    assert reponse.status_code == 200
    assert reponse.json() == {"email": "alex@mail.fr", "resultat": True}


def test_route_email_invalide():
    reponse = client.get("/email_valide?email=alex.mail.fr")
    assert reponse.status_code == 200
    assert reponse.json() == {"email": "alex.mail.fr", "resultat": False}


def test_route_email_valide_vide():
    reponse = client.get("/email_valide?email=")
    assert reponse.status_code == 400
    assert reponse.json() == {"detail": EMAIL_VIDE}
