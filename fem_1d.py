import numpy as np
import matplotlib.pyplot as plt

eps_0 = 8.8541878176*10e-12 
eps_r = 1.0
eps = eps_0*eps_r
rho_0 = 10e-8 
V_0 = 1.0 

d = 0.1
n = 4

l=d/n

K = np.zeros((n-1, n-1))

for i in range(n-1):
    for j in range(n-1):
        if i == j: K[i,j]=2
        if abs(i-j) == 1:
            K[i,j] = -1
print(K)

V = np.zeros(n + 1)
V[0] = V_0
print(V)
f = np.ones(n-1)*(-(l**2)*rho_0)/(eps)
f[0] += V_0
print(f)
V[1:-1] = np.linalg.solve(K,f)
print(V)

solved = np.linspace(0.0, d, num=n+1)

fig, ax = plt.subplots()
ax.plot(solved,V);
ax.set_xlim(0,d);
plt.show()
