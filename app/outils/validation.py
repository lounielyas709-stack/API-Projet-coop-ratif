from app.erreurs import EMAIL_VIDE, ErreurEntree


def email_valide(email: str) -> bool:
    if email == "":
        raise ErreurEntree(EMAIL_VIDE)
    if email.count("@") != 1:
        return False
    for caractere in email:
        if caractere.isspace():
            return False
    avant, apres = email.split("@")
    if avant == "":
        return False
    if "." not in apres or apres.startswith(".") or apres.endswith("."):
        return False
    if ".." in apres:
        return False

    return True
