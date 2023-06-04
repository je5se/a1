import random
# count = 0

print("Welcome to J's number guessing game.")
n = int(input("Guess a number: "))
r = random.randint(1,100)

while (n != r):
    if n>r:
        print("Guess is too large")
        n = int(input("Guess again: "))
    elif n<r:
        print("Guess is too small")
        n = int(input("Guess again: "))

print("Correct guess, you win!")
# user_input = input("")
# count  += 1

# print(count)