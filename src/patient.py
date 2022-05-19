import datetime
import re


class Patient:

    def __init__(self, nom: str, prenom: str, postnom: str, phone: str, dob: str) -> None:
        """
        Classe representant un patient
        :param nom:
        :param prenom:
        :param postnom:
        :param phone:
        :param dob: Date of Birth in iso format (YYYY-MM-DD)
        :return: None
        """
        # TODO change this (if) to assert
        phone_verif = re.fullmatch(r"[+|0]\d{9,}", phone)
        dob_verified = datetime.date.fromisoformat(dob)
        if not isinstance(nom, str) or not isinstance(prenom, str) or not isinstance(postnom, str) or \
                not isinstance(phone, str) or not isinstance(dob, str) or not isinstance(phone_verif, re.Match) or \
                not isinstance(dob_verified, datetime.date):
            raise TypeError
        self.__nom = nom
        self.__prenom = prenom
        self.__postnom = postnom
        self.__phone = phone
        self.__dob = dob_verified

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def prenom(self) -> str:
        return self.__prenom

    @property
    def postnom(self) -> str:
        return self.__postnom

    @property
    def phone(self) -> str:
        return self.__phone

    @property
    def dob(self) -> datetime.date:
        return self.__dob
