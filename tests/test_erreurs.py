from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.erreurs import PARAMETRE_INVALIDE, ErreurEntree
from app.main import app


def _app_de_test() -> FastAPI:
    essai = FastAPI()
    essai.exception_handlers.update(app.exception_handlers)

    @essai.get("/essai/{n}")
    def route_essai(n: int):
        if n < 0:
            raise ErreurEntree("n doit être positif")
        return {"n": n}

    return essai


client_essai = TestClient(_app_de_test())


def test_entree_valide():
    assert client_essai.get("/essai/1").status_code == 200


def test_erreur_entree_renvoie_400():
    r = client_essai.get("/essai/-1")
    assert r.status_code == 400
    assert r.json() == {"detail": "n doit être positif"}


def test_type_invalide_renvoie_400():
    r = client_essai.get("/essai/abc")
    assert r.status_code == 400
    assert r.json() == {"detail": PARAMETRE_INVALIDE}
