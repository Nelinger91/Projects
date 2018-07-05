function [magnitude] = fourierDerivative( inImage )
%A function that receives an image, and derives it by
%transforming the image to Fourier space, multiply it with the weighted function,
%and returns it to the original vector space.
fourierImage = DFT2(inImage);
[row,col] = size(inImage);
%creating a matrix that her columns are 0:255, and multiplying by
%our DFT image, then getting it back to the image space
% both in x axis and in y axis
m = (0:(row-1))';
m =repmat(m,1,row);
xDerivative =  fourierImage * m ;
xDerivative = IDFT2(xDerivative);
xDerivative = (2*pi*1i/row) * xDerivative
n = (0:(col-1))';
n =repmat(n,1,col);
yDerivative = n * fourierImage ;
yDerivative = IDFT2(yDerivative);
yDerivative = yDerivative*(2*pi*1i/col)
%calculating the magnitude and shifting the image.
magnitude = sqrt(abs(xDerivative.^2)+abs(yDerivative.^2));
magnitude = fftshift(magnitude);
imshow(magnitude);
end

