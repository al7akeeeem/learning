import numpy as np
from  scipy.integrate import odeint 
import matplotlib.pyplot as plt # for plotting commands
def deriv(y,t):  # return derivatives of the array y
    a = -2.0
    b = -0.1
    return np.array([ y[1], a*y[0]+b*y[1] ])
time =np.linspace(0.0,10.0,1000)
yinit =np.array([0.0005,0.2])  # initial values
y = odeint(deriv,yinit,time)
plt.plot(time,y[:,0],label='y')  # y[:,0] is the first column of y
plt.plot(time,y[:,1],label="y'")
plt.xlabel('$t$')
plt.ylabel('$y$')
plt.legend()
plt.show()
