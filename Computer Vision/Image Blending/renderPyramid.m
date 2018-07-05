function [res] = renderPyramid(pyr,levels)
%the function receives a pyramid and number of levels
%and render the image so the first level will be to the left
%the next level will be aligned to upper edge to the right of the first 
%image and so on, till level "levels"
    [rowNum,colNum] = size(pyr{1});
% this is a loop    
    for i = 1:levels
        pyr{i} = linearStretch(pyr{i});
        [currRow, currCol] = size(pyr{i});
        im{i} = [pyr{i};zeros(rowNum - currRow,currCol)];
    end 
    res = cell2mat(im);
end

