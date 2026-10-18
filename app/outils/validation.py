from app.erreurs import EMAIL_VIDE, ErreurEntree


def email_valide(email: str) -> bool:
    if email == "":
        raise ErreurEntree(EMAIL_VIDE)
    if email.count("@") != 1:
        return False
    if " " in email:
        return False
    avant, apres = email.split("@")
    if avant == "":
        return False
    if "." not in apres or apres.startswith(".") or apres.endswith("."):
        return False

    return True
