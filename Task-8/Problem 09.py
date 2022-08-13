p= 5
xy = [map(int, input().split()) for _ in range(p)]
sx, sy, sx2, sxy = map(sum, zip(*[(x, y, x**2, x * y) for x, y in xy]))
b = (p * sxy - sx * sy) / (p * sx2 - sx**2)
a = (sy / p) - b * (sx / p)
print('{:.3f}'.format(a + b * 80))
