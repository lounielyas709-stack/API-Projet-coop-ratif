from app.erreurs import TEXTE_VIDE, ErreurEntree


def est_palindrome(texte: str) -> bool:
    # on ne garde que les lettres et les chiffres, en minuscules
    propre = ""
    for caractere in texte:
        if caractere.isalnum():
            propre += caractere.lower()

    # si rien ne reste, l'entrée est invalide
    if propre == "":
        raise ErreurEntree(TEXTE_VIDE)

    # [::-1] lit le texte à l'envers
    return propre == propre[::-1]


def inverser(texte: str) -> str:
    # un texte vide ou fait seulement d'espaces est invalide
    if texte.strip() == "":
        raise ErreurEntree(TEXTE_VIDE)

    # [::-1] lit le texte de la fin vers le début
    return texte[::-1]