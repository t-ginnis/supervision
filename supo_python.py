import numpy as np
N=10000
M=1000
x=np.array([np.cos(i+1) for i in range(N)])
y=np.array([np.cos(2*(i+1)) for i in range(N)])
A=np.array([[np.sin(i-j+1) for i in range(N)] for j in range(N)])

print("Initialised")

for i in range(M):
    D=np.dot(y,np.matmul(np.transpose(A),np.matmul(A,x)))

print(D)
