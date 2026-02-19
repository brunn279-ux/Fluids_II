function [] = helmholtz2D_green(lambda)
% plot free-space 2D Green's function for the Helmholtz operator with
% wavelength lambda
%
% Green's function G satisfies (\nabla^2 + k^2) G = \delta(y - x), where
% y is the observer and x is the source
%
% Joseph W. Nichols, 2024

k = 2*pi/lambda; % wavenumber
omega = k;       % temporal frequency (assuming c = 1)

[X,Y] = meshgrid(-4:.05:4, -4:.05:4);
R = sqrt(X.^2 + Y.^2);

%G = -1i/4*besselh(0,k*R);  % Green's function for 2D Helmholtz equation
G = log(R)/2*pi;

% Animate in time
for i1 = 1:100
    t = i1/100;
    pcolor(X,Y,real(G*exp(-1i*omega*t))); shading interp; colorbar;
    caxis([-1 1]*.1);
    axis equal;
    drawnow;
end

end
