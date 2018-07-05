function [newIm] = Reduce(im, filter)
%this function take and image and a filter.
%blurs it, and then reduces it size by 2.
    im = conv2(im,filter, 'same');
    im = conv2(im,(filter)','same');
    [row, col] = size(im);
    newIm = im(1:2:end,1:2:end);         

end

