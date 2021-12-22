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
            question - string to ask the user
            default (1) - 1 defaults to yes, 0 defaults to no, 2 has no default
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