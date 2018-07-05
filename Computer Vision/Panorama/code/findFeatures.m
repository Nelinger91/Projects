function [pos,desc] = findFeatures(pyr)
% The function calculates the features and descriptors of an image
% (receiving a gaussian pyramid of the image) and returns it.
    n = 7;
    m = 7; 
    radius = 7;
    descRad = 7;
    pos = spreadOutCorners(pyr{1},n,m,radius);
    desc = sampleDescriptor(pyr{3},pos,descRad);
end

