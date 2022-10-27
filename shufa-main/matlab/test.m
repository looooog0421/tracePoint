data = load("./bihua_data/alpha4.txt");

x = find(data <0);
data(x) = [];
data = reshape(data,2,length(data)/2);
data = data.';
% fprintf('%f',data);
[m,n] = size(data);
fprintf('%f,%f',m,n)
for i = 1:m 
    data(i,2) = 256 - data(i,2);
end
%x1 = find(A==(238,7))

[~,row]=ismember([58,121],data,'rows');
data1 = data(row:end,1:2);
figure(1);
x = data1(:,1);
y = data1(:,2);
plot(data1(:,1),data1(:,2),'b');

% p = polyfit(data1(:,1),data1(:,2),10);
% f = polyva l(p,data1(:,1));
%plot(data1(:,1),data1(:,2),n,f,'-');  

% xlabel('xlabel');
% ylabel('ylabel');
%scatter(data(:,1),data(:,2),'r');
%[~, ind] = min(data(:,1));
%data1 = data(1:ind,1:2);
%scatter(data1(:,1),data1(:,2));

% data2 = load("./bihua_data/alpha5.txt");
% x = find(data2 <0);
% data2(x) = [];
% data2 = reshape(data2,2,length(data2)/2);
% data2 = data2.';
% [m,n] = size(data2);
% for i = 1:m 
%     data2(i,2) = 400 - data2(i,2);
% end
% %x1 = find(A==(238,7))
% 
% xlabel('xlabel');
% ylabel('ylabel');
% scatter(data2(:,1),data2(:,2),'b');
