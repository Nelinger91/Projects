function [img] = LaplacianToImage2(lpyr, filter, coeffMultVec)
% creates an image from a Laplacian pyramid
    [NOTUSED,len] = size(coeffMultVec);
    % multiply the coeff vec with each pyr level.
    for i=1:len
        newPyr{i} = lpyr{i} .* coeffMultVec(i);
    end
    % creates an image from the pryamid
    for i= 0:len-2
        addedIm = Expand(newPyr{len-i},filter);
        lpyr{len-i-1} = addedIm + lpyr{len-i-1};
    end
    img = lpyr{1} + Expand(lpyr{2},filter);
end

