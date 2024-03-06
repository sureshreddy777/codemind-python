n = int(input())
l = list(map(int,input().split()))
a = []
b = []
for i in range(0,n):
    if i%2 != 0: a.append(l[i])
    else: b.append(l[i])
s1 = sum(a)
s2 = sum(b)
if s1-s2 == 0: print("YES")
else: print("NO")