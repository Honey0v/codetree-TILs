a,b = map(int,input().split())
tmp = []
for i in range(0, min(a,b)) :
    if a % i == 0 and b % i == 0 :
        tmp.append(i)
print(max(tmp))