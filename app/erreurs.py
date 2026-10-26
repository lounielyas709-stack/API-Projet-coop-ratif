class ErreurEntree(ValueError):
    """Entrée invalide : l'API répond 400 avec le message en détail."""


PARAMETRE_INVALIDE = "paramètre invalide"
N_NEGATIF = "n doit être positif"
N_TROP_GRAND = "n doit être inférieur ou égal à 1000"
