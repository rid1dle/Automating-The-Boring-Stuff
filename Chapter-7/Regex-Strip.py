import re


def stripRegex(string, char=''):
    stripRegex = re.compile(r'^\s+|\s+$')
    return stripRegex.sub(char, string)


print(stripRegex(input()))
