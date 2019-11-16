# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   编制行星数据分析 （主程序）
# ------------------------(max to 80 columns)-----------------------------------

import math

def cal_V(r):
    '输入行星半径，返回行星的体积'

    V = 4 / 3 * math.pi * r * r *r
    'V = 4 / 3 * math.pi* (r**3)也可以'
    return V

def cal_P(M,r):
    V = cal_V(r)
    return M/V/(10**12)

def cal_g(M, r):
    g = M * 6.67259 * (10**-11) / r / r / (10**6)
    return g

def cal_Ve(M, r):
    Ve = math.sqrt(2 * 6.67259 * (10**-11) * M / r / 1000) / 1000
    return Ve



if __name__ == '__main__':
    V = cal_V(6371)
    print (V)

    density = cal_P(4.869E+24, 9.28415E+11)
    print (density)

    g = cal_g(4.87E+24, 6051.8)
    print (g)

    Ve = cal_Ve (4.87E+24, 6051.8)
    print (Ve)
