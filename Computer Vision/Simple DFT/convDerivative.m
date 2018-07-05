function [ magnitude ] = convDerivative( inImage )
%A function that receives an image, an derives it using convolution 
%with the vectors [1,0,-1] and [1;0;-1]
x = [1,0,-1];
xDerivative = conv2(double(inImage),double(x),'same');
y = x';
yDerivative = conv2(double(inImage),double(y),'same');
magnitude = sqrt(abs(xDerivative.^2)+abs(yDerivative.^2));
imshow(magnitude);
end

