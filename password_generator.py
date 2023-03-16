"""This program generates a random password of a given length and type.
It asks the user if wants to change the password
and if wants to save it to a csv file.
"""

import random
import string
import datetime


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


def change_password():
    """Change the password. Ask user to input
    length and type of the password.
    """

    ask_length = True
    ask_type = True

    # Ask user for the length of the password
    while ask_length:
        length = input("Enter the length of the password: ")
        try:
            length = int(length)
        except ValueError:
            print("The length must be an integer.")
            continue

        ask_length = False

    # Ask user for the type of the password
    while ask_type:
        password_type = input(
            "Enter the type of the password [L]etters, [N]umbers,\
[S]pecial charakters: ")
        password_type = password_type.upper()
        if "L" not in password_type and "N" not in password_type\
                and "S" not in password_type:
            print("The type must contain letters L, N or S.")
            continue

        ask_type = False

    password = generate_password(length, password_type)
    print(f"Your new password is: {password}")

    return password


def save_password(password, password_name):
    """Save the password in a file.

    Parameters
    ------------
        password: str
            The password to save.
        password_name: str
            The name of the password.
    """
    if password_name == "":
        password_name = "no_name"

    with open("passwords.csv", "a") as file:
        file.write(
            f"{datetime.datetime.now()} {password_name} {password}" + "\n")


def print_passwords():
    """Print the passwords from the file."""

    # check if the file exists
    try:
        with open("passwords.csv", "r") as file:
            print(
                "------------------------------------------------------------------------------------")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("There is no file with passwords.")


if __name__ == "__main__":
    loop = True
    while loop:
        password = generate_password()
        print("------------------------------------------------------------------------------------")
        print(f"Random password: {password}")
        print("------------------------------------------------------------------------------------")

        # Ask user if he wants to change the password
        change_password_answer = input(
            "Do you want to change the password? [Y/N]")
        if change_password_answer.lower() == "y"\
                or change_password_answer.lower() == "yes":
            password = change_password()

        # Ask user if he wants to save the password to a csv file
        save_password_answer = input("Do you want to save the password? [Y/N]")
        if save_password_answer.lower() == "y"\
                or save_password_answer.lower() == "yes":
            password_name = input("Enter the name of the password: ")
            save_password(password, password_name)

        # Ask user if wants to generate new password or print passwords
        end_loop_answer = input("Do you want to create new [P]assword or\
[S]how passwords? [P/S]. Press Enter to exit.")
        if end_loop_answer.lower() == "s":
            print_passwords()
        elif end_loop_answer.lower() == "p":
            continue
        else:
            loop = False
