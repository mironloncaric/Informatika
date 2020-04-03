n = int(input())
ns = str(n * n)
l = len(ns)
message = ':^{}d'.format(l)
message2 = '{' + message + '}'
for i in range(1, n+1) :
    for j in range(1, n+1) :
        print(message2.format(i * j), end=' ')
    print("\n", end="")