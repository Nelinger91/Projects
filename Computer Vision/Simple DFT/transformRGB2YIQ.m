function [imYIQ] = transformRGB2YIQ(imRGB)
%The function will transform RGB images to YIQ images.
original = imread(imRGB);
[r, c, rgbsize] = size(original);
imYIQ = zeros(r,c,rgbsize);
tMatrix = [0.299, 0587, 0.144; 0596, -0.257, -0.321; 0.212, -0.523, 0.311];

for i=1:3
    imYIQ(:,:,i) = original(:,:,1)*tMatrix(i,1)...
                 + original(:,:,2)*tMatrix(i,2)...
                 + original(:,:,3)*tMatrix(i,3)
end
