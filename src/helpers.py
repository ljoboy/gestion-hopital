import random


def date_generator() -> str:
    """
    Generate an iso formated date
    :return: str
    """
    year = random.randint(1900, 2022)
    month = str(random.randint(1, 12)).zfill(2)
    d = 30 if month != 2 else 28
    day = str(random.randint(1, d)).zfill(2)
    return f"{year}-{month}-{day}"


def random_firstname() -> str:
    """
    Generate a first name
    :return: str
    """
    prenoms = ["melanie", "yves", "esther", "luc", "marc", "jean", "marie", "emily", "deborah", "sam", "sarah"]
    return random.choice(prenoms)


def random_lastname() -> str:
    """
    Generate a lastname
    :return: str
    """
    noms = ["ilunga", "kabongo", "mwape", "kalenga", "kabamba", "yav", "banza", "kitenge", "kasongo", "nyembo"]
    return random.choice(noms)


def random_phone_number() -> str:
    """
    Generate an international phone number as a string
    :return: str
    """
    return "+" + str(random.randint(111111111, 999999999999))