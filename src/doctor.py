import datetime
import re


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
    __i = 1

    def __init__(self, nom: str, prenom: str, postnom: str, phone: str) -> None:
        tel = re.fullmatch(r"^[0|+]\d{9,}", phone)
        if not str.isalnum(nom) or not str.isalnum(prenom) or not str.isalnum(postnom) \
                or len(phone) < 10 or not isinstance(tel, re.Match):
            raise TypeError
        self.__nom = nom
        self.__prenom = prenom
        self.__postnom = postnom
        self.__phone = phone
        self.__specialization = []
        self.__matricule = self.__matricule_generator()

        self.__class__.__i += 1

    @property
    def specialization(self) -> list:
        return self.__specialization

    @specialization.setter
    def specialization(self, value: [str]) -> None:
        if isinstance(value, list):
            for val in value:
                if not isinstance(val, str):
                    raise TypeError
                elif val.strip():
                    self.__specialization.append(val.strip().lower())
        elif isinstance(value, str):
            self.__specialization.append(value.lower())
        else:
            raise TypeError

    @property
    def matricule(self) -> str:
        return self.__matricule

    def __matricule_generator(self) -> str:
        """
        method to generate a matricule
        """
        mat = str(datetime.datetime.now().year)[-2:]
        s = str(self.__i)
        s = ("0" * (3 - len(s))) + s
        mat += self.__nom[0].upper() + self.__postnom[0].upper() + s
        return mat
