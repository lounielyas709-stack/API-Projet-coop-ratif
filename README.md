# Mini API

[![CI](https://github.com/lounielyas709-stack/API-Projet-coop-ratif/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/lounielyas709-stack/API-Projet-coop-ratif/actions/workflows/ci.yml)

API FastAPI de petits outils : math, texte, conversion et validation.

## Installation

```bash
git clone https://github.com/lounielyas709-stack/API-Projet-coop-ratif.git
cd API-Projet-coop-ratif
python -m venv .venv
source .venv/bin/activate   # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

## Lancement

```bash
uvicorn app.main:app --reload
```

Documentation interactive : http://localhost:8000/docs

## Utilisation

```bash
curl http://localhost:8000/sante
# {"statut":"ok","version":"1.0.0"}
```

| Module | Routes |
|---|---|
| math | `/factorielle/{n}`, `/est_premier/{n}`, `/pgcd/{a}/{b}` |
| texte | `/est_palindrome?texte=`, `/compter_voyelles?texte=`, `/inverser?texte=` |
| conversion | `/celsius_fahrenheit/{celsius}`, `/km_miles/{km}`, `/euros_devise/{montant}?devise=USD` |
| validation | `/email_valide?email=`, `/mdp_robuste?mdp=`, `/code_postal?code=` |

Une entrée invalide renvoie 400 avec `{"detail": "..."}`.

## Tests

```bash
ruff check .
pytest --cov=app --cov-fail-under=80
```

## Structure

```
app/
├── main.py      assemble les routeurs, /sante, gestion des erreurs
├── erreurs.py   exception ErreurEntree et messages, partagé par tous
├── outils/      fonctions pures, un fichier par module
└── routes/      un APIRouter par module
tests/           un fichier de test par module
```

Une fonction de `app/outils/` lève `ErreurEntree` sur entrée invalide, `main.py` la transforme en 400 : pas de `try/except` dans les routes.

## Contribuer

- Une issue par fonction, une branche par issue : `feat/12-factorielle`
- Commits au format Conventional Commits : `feat(math): ajoute factorielle`
- Pull request vers `main`, CI verte et une approbation avant de fusionner

## Équipe

| Membre | Module | Validation |
|---|---|---|
| Elyas | math | `email_valide` |
| Alex | texte | `mdp_robuste` |
| Arsène | conversion | `code_postal` |
