p= int(input())
X = list(map(float,input().strip().split()))
Y = list(map(float,input().strip().split()))

mu_x = sum(X) / p
mu_y = sum(Y) / p

stdv_x = (sum([(i - mu_x)**2 for i in X]) / p)**0.5
stdv_y = (sum([(i - mu_y)**2 for i in Y]) / p)**0.5


covar= sum([(X[i] - mu_x) * (Y[i] -mu_y) for i in range(p)])

coefficient = covar/ (p * stdv_x * stdv_y)

print(round(coefficient,3))
