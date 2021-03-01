n = int(input())
r = 0
for i in range(1, n+1):
    b = ((i**2) * (i**2 - 1)) // 2
    r = r + i-2
    r = r if r >= 0 else 0
    print(b-8*r)