from sys import stdin, stdout
n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
tsum = (n*(n+1))//2
dsum = sum(data)
stdout.write("%s" %(tsum-dsum))