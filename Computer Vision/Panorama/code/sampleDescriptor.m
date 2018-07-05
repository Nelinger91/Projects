function [desc] = sampleDescriptor(im,pos,descRad)
% The function receives an image 'im'. Nx2 array 'pos
% of features coords. and descRad, that describes the size of 
%the descriptor. and returns kxkxN matrix which is N descriptors.
    firstToThird = 2^(1-3);
    pos(:) =  firstToThird*(pos(:)-1)+1;
    [N,~] = size(pos);
    k = 1+(descRad*2);
    desc = zeros(k,k,N);
    for i =1:N
        x = pos(i,1);
        y = pos(i,2);
        vecX = x-descRad:1:x+descRad;
        vecY = y-descRad:1:y+descRad;
        [Xcoords, Ycoords] = meshgrid(vecX,vecY);
        desc(:,:,i) = interp2(im,Xcoords,Ycoords);
        d = desc(:,:,i);
        m = mean2(d);
        dCent = d-m;
        desc(:,:,i) = (dCent) / norm(dCent(:));
    end    
end

   