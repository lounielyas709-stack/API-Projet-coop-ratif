class ErreurEntree(ValueError):
    """Entrée invalide : l'API répond 400 avec le message en détail."""


PARAMETRE_INVALIDE = "paramètre invalide"
N_NEGATIF = "n doit être positif"
N_TROP_GRAND = "n doit être inférieur ou égal à 1000"
A_B_NEGATIF = "a et b doivent être positifs ou nuls"
A_B_NULS = "a et b ne peuvent pas être tous deux nuls"
TEXTE_VIDE = "le texte doit contenir au moins une lettre ou un chiffre"
PREMIER_TROP_GRAND = "n doit être inférieur ou égal à 1000000000000"
