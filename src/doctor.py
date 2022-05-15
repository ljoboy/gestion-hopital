import unittest


class Doctor:
    """
    Class constructor
    """
    def __int__(self, nom: str, prenom: str, postnom: str, phone: str, specialisation: str = "", matricule: str = ""):
        self._nom = nom
        self._prenom = prenom
        self._postnom = postnom
        self._phone = phone
        self._matricule = matricule
        self._specialisation = specialisation
