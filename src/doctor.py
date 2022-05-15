import unittest


class Doctor:
    """
    Class representing a doctor
    constructor with some params
        nom: str
        prenom: str
        postnom: str
        phone: str
        ---------
    others properties
        specialization: [str]
    """

    def __init__(self, nom: str, prenom: str, postnom: str, phone: str) -> None:
        if not str.isalnum(nom) or not str.isalnum(prenom) or not str.isalnum(postnom) or not str.isalnum(phone):
            raise TypeError
        self._nom = nom
        self._prenom = prenom
        self._postnom = postnom
        self._phone = phone
        self._specialization = []

    @property
    def specialization(self) -> list:
        return self._specialization

    @specialization.setter
    def specialization(self, value: [str]) -> None:
        if isinstance(value, list):
            for val in value:
                if not isinstance(val, str):
                    raise TypeError
                elif val.strip():
                    self._specialization.append(val.strip().lower())
        elif isinstance(value, str):
            self._specialization.append(value.lower())
        else:
            raise TypeError
