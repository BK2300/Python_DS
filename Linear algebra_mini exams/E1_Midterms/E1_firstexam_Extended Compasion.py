import numpy as np

A = np.array([
    [50,100,150,200,250,250,200,150,100,50],
    [40, 90,140,190,240,240,190,140,90,40],
    [30, 80,130,180,230,230,180,130,80,30],
    [20, 70,120,170,220,220,170,120,70,20],
    [10, 60,110,160,210,210,160,110,60,10]
], dtype=float)

B = A[:, ::-1] #mirroring it.

alpha = 0.5

# 1) scalar multiplication
alphaA = alpha * A

# 2) Linear combination
mix = alpha * A + (1 - alpha) * B   # = (A+B)/2 when alpha=0.5

print("0.5 * A =\n", alphaA, "\n")
print("(A+B)/2 =\n", mix, "\n")

# print ranks
print("rank(A)        =", np.linalg.matrix_rank(A))
print("rank(B)        =", np.linalg.matrix_rank(B))
print("rank(0.5*A)    =", np.linalg.matrix_rank(alphaA))
print("rank((A+B)/2)  =", np.linalg.matrix_rank(mix))

