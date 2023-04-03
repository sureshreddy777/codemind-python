t = input()

h, m = map(int, t.split(':'))

ha = (h % 12) * 30 + m * 0.5

ma = m* 6

ad = abs(ha - ma)

m = min(ad, 360-ad)

print(m)
