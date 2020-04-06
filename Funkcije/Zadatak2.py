def Function(str1, str2) :
    # lista brojeva koji su već ispisani i ne treba ih ponovno ispisivati
    koristeni_brojevi = []
    # prolazimo kroz string str1 znak po znak pri čemu varjabla slovo1 poprima vrijednost znaka
    for slovo1 in str1 :
        # prolazimo kroz string str2 znak po znak pri čemu varjabla slovo2 poprima vrijednost znaka
        for slovo2 in str2 :
            # provjeravamo je li sadržaj varjable slovo1 jednako sadržaju varjable slovo2
            if slovo1 == slovo2 :
                koristeno = False
                # provjeravamo je li slovo već ispisano 
                for element in koristeni_brojevi :
                    if element == slovo1 :
                        koristeno = True
                if koristeno == False :
                    print(slovo1)
                    # ako slovo nije ispisano, dodajemo ga na listu da ga program više ne ispisuje
                    koristeni_brojevi.append(slovo1)
                
# pomoću funkcije split() razdvajamo unos u dvije varjable (str1, str2)
str1, str2 = input('--> ').split()
# zovemo funkciju Function() i dajemo joj parametre str1 i str2
Function(str1, str2)
