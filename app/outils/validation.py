import re

from app.erreurs import CODE_POSTAL_VIDE, ErreurEntree


def code_postal(code: str) -> bool:
    if not code:
        raise ErreurEntree(CODE_POSTAL_VIDE)

    return bool(re.fullmatch(r"\d{5}", code))