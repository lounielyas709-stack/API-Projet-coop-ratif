## Quoi

<!-- Ce que la PR ajoute ou change, en une ou deux phrases. -->

## Pourquoi

Closes #

## Comment tester

```bash
pytest tests/test_<module>.py
```

## Vérifications

- [ ] Un seul sujet, annoncé dans le titre (`feat(math): ajoute la route /factorielle`)
- [ ] 3 tests minimum par fonction : normal, limite, erreur
- [ ] `ruff check .` et `pytest --cov=app --cov-fail-under=80` passent en local
- [ ] Messages d'erreur ajoutés dans `app/erreurs.py`
- [ ] Un relecteur assigné
