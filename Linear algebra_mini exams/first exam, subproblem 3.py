import numpy as np

A = np.array([
    [50,100,150,200,250],
    [40,90,140,190,240],
    [30,80,130,180,230],
    [20,70,120,170,220],
    [10,60,110,160,210]
])

B = A[:, ::-1] #Mirroring

alpha = 0.5
result = alpha*A + (1-alpha)*B

print(result)
