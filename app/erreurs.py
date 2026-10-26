class ErreurEntree(ValueError):
    """Entrée invalide : l'API répond 400 avec le message en détail."""


PARAMETRE_INVALIDE = "paramètre invalide"
TEXTE_VIDE = "le texte doit contenir au moins une lettre ou un chiffre"
MDP_VIDE = "le mot de passe ne peut pas être vide"
