n = int(input())
if n == 1:
    print(1)
elif n <= 3:
    print("NO SOLUTION")
else:
    lst1 = [x for x in range(1, n+1) if x % 2 == 0]
    lst2 = [x for x in range(1, n+1) if x % 2 != 0]
    print(*(lst1+lst2))