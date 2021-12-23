def collatz (number) :
    if (number % 2 == 0) :
        print(number // 2)
        return number // 2
    else :
        print(3 * number + 1)
        return 3 * number + 1

i = int(input("Enter number: "))

while True :
    i = collatz(i)
    if (i == 1) :
        break