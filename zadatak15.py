a = int(input())
prost = True
for i in range(a//2, 1, -1) :
    print("{} % {} = {}".format(a, i, a % i))
    if a % i == 0 :
        prost = False       
        break
if prost == False :
    print("Broj nije prost")
else :
    print("Broj je prost")