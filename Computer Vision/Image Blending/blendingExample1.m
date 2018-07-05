%bibi and dog are 2 RGB photos that will be blended using 
%the function we built. we do the opration 3 times, once for each dimension
%1-R,2-G,3-B and then we combine them together to get the new blended
%image!
dog = im2double(imread('dog.jpg'));
bibi = im2double(imread('bib.jpg'));
mask = im2double(imread('mask.jpg'));
[row,col,dim] = size(dog);
mask = mask(:,:,1);
bibiR = bibi(:,:,1);
bibiG = bibi(:,:,2);
bibiB = bibi(:,:,3);
dogR = dog(:,:,1);
dogG = dog(:,:,2);
dogB = dog(:,:,3);
im = zeros(row,col,dim);
im(:,:,1) = pyramidBlending(bibiR,dogR,mask,3,3,51);
im(:,:,2) = pyramidBlending(bibiG,dogG,mask,3,3,51);
im(:,:,3) = pyramidBlending(bibiB,dogB,mask,3,3,51);
imshow(bibi); figure
imshow(dog); figure
imshow(mask);figure
imshow(im);figure