word1 = input()
word2 = input()
usedLetters = []

def check(letter) :
    isWritten = False
    for item in usedLetters :
        if item == letter :
            isWritten = True
    if isWritten == False :
        usedLetters.append(letter)

for letter1 in word1 :
    for letter2 in word2 :
        if letter1 == letter2 :
            check(letter1)

for item in usedLetters :
    print(item)


