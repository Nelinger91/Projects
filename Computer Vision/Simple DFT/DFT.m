function [fourierSignal] = DFT(signal)
%A function that receives a 1d vector and 
%operates a Fourier transform on it
[row, col] = size(signal);
x= 0:col-1;
u = 0:col-1;
secondPart = (exp(-2*pi*1i*u'*x/col))';
fourierSignal = double(signal)*secondPart;
end
