for a in range(9) :
    for b in range(9) :
        for c in range(9) :
            for d in range(9) :
                if (d + 10 * c + 100 * b + 1000 * a) == 4 * (a + 10 * b + 100 * c + 1000 * d) :
                    print("{}{}{}{}".format(a, b, c, d))