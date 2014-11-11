import numpy as np
from  scipy.integrate import odeint 
import matplotlib.pyplot as plt # for plotting commands
def deriv(y,t):  # return derivatives of the array y
    return np.array([ y[1],np.sin(t)])
time =np.linspace(0.0,10.0,1000)
yinit =np.array([0.0,-1.0])  # initial values
y = odeint(deriv,yinit,time)
plt.plot(time,y[:,0],label='y')  # y[:,0] is the first column of y
plt.plot(time,y[:,1],label="y'")
plt.plot(time,-1*np.cos(time),"--",label="exact sol.")
plt.xlabel('$t$')
plt.ylabel('$y$')
plt.legend()
plt.show()
