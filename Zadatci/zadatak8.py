a = int(input("->"))
najveci = a
najmanji = a
count = 0
for i in range(9) :
    a = int(input("->"))
    if a > najveci :
        najveci = a
    if a < najmanji :
        najmanji = a
    if a % 3 == 0 :
        count += 1
print("najveci -> {}\nnajmanji -> {}\ndjeljivo s 3 -> {}".format(najveci, najmanji, count))
    