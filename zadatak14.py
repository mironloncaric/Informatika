guess = 0
user = ""
n = 0
minimum = 0
maximum = 1000
while True :
    n += 1
    guess = (minimum + maximum) // 2
    print(guess)
    user = input()
    if user[0].lower() == 'm' :
        maximum = guess
    if user[0].lower() == 'v' :
        minimum = guess
    if user[0].lower() == 'p' :
        print("Pogodak!")
        print(n)
        break