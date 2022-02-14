a, b, c = (float(input()) for _ in range(3))
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** (0.5)
if S % 2 == 0:
    print(int(S))
else:
    print('{0:.6f}'.format(S))
