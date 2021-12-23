##########
# Author: Skylar Baker
# Title: Text based call flow maker
##########

# Notes
# Questions passed to helpers should NOT include a newline, helpers add the newline

# Imports
import re

# Helpers
def get_yes_no_input(question, default=2):
    """
        Get an input from the end user and verify it is a y or n

        Inputs:
            question = string to ask the user
            default (1) = 1 defaults to yes, 0 defaults to no, 2 has no default
    """
    answer_format = re.compile(r"^Y|y|N|n$")
    answer = input("{question}\ny/n\n".format(question=question))

    while not re.match(answer_format, answer):
        if not answer:
            if default == 0:
                return False
            elif default == 1:
                return True
        print("Please enter y or n")
        answer = input("{question}\n".format(question=question))

    if re.match(re.compile(r"y|Y"), answer):
        return True
    elif re.match(re.compile(r"n|N"), answer):
        return False

def get_valid_extension(question, ext_len=4):
    """
        Get an input from the end user and verify it is the correct extension length

        Inputs:
            question = string to ask the user
            ext_len (4) = length of extensions
    """
    ext_format = re.compile(r"^\d{" + str(ext_len) + "}$")
    answer = input("{question}\n".format(question=question))

    while not re.match(ext_format, answer):
        print("Please enter a {ext_len} number".format(ext_len=ext_len))
        answer = input("{question}\n".format(question=question))
    
    return answer

def get_valid_phone_number(question):
    """
        Get an input from the end user and verify it is a valid phone number format

        Inputs:
            question = string to ask the user

        Recognized formats:
            1234567890
            123 456 7890
            123-456-7890
            (123)4567890
            (123) 456 7890
            (123) 456-7890
            (123)-456-7890
    """
    dn_format = re.compile(r"^\(?\d{3}\)?\s?-?\d{3}\s?-?\d{4}$")
    answer = input("{question}\n".format(question=question))

    while not re.match(dn_format, answer):
        print("Please enter a 10 digit phone number")
        answer = input("{question}\n".format(question=question))

    return True