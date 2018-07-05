function [] = displayPyramid(pyr,levels)
%The function uses renderPyramid to get a new image showing "levels" levels
%of the pyramid and displays it
    ren = renderPyramid(pyr, levels);
    imshow(ren);figure
end

