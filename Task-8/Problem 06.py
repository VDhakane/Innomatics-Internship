import math

a = float(input())
b = float(input())
m= b * float(input())
s= math.sqrt(b) * float(input())

print(round(0.5*(1+math.erf((a - m)/(s * math.sqrt(2)))),4))
