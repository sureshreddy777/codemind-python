from collections import Counter
s = input()
d = Counter(s)
if len(d) >=26:
    print(True)
else:
    print(False)