a,b = map(int,input().split())
tmp = [1]
for i in range(1, min(a,b)) :
    if a % i == 0 and b % i == 0 :
        tmp.append(i)
print(max(tmp))