function displayMatches(im1,im2,pos1,pos2,inliers)
% the function shows the good matches we found in yellow lines. bad matches
% in blue line. and showing each position of a feature point as a red dot.
        image = [im1,im2];
        imshow(image);hold on
        [N,M] = size(im1);
        [sPX,sPY] = size(pos1);
        x = pos1(:,1);
        x2 = pos2(:,1) + M;
        y = pos1(:,2);
        y2 = pos2(:,2);
        %showing the matches as red dots.
        plot(x,y,'r.');
        plot(x2,y2,'r.');
        [sInlier,~] = size(inliers);
        
        %showing outliers matches between the images as yellow lines
        for i = 1:sPX
            x = [pos1(i,1),pos2(i,1) + M];
            y = [pos1(i,2),pos2(i,2)];
            plot(x,y,'b-');
        end
        
        %showing inliers matches between the images as yellow lines
        for i = 1:sInlier
            x = [pos1(inliers(i),1),pos2(inliers(i),1)+M];
            y = [pos1(inliers(i),2),pos2(inliers(i),2)];
            plot(x,y,'y-');
        end
        hold off;
    end
    
