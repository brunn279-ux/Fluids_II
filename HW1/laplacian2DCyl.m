function [] = laplacian2DCyl(N)
% Boundary Element Method (BEM) for plane-wave scattering from cylinder
%
% Joseph W. Nichols, 2024
  
%k = 2*pi/lambda;  % wavenumber

% circle
dth = 2*pi/N;
th = [dth/2:dth:2*pi-dth/2];
x = [cos(th); sin(th)];   % collocation points

n = -x;                   % normal vectors (pointing into the cylinder)
ds = dth*ones(N);         % panel sizes


% Boundary element matrices
A = zeros(N,N);
B = zeros(N,N);
for i2 = 1:N
    for i1 = 1:N
        if (i1 == i2)
            A(i1,i2) = -0.5;
            B(i1,i2) = 0.0;
        else
            r = x(:,i2) - x(:,i1);  % source - observer
            rmag = norm(r);
            r = r/rmag;
            %G    = -1i/4*besselh(0,k*rmag);
            %dGdr =  1i*k/4*besselh(1,k*rmag);
            G = log(rmag)/2*pi;
            dGdr = 1/2/rmag/pi;
            A(i1,i2) = ds(i2)*dot(r,n(:,i2))*dGdr;
            B(i1,i2) = ds(i2)*G;
        end
    end
end

%drhos0 = 1i*k*x(1,:)'.*exp(1i*k*x(1,:)');  % drho/dn of scattered wave on cyl surf
%drhos0 = 1./2./pi./x(1,:)'+x(1,:)'.*cos(th)';
%rhos0  = A\(B*drhos0);                     % where the magic happens
psi1 = -sin(th)';
dpsi = (A*psi1)\B;

part2 = figure;
subplot(211);
%hold on;
plot(th, psi1);
grid on;
xlim([0 6])
ylim([-1.5 1.5])
subplot(212);
%hold on;
plot(th,dpsi);
grid on;


% Visualize solution
[XX,YY] = meshgrid(-4:.05:4, -4:.05:4);
RR = sqrt(XX.^2+YY.^2);
TT = atan(YY./XX);
%rhos = 0*XX;

psi = 0*XX;

for i1 = 1:N  % loop over source panels

    Rx = x(1,i1) - XX;    % source - observer(s)
    Ry = x(2,i1) - YY;   
    rmag = sqrt(Rx.^2 + Ry.^2);
    Rx = Rx./rmag;
    Ry = Ry./rmag;
    %G    = -1i/4*besselh(0,k*rmag);
    %dGdr =  1i*k/4*besselh(1,k*rmag);            
    G = log(rmag)./2.*pi;
    dGdr = 1./2./rmag./pi;
    psi = psi + ds(i1)*(psi1(i1).*dGdr-G.*dpsi(i1));
    %rhos = rhos + ds(i1)*(rhos0(i1)*(Rx*n(1,i1) + Ry*n(2,i1)).*dGdr - drhos0(i1)*G);
end

%psi = psi + RR.*sin(TT);
psi = psi + YY;

part3 = figure;
contour(XX, YY, psi, 100);
pbaspect([1 1 1]);
%
%% incident wave
%rhoi = exp(1i*k*XX);
%
%% Animate solution in time
%for i1 = 1:100
%    pcolor(XX,YY,real((rhos)*exp(-1i*2*pi*i1/20))); 
%%    pcolor(XX,YY,real((rhoi + rhos)*exp(-1i*2*pi*i1/20))); 
%    shading interp; 
%    colorbar;
%    caxis([-1 1]);
%    axis equal;
%    drawnow;
%end

end
