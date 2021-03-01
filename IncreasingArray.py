n = int(input())
data = list(map(int, input().split()))
c = 0
for i in range(n-1):
    if data[i+1] < data[i]:
        x = data[i] - data[i+1]
        c += x
        data[i+1] = data[i]
print(c)