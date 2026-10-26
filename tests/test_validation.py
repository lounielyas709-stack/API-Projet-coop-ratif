import pytest
from fastapi.testclient import TestClient

from app.erreurs import EMAIL_VIDE, MDP_VIDE, PARAMETRE_INVALIDE, ErreurEntree
from app.main import app
from app.outils.validation import email_valide, mdp_robuste

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
