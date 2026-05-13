from colorspacious import cspace_converter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math

from funcScript import *

x = np.linspace(-3, 3, 1001)
y = np.linspace(-3, 3, 1001)

xx, yy = np.meshgrid(x,y)

zz = xx + 1j*yy


theta = np.linspace(0,2*np.pi, 500)

m004 = 0.03181286228622863
m008 = 2.065*0.03181286228622863

m004_book = 0.04/1.3
m008_book = 0.08/1.3

a004 = 1.0 + m004
a008 = 1.0 + m008

U_inf = 1.0
aoa = 4.0 #deg
rho = 1.0

midpoint = np.pi

midpointind = find_nearest(theta, midpoint)

zetzet004 = zetafz(zz, m004)
zetzet008 = zetafz(zz, m008)
Fzet008 = cylFlow(zetzet008, U_inf, a008, m008)
print(aoa)
Fzet004_AOA4 = foilFlowAOA(zetzet004, U_inf, a004, aoa)
Fzet008_AOA4 = foilFlowAOA(zetzet008, U_inf, a008, aoa)

Zout = compZ(Fzet008)

zeta004 = compZeta(a004,m004,theta)
z004 = compZ(zeta004)

#print(zeta.real)
#print(a*np.cos(theta))
#print(z)
ratio004 = thickVal(z004)

zeta008 = compZeta(a008,m008,theta)
z008 = compZ(zeta008)

#print(zeta.real)
#print(a*np.cos(theta))
#print(z)

ratio008 = thickVal(z008)

cumLen004 = np.zeros(midpointind)
cumLen008 = np.zeros(midpointind)

for lv1 in range(midpointind-1):
    backlv1 = midpoint-lv1 #sort this out because right now I think cumlen is backwards
    cumLen004[lv1+1] = cumLen004[lv1]+((z004[lv1+1]-z004[lv1]).real**2+(z004[lv1+1]-z004[lv1]).imag**2)**0.5
    cumLen008[lv1+1] = cumLen008[lv1]+((z008[lv1+1]-z008[lv1]).real**2+(z008[lv1+1]-z008[lv1]).imag**2)**0.5

lift004 = (-1.j*rho/2*np.trapezoid(velFuncAOA(z004[midpointind:], U_inf, a004, m004, aoa)**2, cumLen004)).imag
lift008 = (-1.j*rho/2*np.trapezoid(velFuncAOA(z008[midpointind:], U_inf, a008, m008, aoa)**2, cumLen008)).imag

print(lift004, lift008)
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

Contour = ax.contour(xx, yy, Fzet008.imag, 30, cmap='plasma')
ax.grid(True)

fig4, axs = plt.subplots(1, 2)

#print(np.where(Fzet008==0.0))
np.savetxt("ComplexPotential.csv", Fzet008.imag, delimiter=",")

axs[0].contour(xx, yy, Fzet004_AOA4.imag, 200, colors='blue', linewidths=0.5)
axs[0].plot(z004.real, z004.imag,color='black',linewidth=2)
axs[1].contour(xx, yy, Fzet008_AOA4.imag, 200, colors='blue', linewidths=0.5)
axs[1].plot(z008.real, z008.imag,color='black',linewidth=2)

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
