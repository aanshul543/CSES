from sys import stdin, stdout
n = int(stdin.readline())
stdout.write("%s" %n)
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3*n + 1
    stdout.write(" %s" %n)