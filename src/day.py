from enum import IntEnum


class Day(IntEnum):
    """
    Enum representant les jours de la semaine
    LUNDI = 0
    MARDI = 1
    MERCREDI = 2
    JEUDI = 3
    VENDREDI = 4
    SAMEDI = 5
    DIMANCHE = 6
    """
    LUNDI = 0
    MARDI = 1
    MERCREDI = 2
    JEUDI = 3
    VENDREDI = 4
    SAMEDI = 5
    DIMANCHE = 6

    # def __init__(self, value: int):
    #     if not isinstance(value, int):
    #         raise TypeError
    #     if not value < 0 or value > 7:
    #         raise ValueError
