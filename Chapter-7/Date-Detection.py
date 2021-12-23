import re

dateReg = re.compile(
    r'(?P<Day>0[1-9]|[12][0-9]|3[01])(?P<Delimiter>[./-])(?P<Month>0[1-9]|1[012])\2(?P<Year>(?:19|20)\d\d)')


val = dateReg.search(input())
if (val):

    day, _, month, year = val.groups()

    if (month == '04' or month == '06' or month == '09' or month == '11'):
        if (day != '30'):
            print("Invalid Date: " + val.group())

    elif (month == '02'):
        if (int(day) > 29):
            print("Invalid Date: " + val.group())
        elif (day == '29' and (int(year) % 4 != 0 or int(year) % 400 != 0)):
            print("Invalid Date: " + val.group())

    else:
        print("Valid Date: " + val.group())

else:
    print('Invalid Syntax')
