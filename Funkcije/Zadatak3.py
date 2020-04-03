import cmath

def KvadratnaJednadzba(a, b, c) :

    d = (b**2) - (4*a*c)

    x1 = (-b-cmath.sqrt(d))/(2*a)
    x2 = (-b+cmath.sqrt(d))/(2*a)

    return x1, x2

a = int(input('-->'))
b = int(input('-->'))
c = int(input('-->'))

print('The solution are {} and {}'.format(KvadratnaJednadzba(a, b, c)[0], KvadratnaJednadzba(a, b, c)[1]))
