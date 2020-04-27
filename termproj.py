import numpy as np 
import matplotlib.pyplot as plt


DT = 0.01
Tfinal = 10
N = int(Tfinal/DT)

y = np.zeros((N, 100))


def initial_y(i):
    if i<20:
        return 4*(i)
    else:
        return -1*(i)+99
    
        



for j in range(1, 100):
    y[0, j] = initial_y(j) 
    
print(y)
plt.plot(y)




#make a tuple so that we can itterate through each row and each column

'''

for a in range(1,100):
    for b in range(1, 100):
            y[b, a+1]=(2-2*(r**2)-6*10**(r**2M**2))*(y[a, b]-y[a, b-1]) + r**2(1+4*10**(M**2))*(y[a+1, b] + y[a-1, b]) - 10**((r**2)*(M**2))*(y[a+2, b] + y[a-2, b])

print(y)
    
'''

