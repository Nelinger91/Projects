function [Htot] = accumulateHomographies(Hpair,m)
% the function calculates an homographies to a certain image in location
% 'm' using the set of homographies from im i to im i+1
    numOfTrans = max(size(Hpair))+1;
    
%homographie for the m matrix is identity matrix.    
    Htot{m}=eye(3);
%accumlate homographies for homgraphies smaller then m    
    for i = (m-1):(-1):1
        Htot{i} = homNorm(Htot{i+1} * Hpair{i});
    end
%accumlate homographies for homgraphies bigger then m        
    for i = (m+1):1:(numOfTrans)
        Htot{i} = homNorm(Htot{i-1} / (Hpair{i-1}));
    end
end

