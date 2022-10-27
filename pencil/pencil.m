clc
close all
clear
name ='E:\study\pencil\alpha1_1000.jpg' ; 
dataname = find_track( name , 1 );

function dataname = find_track( name , show  )
im = rgb2gray(imread(name) );

im = imadjust(im,[0.5,0.6],[0,1]) ; % 【0,0.6】参数可调，根据拍摄质量自主调节，调整灰度值
 %imshow(im);hold on
im1 = imbinarize( im , 0.5 ) ; 
im1 = imcomplement(im1);
%im2 = imfill(~im1,'holes') ; 
im2 = im1;
se = strel('disk',5);
im3 = imclose(im2,se) ; 
se = strel('disk',10);
im3 = imclose(im3,se) ; 
im3 = bwareaopen (im3,10000)  ; 
% 以上为图像预处理
im4 = bwmorph(im3,'skel',Inf);
im4 = bwmorph(im4,'spur',150); %提取骨架，并删除小分叉
[x,y] = find(im4) ; % 提取骨架点
if show
    figure 
    imshow(im3) ; hold on 
    plot(y,x,'r.'); hold on 
    pause
end
%寻找端点
k = 1 ; 
for i = 1 : size(x,1)
    ss = sum(sum(im4(x(i)-1:x(i)+1 , y(i)-1:y(i)+1 )));
    if ss < 3 % 骨架点邻域值的和为2时，该点为端点
        m(k) = i ; 
        k = k + 1 ; 
    end
end
x1 = x ; y1 = y ; 
g = [x(m(1)),y(m(1))] ; 
x1(m(1)) = [] ; 
y1(m(1)) = [] ; 
if show
    figure 
    imshow(im) ; hold on 
    h1 = plot(y(m),x(m),'r.'); hold on 
    h2 = quiver(1,1,1,1,100,'color','r'); hold on 
end
while 1 % 轨迹点连线
    d = sqrt( (x1 - g(end,1)).^2 + (y1 - g(end,2)).^2 ) ; 
    b = find(d == min(d)) ; 
    g = [g;  [x1(b(1)),y1(b(1))] ] ; 
    x1(b) = [] ; 
    y1(b) = [] ;
    if show
        set(h1 , 'Xdata',g(:,2),'Ydata',g(:,1)) ; pause(0.000001)
    end
    if isempty(x1) | isempty(b)
        break
    end
end


dataname = name ; 
dataname(end-2:end) = 'xls' ;
dataname = strcat(dataname , 'x') ; 
xlswrite(dataname ,g)

end