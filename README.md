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

Une issue par fonction, une branche par issue, une pull request par branche. Personne ne pousse sur `main` : CI verte et une approbation avant de fusionner.

### Branches

`type/numéro-description`, en minuscules, mots séparés par des tirets. Le numéro est celui de l'issue.

```
feat/3-factorielle
fix/18-division-par-zero
docs/21-readme-installation
```

### Commits

Format Conventional Commits : `type(portée): description à l'impératif`, en français, sans majuscule ni point final. La portée est le module ou le fichier concerné.

```
feat(math): ajoute la route /factorielle
fix(math): renvoie 400 si n est négatif
test(texte): couvre la chaîne vide
docs(readme): détaille l'installation
```

| Type | Usage |
|---|---|
| `feat` | nouvelle fonctionnalité |
| `fix` | correction de bug |
| `test` | ajout de tests |
| `docs` | documentation |
| `refactor` | réorganisation sans effet sur le comportement |
| `ci` | GitHub Actions |
| `chore` | maintenance, configuration |

### Pull requests

Le titre reprend le format des commits, la description contient `Closes #numéro` pour fermer l'issue à la fusion.

### Code

| Élément | Convention | Exemple |
|---|---|---|
| Fonction d'un module | nom du sujet, `snake_case`, en français | `factorielle`, `est_premier` |
| Route | même nom que la fonction | `/factorielle/{n}`, `/est_palindrome?texte=` |
| Fonction de route | `route_` + nom de la fonction | `route_factorielle` |
| Test | `test_` + fonction + cas | `test_factorielle_negative` |
| Message d'erreur | constante en majuscules dans `app/erreurs.py` | `PARAMETRE_INVALIDE` |
| Réponse JSON | paramètres reçus + `resultat` | `{"n": 5, "resultat": 120}` |

## Équipe

| Membre | Module | Validation |
|---|---|---|
| Elyas | math | `email_valide` |
| Alex | texte | `mdp_robuste` |
| Arsène | conversion | `code_postal` |
