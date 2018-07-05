function [imBlend] = pyramidBlending(im1, im2, mask,...
    maxLevels, filterSizeIm, filterSizeMask)
% The function recieves two images to blend, a mask (all of the same size)
% and creates 2 laplacian pryamids from the image (with maxLevels, and 
% filter size) and another gaussian pryamid from the mask.
% then its creates a new lalpacian prymaid using those 3 pryamids 
% and creates a new blended image out of it.
mask = im2double(mask);
[L1,filterL1] = LaplacianPyramid(im1,maxLevels,filterSizeIm);
[L2,filterL2] = LaplacianPyramid(im2,maxLevels,filterSizeIm);
[gMask, filterMask] = GaussianPyramid(mask,maxLevels,filterSizeMask);
for k=1:maxLevels
    newL{k} = (gMask{k}.*L1{k}) + ((1-gMask{k}).*L2{k});
end
imBlend = LaplacianToImage(newL,filterL1, ones(1,k));
end

