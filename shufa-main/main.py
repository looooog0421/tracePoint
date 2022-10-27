import numpy as np
import poly
import cv2 as cv
# import matplotlib.pyplot as plt

if __name__ == '__main__':
    PolyPoints1 = poly.PolyPoints()
    spiral_data1 = np.loadtxt("bihua_data/spiral930points.txt").reshape(-1, 2)
    # spiral_data1 = PolyPoints1.delRepeatPoint(spiral_data1)
    poly_spiral_data1 = PolyPoints1.poly(spiral_data1)
    print(poly_spiral_data1.shape)

    PolyPoints2 = poly.PolyPoints()
    spiral_data2 = np.loadtxt("bihua_data/alpha5.txt").reshape(-1, 2)
    # spiral_data2 = PolyPoints2.delRepeatPoint(spiral_data2)
    poly_spiral_data2 = PolyPoints2.poly(spiral_data2)
    print(poly_spiral_data2.shape)

    # PolyPoints3 = poly.PolyPoints()
    # spiral_data3 = np.loadtxt("bihua_data/spiral1035points.txt").reshape(-1, 2)
    # # spiral_data3 = PolyPoints3.delRepeatPoint(spiral_data3)
    # poly_spiral_data3 = PolyPoints3.poly(spiral_data3)
    # print(poly_spiral_data3.shape)
    #
    # # PolyPoints4 = poly.PolyPoints()
    # # spiral_data4 = np.loadtxt("bihua_data/spiral1060points.txt").reshape(-1, 2)
    # # # spiral_data4 = PolyPoints4.delRepeatPoint(spiral_data4)
    # # poly_spiral_data4 = PolyPoints2.poly(spiral_data4)
    # # print(poly_spiral_data4.shape)
    #
    # PolyPoints5 = poly.PolyPoints()
    # spiral_data5 = np.loadtxt("bihua_data/spiral1020points.txt").reshape(-1, 2)
    # # spiral_data5 = PolyPoints5.delRepeatPoint(spiral_data5)
    # poly_spiral_data5 = PolyPoints5.poly(spiral_data5)
    # print(poly_spiral_data5.shape)
    #
    # PolyPoints6 = poly.PolyPoints()
    # spiral_data6 = np.loadtxt("./bihua_data/luoxuan9.txt").reshape(-1, 2)
    # # spiral_data6 = PolyPoints6.delRepeatPoint(spiral_data6)
    # poly_spiral_data6 = PolyPoints6.poly(spiral_data6)
    # print(poly_spiral_data6.shape)
    #
    # row = np.min([poly_spiral_data1.shape[0],
    #               poly_spiral_data2.shape[0],
    #               poly_spiral_data3.shape[0],
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
    #
    # for j in range(add_points.shape[0]):
    #     cv.circle(img, (int(add_points[j, 0]), int(add_points[j, 1])), 1, 255)
    #
    # for j in range(final_line.shape[0]):
    #     cv.circle(img, (int(final_line[j, 0]), int(final_line[j, 1])), 1, 255)
    # # for j in range(unique_data.shape[0]):
    # #     cv.circle(img, (int(unique_data[j, 0]), int(unique_data[j, 1])), 1, 255)
    # cv.imshow("img", img)
    # cv.waitKey(0)
    #
    #
    #
    # np.savetxt("bihua_data/final_line.txt", final_line)
    # np.savetxt("bihua_data/final_trace.txt", add_points)
