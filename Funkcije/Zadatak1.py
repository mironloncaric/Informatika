def definition(num) :
    # i poprima vrijednosti od 1 do 10, ispisuju se umnožak broja num i broja i
    for i in range(1, 11) :
        print("{} * {} = {}".format(num, i, num*i))

# unosimo broj i pohranjujemo ga u varjablu num
num = int(input("--> "))

# zovemo funkciju definition() i dajemo joj parametar num
definition(num)
