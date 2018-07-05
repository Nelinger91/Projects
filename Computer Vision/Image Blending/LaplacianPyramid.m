function [pyr, filter] = LaplacianPyramid(im, maxLevels, filterSize)
%the function creates a laplacian image with "maxLevels" levels and 
%blurs the levels with gaussian filter of size "filterSize"

%creates the filter
    convWith =[1,1];
    filter = 1;
    for i=1:filterSize-1;
        filter = conv(filter,convWith);
    end
    filter = filter/(4.^floor(filterSize/2));
% each level is l(i) = g(i) - Expand(g(i-1))
    pyr{1} = im - Expand(Reduce(im, filter), filter);
    i = 2;
    [row, col] = size(pyr{1});
    while (i ~= (maxLevels) && row/4 >= 16 && col/4 >= 16) 
        im = Reduce(im,filter);
        pyr{i} = Reduce(pyr{i-1},filter) -...
            Expand(Reduce(Reduce(pyr{i-1},filter),filter),filter);
        row = row/2;
        i = i + 1;       
    end
    im = Reduce(im,filter);
%the last level equals to the gaussian last level.    
    pyr{i} = im;
%returns a cell array with 1 columns and "maxLevels" rows        
    pyr = pyr';
end

