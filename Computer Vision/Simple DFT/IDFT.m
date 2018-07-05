function [signal] = IDFT(fourierSignal)
%A function that receives a 1d vector in the Fourier space,
%and transform it back.
[row, N] = size(fourierSignal);
x = 0:N-1;
u = 0:N-1;
secondPart = (exp(2*pi*1i*u'*x/N))';
signal = (1/N)*(fourierSignal*secondPart);
signal = real(signal);
end

