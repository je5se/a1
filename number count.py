n = int(input("write an interger"))

if n > 0:
    i, sum = 1, 0
    while i <= n:
        sum = sum +1
        i += 1
    print("the num is positive")
    print("the sum from 1 to n is : ", sum)
elif n< 0:
    i, sum = -1, 0
    while i >=n:
        sum = sum +i
        i -= 1
    print("the number you enter in negative")
    print("the sum from -1 to n is :", sum)
else:
    print("you enter zero")