function [strechedIm] = linearStretch(im)
%the function gets an image, and does a linear stretch between 0 and 1
    minPix = min(min(im));
    maxPix = max(max(im));
    a = 1/(maxPix-minPix);
    b = -a * minPix;
    strechedIm = a .* im +b; 
end