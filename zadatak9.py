n1 = 1
n2 = 1
n3 = 0
print(" {} \n {} ".format(n1, n2))
while n1 + n2 < 1000 :
    n3 = n2
    n2 = n2 + n1
    print(" {} ".format(n2))
    n1 = n3