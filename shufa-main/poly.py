from curses import raw
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

    def delNegOne(self,raw_data):    #用于去除数据中的-1,也可手动删除
        rowIndex = np.where((raw_data == (-1, -1)).all(axis=1))
        data = np.delete(raw_data,rowIndex,axis=0)

        return data

    def delRepeatPoint(self, raw_data):  #删除重复点

        raw_data = self.delNegOne(raw_data)

        for i in range(raw_data.shape[0] - 1):
            self.point1 = raw_data[i]
            self.point2 = raw_data[i + 1]
            self.d = np.linalg.norm(self.point2 - self.point1)
            if self.d <= 1:
                raw_data[i + 1] = raw_data[i]
        while self.fast < raw_data.shape[0]:
            if not (raw_data[self.fast] == raw_data[self.slow]).all():
                self.slow = self.slow + 1
                raw_data[self.slow] = raw_data[self.fast]
            self.fast = self.fast + 1
        unique_data = raw_data[:self.slow]
        return unique_data

    def poly(self, unique_data1):  #多项式插值

        unique_data = self.delRepeatPoint(unique_data1)

        poly_data = []
        times = (unique_data.shape[0] - 1) // 2
        for i in range(times):
            data_part = unique_data[i * 2: i * 2 + 3]
            new_x, new_y = self.poly_part(data_part)
            new_data = np.transpose([new_x, new_y])
            poly_data.append(new_data)

        poly_data = np.array(poly_data).reshape(-1, 2)
        img = np.zeros((400, 400), np.uint8)
        for j in range(poly_data.shape[0]):
            cv.circle(img, (int(poly_data[j, 0]), int(poly_data[j, 1])), 1, 255)

        # line_point = self.SED(poly_data)
        #
        # for index in range(line_point.shape[0]):
        #     cv.circle(img, (int(line_point[index, 0]), int(line_point[index, 1])), 1, 255)

        # print(int(line_point[-1, 0]))
        # for j in range(unique_data.shape[0]):
        #     cv.circle(img, (int(unique_data[j, 0]), int(unique_data[j, 1])), 1, 255)



        cv.imshow("img", img)
        cv.waitKey(0)

        return poly_data

    def poly_part(self, data_part):
        x = data_part[:, 0]
        y = data_part[:, 1]
        # AX = B
        B1 = x
        B2 = y
        A = np.array(self.Vandermonde()).reshape(len(self.t), len(self.t))
        X1 = np.dot(inv(A), B1)
        a1 = X1
        X2 = np.dot(inv(A), B2)
        a2 = X2

        x1 = np.linspace(0, self.t[-1], 2 * self.t.shape[0] - 1)
        x1 = np.linspace(0, self.t[-1], 2 * self.t.shape[0] - 1)
        y1 = []
        y2 = []
        for k in x1:
            y1.append(self.Pn(k, a1))
            y2.append(self.Pn(k, a2))

        return y1, y2

    def Vandermonde(self):
        temp = []
        for i in self.t:
            for j in range(len(self.t)):
                temp.append(math.pow(i, j))
        return temp

    def Pn(self, x, a):
        i = 0
        pn = 0.0
        for j in range(len(a)):
            pn += a[i] * math.pow(x, j)
            i += 1
        return pn

    def SED(self, data): #做轨迹首尾相连的直线,直线上点的数量等于轨迹点数
        start_point = data[0, :]
        end_point = data[-1, :]
        line_point = []
        point_length = [0]

        for i in range(data.shape[0] - 1):
            point1 = data[i]
            point2 = data[i + 1]
            length = np.linalg.norm(point1 - point2)
            point_length.append(length)

        total_length = sum(point_length)

        x_line = (end_point[0] - start_point[0])
        y_line = (end_point[1] - start_point[1])

        x = start_point[0]
        y = start_point[1]

        for k in range(data.shape[0]):
            delta_x = x_line * point_length[k]/total_length
            x = x + delta_x

            delta_y = y_line * point_length[k]/total_length
            y = y + delta_y

            line_point.append(x)
            line_point.append(y)

        line_point = np.array(line_point).reshape(-1, 2)

        return line_point

    # def forFinalData(self, final_data, filename):
    #
    #     final_line = self.SED(final_data)
    #     np.loadtxt()
    def lesspoint(self,raw_data):
        less_data = []
        self.fast = 0
        while self.fast < raw_data.shape[0]:
            if self.fast%2 != 0:
                less_data.append(raw_data[self.fast])
            self.fast += 1
        less_data = np.array(less_data).reshape(-1, 2)
        return less_data



if __name__ == '__main__':
    data1 = np.loadtxt("bihua_data/spiral930points.txt").reshape(-1, 2)
    PolyPoints1 = PolyPoints()
    unique_data = PolyPoints1.delRepeatPoint(data1)

