n = int(input())
h = list(map(int,input().split()))
result = []
for i in range(n):
    sum = 0
    for j in range(n):
        sum += h[j] * abs(i - j)
    result.append(sum)
print(min(result))