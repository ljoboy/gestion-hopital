import unittest


class Doctor:
    """
    Class representing a doctor
    constructor with some params
        nom: str,
        prenom: str,
        postnom: str,
        phone: str,
    """
    _matricule: str

    def __init__(self, nom: str, prenom: str, postnom: str, phone: str):
        if not str.isalnum(nom) or not str.isalnum(prenom) or not str.isalnum(postnom) or not str.isalnum(phone):
            raise TypeError
        self._nom = nom
        self._prenom = prenom
        self._postnom = postnom
        self._phone = phone

