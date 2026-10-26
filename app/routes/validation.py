from fastapi import APIRouter

from app.outils.validation import mdp_robuste

router = APIRouter(tags=["validation"])


@router.get("/mdp_robuste")
def route_mdp_robuste(mdp: str):
    return {"mdp": mdp, "resultat": mdp_robuste(mdp)}