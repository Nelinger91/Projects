function [ind1,ind2] = matchFeatures(desc1,desc2,minScore)
% checks for descriptors of 2 images which descriptor (represnting a
% feature point) in desc1 fits the descriptor in desc2. returns the
% indecies of the matches.
    [a,b,k] = size(desc1);
    [c,d,l] = size(desc2);
    desc1 = reshape(desc1,[a*b, k]);
    desc2 = reshape(desc2,[c*d, l]);
    desc1 = desc1';
    sumMatrix = desc1 * desc2;
    %finding the max index for rows and cols. each cell i,j represents
    %sum of multiplying (dot wise) the i'th descriptor of desc1 with the
    %j'th descriptor of desc2.
    [~,I] = max(sumMatrix);
    [~,J] = max(sumMatrix,[],2);
    [~,s] = size(I);
    ind1 = [];
    ind2 = [];
    %after finding max for each row and col, checking if the max of a row
    % is the max of a col.
    for i=1:s
        if J(I(1,i)) == i  
            ind1 = [ind1,I(i)];
            ind2 = [ind2,i];
        end
    end 
end
    
  