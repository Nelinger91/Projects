function [ hNorm ] = homNorm( h )
% Normalizing the homographies.
    hNorm = h/h(3,3);
end

