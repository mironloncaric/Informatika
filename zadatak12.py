from random import randint
guess = randint(1, 1000)
user_guess = 0
n = 0
while True :
    n += 1
    user_guess = int(input())
    if user_guess < guess : 
        print("Više")
    if user_guess > guess :
        print("Niže")
    if user_guess == guess :
        print("Pogodak!")
        print(n)
        break
