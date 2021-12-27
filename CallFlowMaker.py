##########
# Author: Skylar Baker
# Title: Text based call flow maker
##########

# Notes
# Questions passed to helpers should NOT include a newline, helpers add the newline

# Imports
import re
from enum import Enum

# Globals
class LineType(Enum):
    TOD = 1
    MLHG = 2
    AA = 3
    SUB = 4
    VM = 5

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
        print("Please enter a {ext_len} digit number".format(ext_len=ext_len))
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

    number = ""
    for c in answer:
        if not c in ["(", " ", ")", "-"]:
            number += c
    return number

def get_valid_forward(question, ext_len=4):
    """
        Get an input from the end user and verify it is either a valid phone number or extension format

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
    input_format = re.compile(r"^((\(?\d{3}\)?\s?-?\d{3}\s?-?\d{4})|(\d{" + str(ext_len) + "}))$")
    answer = input("{question}\n".format(question=question))

    while not re.match(input_format, answer):
        print("Please enter a 10 digit phone number or {ext_len} digit extension".format(ext_len=ext_len))
        answer = input("{question}\n".format(question=question))

    number = ""
    for c in answer:
        if not c in ["(", " ", ")", "-"]:
            number += c
    return number

def get_line_type(ext):
    """
        Get an input from the end user and match it to a line type

        Inputs:
            ext = string with the extension in question

        Recognized line types:
            TOD
            MLHG
            AA
            SUB
            VM
    """
    answer = input("What type of line is {ext}?\n1 - TOD\n2 - MLHG\n3 - AA\n4 - Subscriber\n5 - Voicemail box\n")
    answer_format = re.compile(r"^[1-5]$")

    while not re.match(answer_format, answer):
        answer = input("What type of line is {ext}?\n1 - TOD\n2 - MLHG\n3 - AA\n4 - Subscriber\n5 - Voicemail box\n")

    answer = int(answer) # Regex already verified it was an int, so it's safe to cast
    if answer == 1:
        return LineType.TOD
    elif answer == 2:
        return LineType.MLHG
    elif answer == 3:
        return LineType.AA
    elif answer == 4:
        return LineType.SUB
    elif answer == 5:
        return LineType.VM

# Main code
def setup():
    """
        Ask the user questions to set up the business group.
    """
    name = input("What is the name of the business?\n")
    ext_len = get_valid_extension("How long are the extensions?", 1) # We need a number between 0 and 9, this is like a 1 digit extension
    full_main_num = get_valid_phone_number("What is the 10 digit number of the main line?")
    ext_main_num = get_valid_extension("What is its extension?", ext_len)

    bg = {
        "name": name,
        "ext_len": ext_len,
        "main_num": full_main_num,
        "main_ext": ext_main_num,
        "main_type": ""
    }

def update(bg):
    """
        Updates the business group after changes
    """
    pass

def update_exts(bg):
    """
        Iterates through the connections specified to determine if we have any unprovisioned extensions
    """
    pass

def main():
    """
        Main logic
    """
    pass

if __name__ == "__main__":
    main()