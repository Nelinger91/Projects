function [fourierSignal] = DFT2(signal)
%A  function that receives a 2d matrix, and transforms it to Fourier space.
fourierSignal =DFT((DFT(signal))')';
end

