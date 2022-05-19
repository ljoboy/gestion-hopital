class Hospital:
    def __init__(self, nom: str) -> None:
        """
        CLass representant un hopital
        :param nom:
        :return: None
        """
        if str(nom).isalnum():
            raise TypeError
        self.__nom = nom.title()
        self.__patients = []
        self.__doctors = []

    @property
    def nom(self) -> str:
        return self.__nom
