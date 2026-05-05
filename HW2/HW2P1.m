close all;
clear variables;
clc;


gridPts = 1000;

z0 = 0+0*i;
z1 = 1+0*i;
z2 = 0+1*i;
z3 = -1+0*i;
z4 = 0-1*i;

realVal = linspace(-5,5, gridPts);
imagVal = linspace(-5,5, gridPts);

[REALVAL, IMAGVAL] = meshgrid(realVal,imagVal);
z = REALVAL + 1*i*IMAGVAL;

Q = 1.0;


F1 = source(z,z1,Q);
F2 = source(z,z2,Q);
F3 = source(z,z3,Q);
F4 = source(z,z4,Q);

Ft = F1+F2+F3+F4;

%plot(real(F1), imag(F1))

fig1 = figure;
contour(realVal, imagVal, imag(Ft), 200)
colormap(plasma)
grid on;
ax = gca;
ax.FontSize = 15;
xlabel('x',FontSize=12)
ylabel('y',FontSize=12)
saveas(fig1, 'p1stream', 'epsc')

fig2 = figure;
contour(realVal, imagVal, real(Ft), 200)
colormap(plasma)
grid on;
ax = gca;
ax.FontSize = 15;
xlabel('x',FontSize=12)
ylabel('y',FontSize=12)
saveas(fig2, 'p1pot', 'epsc')



function F = source(z, z0, Q)
   F = Q/2/pi*log(z-z0);
end
