from app.erreurs import MDP_VIDE, ErreurEntree

LONGUEUR_MIN = 8


def mdp_robuste(mdp: str) -> bool:
    # un mot de passe vide est une entrée invalide
    if mdp == "":
        raise ErreurEntree(MDP_VIDE)

    # trop court : le mot de passe n'est pas robuste
    if len(mdp) < LONGUEUR_MIN:
        return False

    a_majuscule = False
    a_minuscule = False
    a_chiffre = False
    a_special = False

    for caractere in mdp:
        if caractere.isupper():
            a_majuscule = True
        elif caractere.islower():
            a_minuscule = True
        elif caractere.isdigit():
            a_chiffre = True
        else:
            a_special = True

    return a_majuscule and a_minuscule and a_chiffre and a_special
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
