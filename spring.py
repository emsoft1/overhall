import numpy as np 
import time
import pandas as pd
import matplotlib.pyplot as plt
print("Wlecome to the spring test ")


m = 0.1
k = 10.5
g = np.array([0,-9.8,0])
L0 = 0.07
t = 0
dt = 0.01
top=  np.array([0,0,0])
mass_pos= top-np.array([0,L0,0])
mass_m = m* np.array([0,0,0])
fulldata = np.array([[0,0,0]])
while t < 5:
    
    L = mass_pos - top
    
    F = -k*(np.linalg.norm(L)-L0)*np.linalg.norm(L) + m*g
    mass_m = mass_m + F*dt
    mass_pos = mass_pos + mass_m*dt/m
    
    t = t + dt
    # data = np.append(mass_pos ,t)
    if mass_pos[1]==float('-inf') :
        print ("oh nooo")
    else:
        if mass_pos[1] > -50 :  
            fulldata = np.concatenate((fulldata ,[mass_pos]))
        
    time.sleep(0.01)
    # print (5-t)

# fulldata = np.concatenate(fulldata ,[69,87,99])
# print(fulldata)    

fulldata222 = np.array([[2,5,5],
                       [3,4,3],
                       [4,7,8],
                       [21,4,9],
                       [25,8,65],
                       [1,7,7],
                       [8,9,5],
                       [9,4,8]
                       ]
                       
                       )
df = pd.DataFrame(fulldata, columns = ['X','Y','Z'])
df.to_csv("./data.csv") # location adress for saving the data
print(df)
df.plot()
plt.show()
# print(type(df)).