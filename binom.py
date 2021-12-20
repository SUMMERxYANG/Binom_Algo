from math import exp, sqrt
import numpy as np
#########################################
""" 
Instructions:
rate = 0 if the underlying is a stock, otherwise = q if index, rf if currency, r if futures
"""
S = 50
X = 50
T = 5/12
r = 0.1
sigma = 0.4
n = 5
rate = 0
##########################################

dt = T/n
disc = exp(-r*dt)
u = exp(sigma*sqrt(dt))
d = 1/u
up_arr = np.power(u, np.arange(0, n+1))
down_arr = np.power(d, np.arange(n, -1, -1))

r_adj = r - rate
p = (exp(r_adj*dt)-d)/(u-d)     
q = 1-p

# initialization
ec = np.maximum(0, S * np.multiply(up_arr, down_arr) - X)
ep = np.maximum(0, X - S*np.multiply(up_arr, down_arr))
ac = np.copy(ec)
ap = np.copy(ep)

# calculate the rest (work backwards)
for i in np.arange(n, 0, -1):
    St = S * np.multiply(up_arr[0:i], down_arr[n-i+1:])
    ec = (p*ec[1:i+1] + q*ec[0:i])*disc
    ep = (p*ep[1:i+1] + q*ep[0:i])*disc
    ac = (p*ac[1:i+1] + q*ac[0:i])*disc
    ap = (p*ap[1:i+1] + q*ap[0:i])*disc
    # additional step for american options
    ac = np.maximum(ac, np.maximum(0, St - X))
    ap = np.maximum(ap, np.maximum(0, X - St))

print("Euro Call = ", round(ec[0], 4))
print("Euro Put = ", round(ep[0], 4))
print("Amer Call = ", round(ac[0], 4))
print("Amer Put = ", round(ap[0], 4))

