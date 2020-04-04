a = 1
while True :
    s = 5 * a
    for i in range(5) :
        s = 5 / 4 * s + 1
    if s % 1 == 0 :
        break
    else :
        a += 1

print('{} kokosa'.format(s))
    
