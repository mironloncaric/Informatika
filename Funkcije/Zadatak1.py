def definition(num) :
    for i in range(1, 11) :
        print("{} * {} = {}".format(num, i, num*i))

num = int(input("--> "))
definition(num)
