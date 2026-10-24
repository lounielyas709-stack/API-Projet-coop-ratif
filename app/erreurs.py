class ErreurEntree(ValueError):
    """Entrée invalide : l'API répond 400 avec le message en détail."""


PARAMETRE_INVALIDE = "paramètre invalide"


TEMPERATURE_SOUS_ZERO_ABSOLU = (
    "la température ne peut pas être inférieure au zéro absolu"
)
