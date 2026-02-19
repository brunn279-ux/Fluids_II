function [] = helmholtz2D_analytic(lambda)
% Series solution for acoustic planewave scattering from hard-walled cylinder
%
% Joseph W. Nichols, 2024
  
k = 2*pi/lambda; % wavenumber

[XX,YY] = meshgrid(-4:.05:4, -4:.05:4);
R = sqrt(XX.^2 + YY.^2);
TH = atan2(YY,XX);

% Compute rhos & drhos on surface (useful for debugging BEM)
% N = 200;
% dth = 2*pi/N;
% TH = [dth/2:dth:2*pi-dth/2];
% R = 0*TH+1;
% XX = cos(TH); 
% YY = sin(TH);


% SERIES solution (based on plane-wave expansion)

B = (besselj(-1,k) - besselj(1,k))/(besselh(-1,k) - besselh(1,k));
rhoi = besselj(0,k*R);
rhos = -B*besselh(0,k*R);

%drhoi = 0.5*k*(besselj(-1,k*R) - besselj(1,k*R));
%drhos = -0.5*k*B*(besselh(-1,k*R) - besselh(1,k*R));

for i1 = 1:200
    B = (besselj(i1-1,k) - besselj(i1+1,k))/(besselh(i1-1,k) - besselh(i1+1,k));    
    rhoi = rhoi + 2*1i^i1*besselj(i1,k*R).*cos(i1*TH); 
    rhos = rhos - 2*1i^i1*B*besselh(i1,k*R).*cos(i1*TH);

%    drhoi = drhoi + 1i^i1*k*(besselj(i1-1,k*R) - besselj(i1+1,k*R)).*cos(i1*TH); 
%    drhos = drhos - 1i^i1*k*B*(besselh(i1-1,k*R) - besselh(i1+1,k*R)).*cos(i1*TH);
end


% Animate solution
for i1 = 1:100
    pcolor(XX,YY,real(rhos*exp(-1i*2*pi*i1/20))); 
%    pcolor(XX,YY,real((rhoi+rhos)*exp(-1i*2*pi*i1/20))); 
    shading interp; colorbar;
    caxis([-1 1]);
    rectangle('Position',[-1 -1 2 2],'Curvature',[1 1],'FaceColor',[0.5 0.5 0.5]);
    axis equal;
    drawnow;
end

end
