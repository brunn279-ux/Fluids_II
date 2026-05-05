import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

eta1, f1, fp1, fpp1 = np.loadtxt('data2.csv', delimiter=',',skiprows=1, unpack=True)
eta2, f2, fp2, fpp2 = np.loadtxt('data1.csv', delimiter=',',skiprows=1, unpack=True)
eta3, f3, fp3, fpp3 = np.loadtxt('data3.csv', delimiter=',',skiprows=1, unpack=True)

etas = np.linspace(0, 1, num=1000)
fpara = 2*etas-etas*etas
fo3a = 1.5*etas-0.5*etas*etas*etas
fo3b = 3*etas-3*etas*etas+etas*etas*etas

fig1, axs = plt.subplots(1, 3, figsize=(15,5.4))

axs[0].plot(eta1, fp1,label=r'$f(\eta)$')
axs[0].plot((eta1[0], eta1[-1]), (fp1[-1], fp1[-1]), label=rf"$f'(10) = {fp1[-1]}$", linestyle=':',linewidth=2)
axs[1].plot(eta2, fp2,label=r'$f(\eta)$')
axs[1].plot((eta2[0], eta2[-1]), (fp2[-1], fp2[-1]), label=rf"$f'(10) = {fp2[-1]}$", linestyle=':',linewidth=2)
axs[2].plot(eta3, fp3,label=r'$f(\eta)$')
axs[2].plot((eta3[0], eta3[-1]), (fp3[-1], fp3[-1]), label=rf"$f'(10) = {fp3[-1]}$", linestyle=':',linewidth=2)

axs[0].grid(True)
axs[1].grid(True)
axs[2].grid(True)

axs[0].legend(fontsize=13)
axs[1].legend(fontsize=13)
axs[2].legend(fontsize=13)

axs[0].set_title(r"$\Delta\eta=0.1$, $f''(0)=0.2$")
axs[0].set_xlabel(r'$\eta$',fontsize=16)
axs[0].set_ylabel('$f\'$',fontsize=16)
axs[0].tick_params(axis='both', labelsize=14)
axs[1].set_title(r"$\Delta\eta=0.1$, $f''(0)=0.3155$")
axs[1].set_xlabel(r'$\eta$',fontsize=16)
axs[1].set_ylabel('$f\'$',fontsize=16)
axs[1].tick_params(axis='both', labelsize=14)
axs[2].set_title(r"$\Delta\eta=0.01$, $f''(0)=0.3305$")
axs[2].set_xlabel(r'$\eta$',fontsize=16)
axs[2].set_ylabel('$f\'$',fontsize=16)
axs[2].tick_params(axis='both', labelsize=14)

#plt.show()
plt.savefig("/Users/abbieb/Documents/School/Grad/Spring2026/Fluids_II/HW3/Figures/problem2.pdf")


fig2, ax = plt.subplots(figsize=(5,5))
ax.plot(etas, fpara, label='2nd Order')
ax.plot(etas, fo3a, label='3rd Order Wall')
ax.plot(etas, fo3b, label='3rd Order Free')
ax.plot(eta3[0:int(eta3.size/2)]/5, fp3[0:int(eta3.size/2)], label='Numeric')
ax.grid(True)
ax.legend(fontsize=13)
ax.set_xlabel(r'$\eta$',fontsize=16)
ax.set_ylabel('$f\'$',fontsize=16)
axs[2].tick_params(axis='both', labelsize=14)

#plt.show()
plt.savefig("/Users/abbieb/Documents/School/Grad/Spring2026/Fluids_II/HW3/Figures/problem3.pdf")
