import datetime
import re


class Patient:

    def __init__(self, nom: str, prenom: str, postnom: str, phone: str, dob: str, genre: str) -> None:
        """
        Classe representant un patient
        :param nom:
        :param prenom:
        :param postnom:
        :param phone:
        :param dob: Date of Birth in iso format (YYYY-MM-DD)
        :param genre:
        :return: None
        """
        # TODO change this (if) to assert
        phone_verif = re.fullmatch(r"[+|0]\d{9,}", phone)
        dob_verified = datetime.date.fromisoformat(dob)
        if not isinstance(nom, str) or not isinstance(prenom, str) or not isinstance(postnom, str) or \
                not isinstance(phone, str) or not isinstance(dob, str) or not isinstance(phone_verif, re.Match) or \
                not isinstance(dob_verified, datetime.date) or not isinstance(genre, str):
            raise TypeError
        if genre.lower() not in ["m", "f"]:
            raise ValueError
        self.__nom = nom.lower()
        self.__prenom = prenom.lower()
        self.__postnom = postnom.lower()
        self.__genre = genre.lower()
        self.__phone = phone
        self.__dob = dob_verified

    @property
    def nom(self) -> str:
        return self.__nom.upper()

    @property
    def prenom(self) -> str:
        return self.__prenom.capitalize()

    @property
    def postnom(self) -> str:
        return self.__postnom.upper()

    @property
    def phone(self) -> str:
        return self.__phone

    @property
    def dob(self) -> datetime.date:
        return self.__dob

    @property
    def genre(self) -> str:
        return self.__genre

    @property
    def nom_complet(self) -> str:
        return f"{self.nom} {self.postnom} {self.prenom}"

    @property
    def age(self) -> int:
        return datetime.date.today().year - self.dob.year

