"""This program generates a random password of a given length and type."""

import random
import string


def generate_password(length=9, password_type="LNS"):
    """Generate a random password of a given length and type.

    Parameters
    ------------
        length: int
            Length of the password (default 9)
        password_type: str
            Type of the password. (default "LNS")
            L : Letters (upper and lower case)
            N : Numbers
            S : Special characters
    Return
    -----------
        password: str
    """

    password_base = ""
    password = ""

    if "L" in password_type:
        password_base += string.ascii_letters
    if "N" in password_type:
        password_base += string.digits
    if "S" in password_type:
        password_base += string.punctuation

    for _ in range(length):
        password += random.choice(password_base)

    return password


if __name__ == "__main__":
    print(generate_password())
