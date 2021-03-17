n = int(input())
s = n*(n+1)//2
if s % 2 == 0:
    print("YES")
    if n % 2 == 0:
        x = n // 4
        print(2*x)
        for i in range(1, x+1):
            print(i, end=' ')
        for i in range(3*x+1, n+1):
            print(i, end=' ')
        print()
        print(2*x)
        for i in range(x+1, 2*x+1):
            print(i, end=' ')
        for i in range(2*x+1, 3*x+1):
            print(i, end=' ')
    else:
        n = n - 3
        x = n // 4
        print(2*x + 2)
        print(1, 2, end=' ')
        for i in range(1+3, x+1+3):
            print(i, end=' ')
        for i in range(3*x+1+3, n+1+3):
            print(i, end=' ')
        print()
        print(2*x + 1)
        print(3, end=' ')
        for i in range(x+1+3, 2*x+1+3):
            print(i, end=' ')
        for i in range(2*x+1+3, 3*x+1+3):
            print(i, end=' ')
else:
    print("NO")