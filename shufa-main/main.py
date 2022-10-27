#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import poly
import cv2 as cv
import os
# import matplotlib.pyplot as plt

if __name__ == '__main__':
    fileFolder = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(fileFolder, 'bihua_data')
    PolyPoints1 = poly.PolyPoints()
    spiral_data1 = np.loadtxt(os.path.join(file, 'morecircle.txt')).reshape(-1, 2)
    # spiral_data1 = PolyPoints1.delRepeatPoint(spiral_data1)
    poly_spiral_data1 = PolyPoints1.poly(spiral_data1)
    print(poly_spiral_data1.shape)
    
    morecircle_line = PolyPoints1.SED(poly_spiral_data1)

    #这段代码是用于生成轨迹首尾相接直线的数据点集,直线上的点数等于轨迹点数
    img = np.zeros((400, 400), np.uint8)
    for j in range(spiral_data1.shape[0]):
        cv.circle(img, (int(spiral_data1[j, 0]), int(spiral_data1[j, 1])), 1, 255)
    
    for j in range(morecircle_line.shape[0]):
        cv.circle(img, (int(morecircle_line[j, 0]), int(morecircle_line[j, 1])), 1, 255)
    # for j in range(unique_data.shape[0]):
    #     cv.circle(img, (int(unique_data[j, 0]), int(unique_data[j, 1])), 1, 255)
    cv.imshow("img", img)
    cv.waitKey(0)

    # 这段代码是用于输出多个轨迹的合成(平均轨迹)的数据和图像
    # row = np.min([poly_spiral_data1.shape[0],
    #               poly_spiral_data2.shape[0],
    #               # poly_spiral_data3.shape[0],
    #               # poly_spiral_data4.shape[0],
    #               poly_spiral_data5.shape[0],
    #               poly_spiral_data6.shape[0]])
    # print(row)
    # add_points = (poly_spiral_data1[:row, :2]
    #               + poly_spiral_data2[:row, :2]
    #               + poly_spiral_data3[:row, :2]
    #               # + poly_spiral_data4[:row, :2]
    #               + poly_spiral_data5[:row, :2]
    #               + poly_spiral_data6[:row, :2]) / 5
    # img = np.zeros((400, 400), np.uint8)
    # print(add_points.shape)
    # finalLine = poly.PolyPoints()
    # final_line = finalLine.SED(add_points)
    
    # for j in range(add_points.shape[0]):
    #     cv.circle(img, (int(add_points[j, 0]), int(add_points[j, 1])), 1, 255)
    
    # for j in range(final_line.shape[0]):
    #     cv.circle(img, (int(final_line[j, 0]), int(final_line[j, 1])), 1, 255)
    # # for j in range(unique_data.shape[0]):
    # #     cv.circle(img, (int(unique_data[j, 0]), int(unique_data[j, 1])), 1, 255)
    # cv.imshow("img", img)
    # cv.waitKey(0)

    np.savetxt(os.path.join(file, 'morecircle_line.txt'), spiral_data1)
    np.savetxt(os.path.join(file, 'morecircle_trace.txt'), morecircle_line)


