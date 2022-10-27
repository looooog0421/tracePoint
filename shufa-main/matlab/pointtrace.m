clc;
% clear all;
data5 = load("./bihua_data/unique_data.txt");
[m,data5] = pointshow(data5);
[x1,y1,x2,y2]=fittingpoint(data);

function [m,data] = pointshow(data)
    negone = find( data<0 );
    data(negone) = [];  %由于提取轨迹坐标点函数中参杂（-1，-1），，为避免影响绘图，此处将这些点删去
    data = reshape(data,2,length(data)/2);
    data = data.';  %将数据转换为n*2的矩阵，每一行为一个坐标点
    [m,~] = size(data);
    for i = 1:m 
        data(i,2) = 256 - data(i,2);
    end
	scatter(data(:,1),data(:,2));
    disp(data);
end

function [x1,y1,x2,y2]=fittingpoint(data)
    midpoint = [57,135];
    [~,row]=ismember(midpoint,data,'rows');
    data1 = data(1:row,1:2);
%     fprintf('data1=%f',data1);
    x1 = data1(:,1);
    y1 = data1(:,2);
%     fitresult1 = fit(x1, y1, 'smoothingspline', 'SmoothingParam', 1);
%     fitresult1 = fit(x1, y1, 'poly9');
%     plot(fitresult1,x1,y1);hold on;
%     plot(fitresult1);hold on;
    data2 = data(row:end,1:2);
    x2 = data2(:,1);
    y2 = data2(:,2)
%     fitresult2 = fit(x2, y2, 'smoothingspline', 'SmoothingParam', 1);
%     fitresult2 = fit(x2, y2, 'poly9');
%     plot(fitresult2,x2,y2);
%     plot(fitresult2);
end