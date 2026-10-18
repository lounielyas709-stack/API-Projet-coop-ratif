import pytest

from app.erreurs import ErreurEntree
from app.outils.validation import email_valide


def test_email_valide():
    assert email_valide("alex@mail.fr")


def test_email_valide_sans_arobase():
    assert not email_valide("alex.mail.com")


def test_email_valide_avec_deux_apostrphe():
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


def test_email_valide_vide():
    with pytest.raises(ErreurEntree):
        email_valide("")
