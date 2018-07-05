%cars and clowns are 2 RGB photos that will be blended using 
%the function we built. we do the opration 3 times, once for each dimension
%1-R,2-G,3-B and then we combine them together to get the new blended
%image!
car = im2double(imread('car.jpg'));
clowns = im2double(imread('clowns.jpg'));
mask = im2double(imread('mask2.jpg'));
[row,col,dim] = size(dog);
mask = mask(:,:,1);
carR = car(:,:,1);
carG = car(:,:,2);
carB = car(:,:,3);
clownsR = clowns(:,:,1);
clownsG = clowns(:,:,2);
clownsB = clowns(:,:,3);
im = zeros(row,col,dim);
im(:,:,1) = pyramidBlending(carR,clownsR,mask,3,3,51);
im(:,:,2) = pyramidBlending(carG,clownsG,mask,3,3,51);
im(:,:,3) = pyramidBlending(carB,clownsB,mask,3,3,51);
imshow(car); figure
imshow(clowns); figure
imshow(mask);figure
imshow(im);figure