import re


def nums(input_string):
    return [int(num) for num in re.findall(r"\d+", input_string)]
