close all;
clear variables

Nr = 100;
r_max = 10;

N = 100;
dth = 2*pi/N;
th = [dth/2:dth:2*pi-dth/2];

dr = (r_max-1)/(Nr-1);
[rTest thetaTest] = ndgrid(1:dr:r_max, 0:dth:2*pi-dth);
psi_polar = (rTest-1./rTest).*sin(thetaTest);
x = rTest.*cos(thetaTest);
y = rTest.*sin(thetaTest);
psiFun = @(x,y) y-(y./(x.^2+y.^2));
psiexact = psiFun(x,y);

part4 = figure;
hold on;
psiHandle = fcontour(psiFun,[-5 5 -5 5],LineWidth=1);
psiHandle.LevelList = linspace(-5,5,21);
colormap(nebula)
grid on
pbaspect([1 1 1]);
xlabel('x',Interpreter='latex',Fontsize=14)
ylabel('y',Interpreter='latex',Fontsize=14)
saveas(part4,'part4el','epsc')

