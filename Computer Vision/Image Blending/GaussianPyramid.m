function [pyr, filter] = GaussianPyramid(im, maxLevels, filterSize)
%the function creates a gaussian image with "maxLevels" levels and 
%blurs the levels with gaussian filter of size "filterSize"

%creates the filter
    convWith =[1,1];
    filter = 1;
    for i=1:filterSize-1;
        filter = conv(filter,convWith);
    end
    filter = filter/(4.^floor(filterSize/2));
%each level is equal to Reduce of last level.
    i = 1;
    pyr{1} = im;
    [row, col] = size(im);
    while (i ~= maxLevels && row/2 >= 16 && col/2 >= 16) 
        pyr{i+1} = Reduce(pyr{i},filter);
        i = i+1;
        [row,col] = size(pyr{i});
    end
%returns a cell array with 1 columns and "maxLevels" rows    
    pyr = pyr';
end

