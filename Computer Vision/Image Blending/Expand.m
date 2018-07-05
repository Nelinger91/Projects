function [newIm] = Expand(im, filter)
%this function take and image and a filter.
%blurs it, and then expands it size by 2.
%because we add zero, we need to make the filter vector equal two
    filter = 2 * filter;
% add zeros to the each 2nd col    
    [row, col] = size(im);
    zeroArray = zeros(row,col);
    im = [im;zeroArray];
    im = reshape(im,[row,2*col]);
    im = (im)';
%manipluating the im till we have zeros every second row and col.    
    zeroArray2 = zeros(2*col, row);
    im = [im;zeroArray2];
    im =reshape(im,[2*col,2*row]);
    newIm = (im)';
%convlate the im with the filter. once with a row filter and once with
% a column filter.
    newIm = conv2(newIm,filter, 'same');
    newIm = conv2(newIm,(filter)','same');
end

