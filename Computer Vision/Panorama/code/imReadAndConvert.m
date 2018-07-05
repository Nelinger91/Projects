function im = imReadAndConvert(filename, represntation)
% This function will recieve a filename and represntation:
% A number, 1 represnting grayscale, and 2 represnting rgb.
% and will change the picture in the filename path accordingly.
    pic = imread(filename);
    s = size(pic);
    dimension = max(size(s));
    if (represntation == 1 && dimension == 3)
        gray = rgb2gray(pic);
        im = im2double(gray);
    else
        im = im2double(pic);
    end
end
       