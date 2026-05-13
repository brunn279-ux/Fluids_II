from colorspacious import cspace_converter
import numpy as np
import matplotlib.pyplot as plt
import math

from funcScript import *

x = np.linspace(-3, 3, 1001)
y = np.linspace(-3, 3, 1001)

xx, yy = np.meshgrid(x,y)

zz = xx + 1j*yy

theta = np.linspace(0,2*np.pi, 500)

midpoint = np.pi

midpointind = find_nearest(theta, midpoint)
print(midpointind)

m004 = 0.03181286228622863
m008 = 2.065*0.03181286228622863

m004_book = 0.04/1.3
m008_book = 0.08/1.3

a004 = 1.0 + m004
a008 = 1.0 + m008

U_inf = 1.0

visc = 0.001

zetzet = zetafz(zz, m008)
Fzet = cylFlow(zetzet, U_inf, a008, m008)

Zout = compZ(Fzet)

zeta004 = compZeta(a004,m004,theta)
z004 = compZ(zeta004)

zeta008 = compZeta(a008,m008,theta)
z008 = compZ(zeta008)

cumLen004 = np.zeros(midpointind)
cumLen008 = np.zeros(midpointind)

norms004 = np.zeros(midpointind, dtype=complex)
norms008 = np.zeros(midpointind, dtype=complex)

#fig, axs = plt.subplots(1,2)

for lv1 in range(midpointind-1):
    backlv1 = midpoint-lv1 #sort this out because right now I think cumlen is backwards
    cumLen004[lv1+1] = cumLen004[lv1]+((z004[lv1+1]-z004[lv1]).real**2+(z004[lv1+1]-z004[lv1]).imag**2)**0.5
    cumLen008[lv1+1] = cumLen008[lv1]+((z008[lv1+1]-z008[lv1]).real**2+(z008[lv1+1]-z008[lv1]).imag**2)**0.5
#    axs[0].plot([z004[lv1].real, z004[lv1+1].real],[z004[lv1].imag, z004[lv1+1].imag])
#    axs[0].plot([norms004[lv1].real, norms004[lv1+1].real],[norms004[lv1].imag, norms004[lv1+1].imag])
#
#    axs[1].plot([z008[lv1].real, z008[lv1+1].real],[z008[lv1].imag, z008[lv1+1].imag])
#    axs[1].plot([norms008[lv1].real, norms008[lv1+1].real],[norms008[lv1].imag, norms008[lv1+1].imag])
#    #plt.show()
#    plt.draw()
#    plt.pause(0.1)
#
#    print(cumLen004[lv1], '\n', cumLen008[lv1], '\n', lv1)


print(cumLen004.shape)
tanVel004 = velFunc(z004[:midpointind], U_inf, a004, m004)
tanVel008 = velFunc(z008[:midpointind], U_inf, a008, m008)

#print(tanVel004.shape)

theta004 = thwaites(tanVel004, cumLen004, visc)
theta008 = thwaites(tanVel008, cumLen008, visc)

lam004 = prof(theta004, tanVel004, visc)
lam008 = prof(theta008, tanVel008, visc)

#print(theta004.shape)

#    norms004[lv1] = 1j*(z004[lv1+1]-z004[lv1])+z004[lv1]
#    norms008[lv1] = 1j*(z008[lv1+1]-z008[lv1])+z008[lv1]
#
#norms004[-1] = (-(z004[1]-z004[0]).imag+1.j*(z004[1]-z004[0]).real)+z004[0]
#norms008[-1] = (-(z008[1]-z008[0]).imag+1.j*(z008[1]-z008[0]).real)+z008[0]

ratio004 = thickVal(z004)
ratio008 = thickVal(z008)

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

fig4, axs = plt.subplots(1,2)

axs[0].plot(cumLen004, np.abs(tanVel004[::-1]))
#axs[0].set_aspect('equal', adjustable='datalim')
axs[1].plot(cumLen008, np.abs(tanVel008[::-1]))
#axs[1].set_aspect('equal', adjustable='datalim')


axs[0].grid(True)
axs[1].grid(True)

fig5, axs = plt.subplots(1,2)

axs[0].plot(cumLen004, theta004[::-1])
#axs[0].set_aspect('equal', adjustable='datalim')
axs[1].plot(cumLen008, theta008[::-1])
#axs[1].set_aspect('equal', adjustable='datalim')


axs[0].grid(True)
axs[1].grid(True)

fig6, axs = plt.subplots(1,2)

axs[0].plot(cumLen004, lam004[::-1])
#axs[0].set_aspect('equal', adjustable='datalim')
axs[1].plot(cumLen008, lam008[::-1])
#axs[1].set_aspect('equal', adjustable='datalim')


axs[0].grid(True)
axs[1].grid(True)


#for lv1 in range(norms004.size-1):
#    axs[0].plot([z004[lv1].real, z004[lv1+1].real],[z004[lv1].imag, z004[lv1+1].imag])
#    axs[0].plot([norms004[lv1].real, norms004[lv1+1].real],[norms004[lv1].imag, norms004[lv1+1].imag])
#
#    axs[1].plot([z008[lv1].real, z008[lv1+1].real],[z008[lv1].imag, z008[lv1+1].imag])
#    axs[1].plot([norms008[lv1].real, norms008[lv1+1].real],[norms008[lv1].imag, norms008[lv1+1].imag])
#    #plt.show()
#    plt.draw()
#    plt.pause(0.1)
#
#
#axs[0].grid(True)
#axs[1].grid(True)
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
