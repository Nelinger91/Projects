% My examples  
% First Example
numFrames = 2;
inpPathFormat = 'data/inp/mine/kitchen%d.jpg';
outPath = 'data/out/mine/kitchen.jpg';
renderAtFrame = ceil(numFrames/2);
generatePanorama(inpPathFormat,outPath,numFrames,renderAtFrame,true);
% Second Example
inpPathFormat = 'data/inp/mine/living%d.jpg';
outPath = 'data/out/mine/living.jpg';
generatePanorama(inpPathFormat,outPath,numFrames,renderAtFrame,true);
