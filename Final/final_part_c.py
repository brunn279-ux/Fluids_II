from colorspacious import cspace_converter
import numpy as np
import matplotlib.pyplot as plt
import math

def compZ(zeta):
    return zeta + 1/zeta
    #return (a+1/a)*np.cos(theta) + 1j*(a-1/a)*np.sin(theta)
def compZeta(a, m, theta):
    return a*np.exp(1j*theta)-m
    #return a*np.cos(theta)+1j*a*np.sin(theta)

def zetafz(z, m):
    return 0.5*(z+np.sqrt(z-2)*np.sqrt(z+2))+m
def cylFlow(zeta, U, a, m):
    return U*zeta+U*a*a/zeta
def find_nearest(array,value): #pulled from stack exchange
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return idx-1
    else:
        return idx

x = np.linspace(-3, 3, 1001)
y = np.linspace(-3, 3, 1001)

xx, yy = np.meshgrid(x,y)

zz = xx + 1j*yy

theta = np.linspace(0,2*np.pi, 500)

midpoint = np.pi

midpointind = find_nearest(theta, midpoint)
#print(midpointind)

m004 = 0.03181286228622863
m008 = 2.065*0.03181286228622863

m004_book = 0.04/1.3
m008_book = 0.08/1.3

a004 = 1.0 + m004
a008 = 1.0 + m008

U_inf = 1.0

zetzet = zetafz(zz, m008)
Fzet = cylFlow(zetzet, U_inf, a008, m008)

Zout = compZ(Fzet)

zeta004 = compZeta(a004,m004,theta)
z004 = compZ(zeta004)

#print(zeta.real)
#print(a*np.cos(theta))
#print(z)

top = np.max(z004.imag)
bottom = np.min(z004.imag)

left = np.min(z004.real)
right = np.max(z004.real)

t = top-bottom
l = right-left

ratio004 = t/l

zeta008 = compZeta(a008,m008,theta)
z008 = compZ(zeta008)

#print(zeta.real)
#print(a*np.cos(theta))
#print(z)

top = np.max(z008.imag)
bottom = np.min(z008.imag)

left = np.min(z008.real)
right = np.max(z008.real)

t = top-bottom
l = right-left

ratio008 = t/l

print(ratio004, ratio008)
#print(ratio004_book, ratio008_book) this line of code didnt work, 
#but the book numbers are way off of what you got numerically

fig1, axs = plt.subplots(1,2)

axs[0].plot(zeta004.real, zeta004.imag)
axs[0].set_aspect('equal', adjustable='datalim')
axs[1].plot(z004.real, z004.imag)
axs[1].set_aspect('equal', adjustable='datalim')

axs[0].grid(True)
axs[1].grid(True)

fig2, axs = plt.subplots(1,2)

axs[0].plot(zeta008.real, zeta008.imag)
axs[0].set_aspect('equal', adjustable='datalim')
axs[1].plot(z008.real, z008.imag)
axs[1].set_aspect('equal', adjustable='datalim')


axs[0].grid(True)
axs[1].grid(True)

fig3, ax = plt.subplots()

Contour = ax.contour(xx, yy, Fzet.imag, 30, cmap='plasma')
ax.grid(True)

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
