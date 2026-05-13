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

def thickVal(z):
    top = np.max(z.imag)
    bottom = np.min(z.imag)

    left = np.min(z.real)
    right = np.max(z.real)

    t = top-bottom
    l = right-left

    return t/l

def velFunc(z, U, a, m):
    t1 = U/2.*(1.-a/zetafz(z, m)**2)
    t2 = 1.+ np.sqrt(z+2.)/2./np.sqrt(z-2.)+np.sqrt(z-2.)/2./np.sqrt(z+2.)
    return t1*t2

def velFuncAOA(z, U, a, m, aoa):
    aoa = np.pi/180.*aoa

    Gamcw = 4*np.pi*U*np.sin(aoa)

    t1 = U*np.exp(-1.j*aoa)
    t2 = -U*np.exp(1.j*aoa)*a*a/zetafz(z,m)**2
    t3 = 1.j*Gamcw/2./np.pi/zetafz(z,m)

    t4 = 1./2.*(1.+np.sqrt(z+2.)/2./np.sqrt(z-2.)+np.sqrt(z-2.)/2./np.sqrt(z+2.))

    return (t1 + t2 + t3)*t4

def foilFlowAOA(zeta, U, a, aoa):
    #print(aoa)
    aoa = aoa*np.pi/180
    Gamcw = 4*np.pi*U*a*np.sin(aoa)
    #print(aoa)
    return U*(np.exp(-1j*aoa)*zeta+np.exp(1j*aoa)*a*a/zeta)+1.j*Gamcw/2/np.pi*np.log(zeta/a)

def thwaites(tanVel, cumLen, visc):

    theta = np.zeros(tanVel.shape)
    for lv1 in range(1, len(tanVel)):
        theta[lv1] = np.abs(((tanVel[lv1-1]**5+tanVel[lv1]**5)*(cumLen[lv1]-cumLen[lv1-1]))/2)
        theta[lv1] = 0.45*visc/tanVel[lv1]**6*theta[lv1]
        theta[lv1] = np.sqrt(theta[lv1])

    return theta

def prof(theta, tanVel, visc):

    lam = np.zeros(theta.shape)

    for lv1 in range(1, len(lam)):
        diff = (tanVel[lv1]-tanVel[lv1-1])/2
        lam[lv1] = theta[lv1]**2/visc*diff

    return lam


