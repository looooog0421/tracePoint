clc;
x0 = 45:0.1:230;
%%
%第一段曲线
p11 = fittedmodel1.p1;
p12 = fittedmodel1.p2;
p13 = fittedmodel1.p3;
p14 = fittedmodel1.p4;
p15 = fittedmodel1.p5;
p16 = fittedmodel1.p6;
p17 = fittedmodel1.p7;
p18 = fittedmodel1.p8;
p19 = fittedmodel1.p9;
p110 =fittedmodel1.p10;
y11 = p11*x0.^9 + p12*x0.^8 + p13*x0.^7 + p14*x0.^6 + p15*x0.^5 + p16*x0.^4 + p17*x0.^3 + p18*x0.^2 + p19*x0 + p110;
disp(p11);
%%
%第二段曲线
p21 = fittedmodel2.p1;
p22 = fittedmodel2.p2;
p23 = fittedmodel2.p3;
p24 = fittedmodel2.p4;
p25 = fittedmodel2.p5;
p26 = fittedmodel2.p6;
p27 = fittedmodel2.p7;
p28 = fittedmodel2.p8;
p29 = fittedmodel2.p9;
p210 =fittedmodel2.p10;
y22 = p21*x0.^9 + p22*x0.^8 + p23*x0.^7 + p24*x0.^6 + p25*x0.^5 + p26*x0.^4 + p27*x0.^3 + p28*x0.^2 + p29*x0 + p210;
%%
d = y11-y22;
ix = find(d >-0.4 & d <0.4);
x1=55;
% disp(x1);
x0 = x1(1):0.1:181;
y11 = p11*x0.^9 + p12*x0.^8 + p13*x0.^7 + p14*x0.^6 + p15*x0.^5 + p16*x0.^4 + p17*x0.^3 + p18*x0.^2 + p19*x0 + p110;
plot(x0,y11);hold on;
x0 = x1(1):0.1:230;
y22 = p21*x0.^9 + p22*x0.^8 + p23*x0.^7 + p24*x0.^6 + p25*x0.^5 + p26*x0.^4 + p27*x0.^3 + p28*x0.^2 + p29*x0 + p210;
x222 = x0(1:1100);
y222 = y22(1:1100);
plot(x0,y22);