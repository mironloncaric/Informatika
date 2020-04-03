def Function(str1, str2) :
    koristeno = False
    koristeni_brojevi = []
    for slovo1 in str1 :
        for slovo2 in str2 :
            if slovo1 == slovo2 :
                koristeno = False
                for element in koristeni_brojevi :
                    if element == slovo1 :
                        koristeno = True
                if koristeno == False :
                    print(slovo1)
                    koristeni_brojevi.append(slovo1)
                
str1, str2 = input('--> ').split()

Function(str1, str2)
