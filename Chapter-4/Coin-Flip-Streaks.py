import random
numberOfStreaks = 0
count = 0
j = 2

for experimentNumber in range(10000):

    i = random.randint(0, 1)
    if (j == i):
        count += 1
    else:
        count = 0
    j = i
    if count >= 6:
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
