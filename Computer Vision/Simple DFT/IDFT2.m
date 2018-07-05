function [signal] = IDFT2(fourierSignal)
%A function that receives a 2d matrix in Fourier space, and transforms
%it back.
signal =IDFT(IDFT(fourierSignal)');
signal = signal';
end

