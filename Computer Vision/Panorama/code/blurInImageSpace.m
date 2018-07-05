function [blurImage] = blurInImageSpace(inImage,kernelSize)
%A function receiving an Image, and a size: describing the 
%width and length of the gaussian kernel. it calculate the gaussian kernel,
%and convolutes the Image with it, in order to receive a blurred image.
kernelIm = zeros(kernelSize,kernelSize);
base = [1,1];
x = 1;
%Creating to first row of the Kernel
for i=1:kernelSize-1;
   x = conv(x,base);
end
firstRow = x;
%Using the first row to kernel to calculate the entire 2d kernel.
for i=1:kernelSize
   kernelIm(i,:) = firstRow * firstRow(1,i); 
end    
% normalizing the kernel
normalFactor = sum(kernelIm);
normalFactor = sum(normalFactor);
division = 1/normalFactor;
kernelIm = division*(kernelIm);
%using conv2 to convulate between inImage and the gaussian kernel.
blurImage = conv2(inImage, kernelIm,'same');
end

