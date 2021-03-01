s = input()
c, m = 1, 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        c += 1
    else:
        c = 1
    if m < c:
        m = c
print(m)