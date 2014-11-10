import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from scipy.integrate import ode

## Vector field function
def vf(t,x):
  dx=np.ones(2)
  dx[1]=x[0]**2-x[0]-2
  return dx

#Solution curves
t0=0; tEnd=10; dt=0.01;
r = ode(vf).set_integrator('vode', method='bdf',max_step=dt)
ic=[[-3.5,-10], [-3,-10], [-2.5,-10]]
color=['r','b','g']
for k in range(len(ic)):
    Y=[];T=[];S=[];
    r.set_initial_value(ic[k], t0).set_f_params()
    while r.successful() and r.t +dt < tEnd:
        r.integrate(r.t+dt)
        Y.append(r.y)

    S=np.array(np.real(Y))
    plt.plot(S[:,0],S[:,1], color = color[k], lw = 1.25)

#Vector field
X,Y = np.meshgrid( np.linspace(-10,10,20),np.linspace(-10,10,20) )
U = 1
V = X**2-X-2

#Normalize arrows
N = np.sqrt(U**2+V**2)  
U2, V2 = U/N, V/N
plt.quiver( X,Y,U2, V2)


plt.xlim([-10,10])
plt.ylim([-10,10])
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.show()
