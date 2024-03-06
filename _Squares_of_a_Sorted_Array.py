n = int(input())
l = list(map(int,input().split()))
a = [i*i for i in l]
a.sort()
for i in a:
    print(i,end = " ")