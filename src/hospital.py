from src.doctor import Doctor
from src.patient import Patient


class Hospital:
    def __init__(self, nom: str) -> None:
        """
        CLass representant un hopital
        :param nom:
        :return: None
        """
        # TODO test if it's a string in proper manner
        if str(nom).isalnum():
            raise TypeError
        self.__nom = nom.title()
        self.__patients = []
        self.__doctors = []

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def doctors(self) -> list:
        return self.__doctors

    @property
    def patients(self) -> list:
        return self.__patients

    def add_patient(self, patient: Patient) -> None:
        """
        Fonction pour ajouter un nouveau patient
        :param patient:
        :return: None
        """
        if not isinstance(patient, Patient):
            raise TypeError
        self.__patients.append(patient)

    def add_doctor(self, doctor: Doctor) -> None:
        """
        Fonction qui ajoute un nouveau docteur
        :param doctor:
        :return: None
        """
        if not isinstance(doctor, Doctor):
            raise TypeError
        self.__doctors.append(doctor)

    def find_patient(self, nom: str, postnom: str = "", prenom: str = "") -> [Patient]:
        """
        Fonction pour trouver un patient par son nom, prenom ou postnom
        :param nom:
        :param postnom:
        :param prenom:
        :return: Patient[]
        """
        nom = nom.strip().upper()
        prenom = prenom.strip().capitalize() if prenom != "" else nom
        postnom = postnom.strip().upper() if postnom != "" else nom

        patients = []

        for patient in self.__patients:
            if nom in patient.nom or prenom in patient.prenom or postnom in patient.postnom:
                patients.append(patient)

        return patients
