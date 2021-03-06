import datetime
import random
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
        if not nom.isalnum() or not prenom.isalnum() or not postnom.isalnum() or not isinstance(phone_verif, re.Match) \
                or not isinstance(dob_verified, datetime.date) or not genre.isalnum():
            raise TypeError
        if genre.lower() not in ["m", "f"]:
            raise ValueError
        self.__nom = nom.lower()
        self.__prenom = prenom.lower()
        self.__postnom = postnom.lower()
        self.__genre = genre.lower()
        self.__phone = phone
        self.__dob = dob_verified
        self.__num_dossier = self.__num_dossier_generator()
        self.__poids = 0
        self.__taille = 0
        self.__plaintes = []

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

    def __num_dossier_generator(self) -> str:
        voyelles = "AEUIOY"
        num_dossier = ""
        for lettre in self.nom:
            if lettre not in voyelles:
                num_dossier += lettre
        num_dossier += str(random.randint(0, 9999)).zfill(4)
        return num_dossier

    @property
    def num_dossier(self) -> str:
        return self.__num_dossier

    def mesures(self, poids: float, taille: int) -> None:
        """
        Reccupere les mesures du patient
        :param poids: en Kg (Kilogrammes)
        :param taille: en cm (Centimetres)
        :return:
        """
        if not str(poids).isnumeric() or not str(taille).isdigit():
            raise TypeError
        self.__poids = float(poids)
        self.__taille = taille

    @property
    def taille(self) -> int:
        return self.__taille

    @property
    def poids(self) -> float:
        return self.__poids

    @property
    def plaintes(self) -> [str]:
        return self.__plaintes

    @plaintes.setter
    def plaintes(self, plainte: str) -> None:
        if not isinstance(plainte, str):
            raise TypeError
        self.__plaintes.append(plainte)

    def __str__(self) -> str:
        return " ".join([self.prenom, self.nom, self.postnom])
