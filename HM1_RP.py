#HOMEWORK 1 - Riccardo Paladin
#FA 595

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,20,0.01)
s = np.sin(x)
c = np.cos(x)
plt.plot(x,s,x,c)                  #Plot with sin and cos
plt.title('Plot of sin and cos')   #Title
plt.xlabel('x value range 0 20')   #Lable X
plt.ylabel('sin and cos')          #Lable Y
plt.legend(['sin(x)', 'cos(x)'])   #Legend

plt.show()






