import pyinputplus as pyip
import random
import time

noOfQuestions = 10
correctAns = 0

for i in range(noOfQuestions):
    no1 = random.randint(0, 9)
    no2 = random.randint(0, 9)

    ans = pyip.inputInt(
        prompt=f"Your Question Number {i + 1} is : {no1} x {no2} \n Ans: ", limit=3, timeout=8, default=-1)

    if (ans == no1 * no2):
        correctAns += 1
        print("Correct :)")
        time.sleep(1)

    else:
        print("Wrong :(")
        time.sleep(1)

print(f"You did good.. Your Score is {correctAns}")
