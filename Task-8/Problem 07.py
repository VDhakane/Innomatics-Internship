m, s = 500, 80


muS, sigmaS = m, s/(100**0.5)


A = m - (1.96*sigmaS)
B = m + (1.96*sigmaS)

print(round(A,2))
print(round(B,2))
