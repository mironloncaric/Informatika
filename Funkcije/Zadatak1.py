def definition(num) :
    # i poprima vrijednosti od 1 do 10, ispisuju se umnožak broja num i broja i
    for i in range(1, 11) :
        print("{} * {} = {}".format(num, i, num*i))

# bilo mi je dosadno pa sam dodao error handling
while True :
    # program pokušava unesti cijeli broj te izlazi iz petlje ukoliko uspije
    try :
        num = int(input("--> "))
        break
    # ukoliko program naiđe na pogrešku tipa ValueError ispisuje poruku i vrača se na početak petlje
    except ValueError :
        print("Molim vas unesite cijeli broj --> ")

# zovemo funkciju definition() i unosimo cijeli broj num kao parametar 
definition(num)
