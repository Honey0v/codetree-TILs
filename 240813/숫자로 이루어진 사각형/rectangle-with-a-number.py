a = int(input())
k = 1
i = 1
while(True) :
    print(i, end=' ')
    if k % a == 0 :
        print()
    i += 1
    k += 1
    if i == 10 :
        i = 1
    if k == a*a + 1 :
        break