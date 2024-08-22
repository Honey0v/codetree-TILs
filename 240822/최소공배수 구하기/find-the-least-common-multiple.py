n,m = map(int,input().split())
i = 1
while True :
    a = min(n,m) * i
    if (a % max(n,m) == 0) :
        break
    i += 1
print(a)