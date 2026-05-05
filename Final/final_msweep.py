import numpy as np
import matplotlib.pyplot as plt
import math

def compZ(zeta):
    return zeta + 1/zeta
    #return (a+1/a)*np.cos(theta) + 1j*(a-1/a)*np.sin(theta)
def compZeta(a, m, theta):
    return a*np.exp(1j*theta)-m
    #return a*np.cos(theta)+1j*a*np.sin(theta)

theta = np.linspace(0,2*np.pi, 100)

tol = 0.000001

m = np.linspace(0.00001, 1.0, 10000)

for lv1 in range(m.size):
    miter = m[lv1]
    #print(miter)
    a = 1.0 + miter

    zeta = compZeta(a,miter,theta)
    z = compZ(zeta)

    #print(zeta.real)
    #print(a*np.cos(theta))
    #print(z)

    top = np.max(z.imag)
    bottom = np.min(z.imag)

    left = np.min(z.real)
    right = np.max(z.real)

    t = top-bottom
    l = right-left

    ratio = t/l

    if (abs(ratio-0.08))<tol:
        m008 = miter
        print(m008,ratio)
        break


fig1, axs = plt.subplots(1,2)

axs[0].plot(zeta.real, zeta.imag)
axs[0].set_aspect('equal', adjustable='datalim')
axs[1].plot(z.real, z.imag)
axs[1].set_aspect('equal', adjustable='datalim')

axs[0].grid(True)
axs[1].grid(True)

#fig2, axs = plt.subplots(1,2)

#axs[0].plot(theta, zeta.imag)
#axs[1].plot(theta, a*np.sin(theta))

#fig3, axs = plt.subplots(1,2)
#
#axs[0].plot(theta, z.real)
#axs[1].plot(theta, z.imag)
#
#fig4, axs = plt.subplots(1,2)
#
#axs[0].plot(theta, np.sin(theta))
#axs[1].plot(theta, np.cos(theta))


plt.show()
