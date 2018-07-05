function [H12,inliers] = ransacHomography(pos1,pos2,numIters,inlierTol)
% A random function. does 'numIters' iterations to discover what
% homography is the best describing the correlation between pos1 and pos2.
% returns the best homgraphy and the features point that are moving well
% using the homography (are less then the inlierTol)
    [N,~] = size(pos1);
    maxInlier = 0;
    for i = 1:numIters;
        % choosing 4 random matches and doing the operation on them.
        r = randi([1,N],1,4);
        p1 = pos1(r,:);
        p2 = pos2(r,:);
        H12 = leastSquaresHomography(p1,p2);
        if ~(isempty(H12))
            transPos1 = applyHomography(pos1,H12);
            E = sum((transPos1 - pos2).^2,2);
            inlierIdx = find(E < inlierTol);
            inlierCount = size(inlierIdx,1);
            %checking if this iteration created the most inliers
            % if so, updating the inliers list.
            if inlierCount > maxInlier
                inliers = inlierIdx;
                maxInlier = inlierCount;
            end    
        end    
    end   
    %calculating the homgraphy using the inliers only that we got from 
    %the best random sampling
    p1MaxIn = pos1(inliers,:);
    p2MaxIn = pos2(inliers,:);
    H12 = leastSquaresHomography(p1MaxIn,p2MaxIn);
end

