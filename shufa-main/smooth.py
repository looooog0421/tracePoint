import numpy as np
import cv2 as cv
import math  # 计算幂函数的
from numpy.linalg import inv  # 求矩阵的逆的 inv



class PolyPoints:
    def __init__(self):
        self.fast = 0
        self.slow = 0
        self.point1 = []
        self.point2 = []
        self.d = 0
        self.t = np.array([0, 1, 2])

    def delRepeatPoint(self, raw_data):
        for i in range(raw_data.shape[0] - 1):
            self.point1 = raw_data[i]
            self.point2 = raw_data[i + 1]
            self.d = np.linalg.norm(self.point2 - self.point1)
            if self.d <= 1:
                raw_data[i+1] = raw_data[i]
        while self.fast < raw_data.shape[0]:
            if not (raw_data[self.fast] == raw_data[self.slow]).all():
                self.slow = self.slow + 1
                raw_data[self.slow] = raw_data[self.fast]
            self.fast = self.fast + 1
        data = raw_data[:self.slow]
        return data

    def poly(self, data_part):
        x = data_part[:, 0]
        y = data_part[:, 1]
        B1 = x
        B2 = y
        A = np.array(self.Vandermonder(self.t)).reshape(len(self.t), len(self.t))
        X1 = np.dot(inv(A), B1)
        a1 = X1
        X2 = np.dot(inv(A), B2)
        a2 = X2

        x1 = np.linspace(0, self.t[-1], 2 * self.t.shape[0] - 1)
        y1 = []
        y2 = []
        for k in x1:
            y1.append(self.Pn(k, a1))
            y2.append(self.Pn(k, a2))

        return y1, y2

    def Vandermonder(self, t):
        temp = []
        for i in t:
            for j in range(len(t)):
                temp.append(math.pow(i, j))
        return temp

    def Pn(self, x, a):
        pn = 0.0
        i = 0
        for j in range(len(a)):
            pn += a[i] * math.pow(x, j)
            i += 1
        return pn

# def delRepeatPoint(data):
#     for i in range(data.shape[0] - 1):
#         point1 = data[i]
#         point2 = data[i + 1]
#         d = np.linalg.norm(point2 - point1)
#         if d <= 1:
#             data[i + 1] = data[i]
#
#     while fast < data.shape[0]:
#         if not (data[fast] == data[slow]).all():
#             slow = slow + 1
#             data[slow] = data[fast]
#         fast = fast + 1
#     unique_data = data[:slow]
#     return slow, unique_data
#
#
# def poly(data_part):
#     t = np.array([0, 1, 2])
#     x = data_part[:, 0]
#     y = data_part[:, 1]
#
#     def Vandermonder(x):
#         temp = []
#         for i in x:
#             for j in range(len(x)):
#                 temp.append(math.pow(i, j))
#         return temp
#
#     def Pn(x, a):
#         pn = 0.0
#         i = 0
#         for j in range(len(a)):
#             pn += a[i] * math.pow(x, j)
#             i += 1
#         return pn
#
#     B1 = x
#     B2 = y
#     A = np.array(Vandermonder(t)).reshape(len(t), len(t))
#     X1 = np.dot(inv(A), B1)
#     a1 = X1
#     X2 = np.dot(inv(A), B2)
#     a2 = X2
#
#     x1 = np.linspace(0, t[-1], 2 * t.shape[0] - 1)
#     y1 = []
#     y2 = []
#     for k in x1:
#         y1.append(Pn(k, a1))
#         y2.append(Pn(k, a2))
#
#     return y1, y2

if __name__ == '__main__':

    data = np.loadtxt("bihua_data/spiral930points.txt").reshape(-1, 2)
    # print(data)
    polyPoints1 = PolyPoints()
    [row, unique_data] = polyPoints1.delRepeatPoint(data)
    # print(unique_data)
    print(row)
    poly_data = []
    times = (unique_data.shape[0] - 1) // 2
    print(times)
    for i in range(times):
        data_part = unique_data[i * 2: i * 2 + 3]
        # print(unique_data)
        new_x, new_y = polyPoints1.poly(data_part)
        new_data = np.transpose([new_x, new_y])
        # print(new_data)
        poly_data.append(new_data)

    poly_data = np.array(poly_data).reshape(-1, 2)
    # poly_data = np.array(poly_data)
    # [row, poly_data] = delrepeatpoint(poly_data)
    print(poly_data.shape)
    # 绘图
    img = np.zeros((400, 400), np.uint8)
    for j in range(poly_data.shape[0]):
        cv.circle(img, (int(poly_data[j, 0]), int(poly_data[j, 1])), 1, 255)

    # for j in range(unique_data.shape[0]):
    #     cv.circle(img, (int(unique_data[j, 0]), int(unique_data[j, 1])), 1, 255)
    cv.imshow("img", img)
    cv.waitKey(0)
