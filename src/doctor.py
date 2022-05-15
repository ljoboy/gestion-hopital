import unittest


class Doctor:
    """
    Class constructor
    """
    def __int__(self, nom: str, prenom: str, postnom: str, phone: str, matricule: str, specialisation: str):
        self.nom = nom
        self.prenom = prenom
        self.postnom = postnom
        self.phone = phone
        self.matricule = matricule
        self.specialisation = specialisation
