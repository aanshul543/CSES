t = int(input())
for i in range(t):
    y, x = map(int, input().split())
    m, n, r, res = 0, 0, 0, 0
    if y > x:
        m = y
        n = x
        r = 1
    else:
        m = x
        n = y
        r = 0
    diag = m ** 2 - m + 1
    if m % 2 == 0:
        if r == 1:
            res = diag + m - n
        else:
            res = diag - m + n
    else:
        if r == 1:
            res = diag - m + n
        else:
            res = diag + m - n
    print(res)