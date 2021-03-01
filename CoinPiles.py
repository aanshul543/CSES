t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if (a+b) % 3 != 0:
        print("NO")
    else:
        x = (a+b) // 3
        if a < x or b < x:
            print("NO")
        else:
            print("YES")