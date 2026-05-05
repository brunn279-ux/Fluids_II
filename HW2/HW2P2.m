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

z0 = 0+a*i;

F = source(z,z0,Gam);

%plot(real(F1), imag(F1))


fig1 = figure;
contour(realVal, imagVal, imag(F), 500)
colormap(plasma)
grid on;
ax = gca;
ax.FontSize = 15;
xlabel('x',FontSize=12)
ylabel('y',FontSize=12)
saveas(fig1, 'p2stream', 'epsc')

fig2 = figure;
contour(realVal, imagVal, real(F), 500)
colormap(plasma)
grid on;
ax = gca;
ax.FontSize = 15;
xlabel('x',FontSize=12)
ylabel('y',FontSize=12)
saveas(fig2, 'p2pot', 'epsc')
function F = source(z, z0, Gam)
   F = z.^(3/2) - Gam.*i./2./pi.*(log(z.^(3/2)-z0)+log(z.^(3/2)+z0));
   %F = z.^(5/3)-i.*Gam./2./pi.*log(z-z0);
   %F = -i.*Gam./2./pi.*log(z.^(5/3)-z0);
   %F = z.^(5/3);
end
