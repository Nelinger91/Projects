function [panorama] = renderPanorama(im,H)
% rendering the panorama we made. using 'H' the homographies and 'im'
% m images that we use to create the panorama

%calculating the centers and corners after homgraphie
    m = max(size(im));
    coords = zeros(4*m,2);
    center = zeros(m,2);
    for i = 1:m
        [M,N] = size(im{i});
        corners = [1,1; 1,M; N,1; N,M];
        newCorners = applyHomography(corners,H{i});
        idx = ((i-1)*4)+1;
        coords(idx:idx+3,:) = newCorners;
        cen = [(N+1)/2,(M+1)/2];
        center(i,:) = applyHomography(cen,H{i});
    end
% max/min x/y's     
    maxX = ceil(max(coords(:,1)));
    maxY = ceil(max(coords(:,2)));
    minX = floor(min(coords(:,1)));
    minY = floor(min(coords(:,2)));
    xRange = minX:maxX;
    yRange = minY:maxY;
    [XPano,YPano] = meshgrid(xRange,yRange);    
    panorama = zeros([maxY-minY+1,maxX-minX+1]);
%calculating the range for each strips. range for the i'th strip will be
%strip(i):strip(i+1) in x range, and all the y range
    Centers = round(center(1:m,1));
    firstCenters = Centers(1:m-1);
    secondCenters = Centers(2:m);
    middleCenters = round( ((firstCenters+secondCenters)/2) - (minX) +1 );
    strip = [1;middleCenters;(maxX-minX+1)];
%calculating each strip using backwarp    
    for i = 1:m
        x = XPano(:,strip(i):strip(i+1));
        y = YPano(:,strip(i):strip(i+1));
        backwarp = applyHomography([x(:),y(:)],inv(H{i}));
        xBackwarp = reshape(backwarp(:,1),size(x));
        yBackwarp = reshape(backwarp(:,2),size(y));
        imNew = interp2(im{i},xBackwarp,yBackwarp);
        panorama(:,strip(i):strip(i+1)) = imNew;
    end    
end
