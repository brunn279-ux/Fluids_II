close all;
clear variables;
clc;


gridPts = 1000;

realVal = linspace(-5,5, gridPts);
imagVal = linspace(-5,5, gridPts);

[REALVAL, IMAGVAL] = meshgrid(realVal,imagVal);
z = REALVAL + 1*i*IMAGVAL;

Gam = 1.0;
a = 1;

the = 120;
alpha = the/2;

z0 = 2*a + 0*i;
F = source(z,z0,Gam);

%plot(real(F1), imag(F1))


fig1 = figure;
contour(realVal, imagVal, imag(F), 1500)
colormap(plasma)
grid on;
ax = gca;
ax.FontSize = 15;
xlabel('x',FontSize=12)
ylabel('y',FontSize=12)
saveas(fig1, 'p3stream', 'epsc')

fig2 = figure;
contour(realVal, imagVal, real(F), 1500)
colormap(plasma)
grid on;
ax = gca;
ax.FontSize = 15;
xlabel('x',FontSize=12)
ylabel('y',FontSize=12)
saveas(fig2, 'p3pot', 'epsc')
function F = source(z, z0, Gam)
   F = 1.5./z+z-Gam/2*pi.*log(z-z0);
end
