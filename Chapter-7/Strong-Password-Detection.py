import re

string = input()
strongPassword = re.compile(
    r'^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z]).{8,}$')

if(strongPassword.search(string)):
    print('Strong Password: ' + strongPassword.search(string).group())

else:
    print('Weak Password: ' + string)
