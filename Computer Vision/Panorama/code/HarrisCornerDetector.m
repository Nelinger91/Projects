function [pos] = HarrisCornerDetector( im )
% A function receiving an image and finding the feature points of the
% image.
    filterWith = [1,0,-1];
    %derivatives 
    Ix = conv2(im, filterWith,'same');
    Iy = conv2(im, (filterWith)','same');
    %blurring
    IxSq = blurInImageSpace(Ix.*Ix,3);
    IySq = blurInImageSpace(Iy.*Iy,3);
    IxIy = blurInImageSpace(Ix.*Iy,3);
    %calculateing det and trace for derivatives for each value
    det = (IxSq).*(IySq) - (IxIy).*(IxIy);
    k = 0.04;
    trace = (IxSq)+(IySq);
    R = det - k*(trace.^2);
    responseThresh = nonMaximumSuppression(R);
    [col,row] = ind2sub(size(responseThresh),find(responseThresh));
    pos = [row,col];
end

