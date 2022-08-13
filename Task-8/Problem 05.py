import math

a= int(input())
n = int(input())
m = int(input())
b = int(input())

mu_sum = n * m
sigma_sum = math.sqrt(n) * b

def cdf(a, m, b):
    Z = (a - m)/b
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(cdf(a, mu_sum, sigma_sum), 4))
