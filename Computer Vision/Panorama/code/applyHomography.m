function pos2 = applyHomography(pos1,H12)
% the function recieves coordinats as 'pos1' and transforms it using
% homography H12.
    pos2 = zeros(size(pos1));
    pos1 = [pos1,ones(size(pos1,1),1)]';
    tempPos = H12 * pos1;
    pos2(:,1) = tempPos(1,:)./tempPos(3,:);
    pos2(:,2) = tempPos(2,:)./tempPos(3,:);
end

