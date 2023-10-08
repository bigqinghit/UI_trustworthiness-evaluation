from sklearn.metrics import explained_variance_score, mean_squared_error, mean_absolute_error, \
    mean_absolute_percentage_error, r2_score, median_absolute_error
from numpy import *
import numpy as np
import math
import matplotlib.pyplot as plt

def load_data(y_true, y_pred):
    f = open(y_true, encoding='gbk')
    txt = []
    for line in f:
        txt.append(line.strip().split('{')[1].split('}')[0])
    M = []
    for i in range(len(txt) - 4):
        part = []
        for j in range(len(txt[i].split(',')) - 1):
            part.append(float(txt[i].split(',')[j]))
        M.append(part)

    f = open(y_pred, encoding='gbk')
    txt = []
    for line in f:
        txt.append(line.strip())
    N = []
    for i in txt:
        part = []
        for j in range(len(i.split('\t'))):
            part.append(float(i.split('\t')[j]))
        N.append(part)
    return M, N


# 均方误差
def JFWC(M, N):
    result = []
    for i in range(280):
        result.append(mean_squared_error(M[i], N[i], multioutput='raw_values')[0])
    b = mean_squared_error(M, N)
    xlist=[]
    for i in range(1,281):
        xlist.append(i)
    fig = plt.figure(figsize=(15, 12), facecolor='black', edgecolor='white')
    ax = fig.add_subplot()
    ax.patch.set_facecolor("black")  # 设置 ax1 区域背景颜色
    ax.patch.set_alpha(0.5)  # 设置 ax1 区域背景颜色透明度
    ax.axhline(linewidth=8, color='white')
    ax.axvline(linewidth=8, color='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='x', colors='white', labelsize=23)
    ax.tick_params(axis='y', colors='white', labelsize=23)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.plot(xlist, result)
    # plt.show()
    plt.savefig('JFWC.jpg')
    return result, b

# 平均绝对误差
def PJJDWC(M, N):
    result = []
    for i in range(280):
        result.append(mean_absolute_error(M[i], N[i], multioutput='raw_values')[0])
    b = mean_absolute_error(M, N)
    xlist = []
    for i in range(1, 281):
        xlist.append(i)
    fig = plt.figure(figsize=(15, 12), facecolor='black', edgecolor='white')
    ax = fig.add_subplot()
    ax.patch.set_facecolor("black")  # 设置 ax1 区域背景颜色
    ax.patch.set_alpha(0.5)  # 设置 ax1 区域背景颜色透明度
    ax.axhline(linewidth=8, color='white')
    ax.axvline(linewidth=8, color='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='x', colors='white', labelsize=23)
    ax.tick_params(axis='y', colors='white', labelsize=23)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.plot(xlist, result)
    # plt.show()
    plt.savefig('PJJDWC.jpg')
    return result, b

# 平均绝对百分比误差
def PJJDBFBWC(M, N):
    result = []
    for i in range(280):
        result.append(mean_absolute_percentage_error(M[i], N[i], multioutput='raw_values')[0])
    b = mean_absolute_percentage_error(M, N)
    xlist = []
    for i in range(1, 281):
        xlist.append(i)
    fig = plt.figure(figsize=(15, 12), facecolor='black', edgecolor='white')
    ax = fig.add_subplot()
    ax.patch.set_facecolor("black")  # 设置 ax1 区域背景颜色
    ax.patch.set_alpha(0.5)  # 设置 ax1 区域背景颜色透明度
    ax.axhline(linewidth=8, color='white')
    ax.axvline(linewidth=8, color='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='x', colors='white', labelsize=23)
    ax.tick_params(axis='y', colors='white', labelsize=23)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.plot(xlist, result)
    # plt.show()
    plt.savefig('PJJDBFBWC.jpg')
    return result, b


# 决定系数
def JDXS(M, N):
    result = []
    for i in range(280):
        result.append(r2_score(M[i], N[i], multioutput='raw_values')[0])
    b = r2_score(M, N)
    xlist = []
    for i in range(1, 281):
        xlist.append(i)
    fig = plt.figure(figsize=(15, 12), facecolor='black', edgecolor='white')
    ax = fig.add_subplot()
    ax.patch.set_facecolor("black")  # 设置 ax1 区域背景颜色
    ax.patch.set_alpha(0.5)  # 设置 ax1 区域背景颜色透明度
    ax.axhline(linewidth=8, color='white')
    ax.axvline(linewidth=8, color='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='x', colors='white', labelsize=23)
    ax.tick_params(axis='y', colors='white', labelsize=23)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.plot(xlist, result)
    # plt.show()
    plt.savefig('JDXS.jpg')
    return result, b



# 中位数绝对误差
def ZWSJDWC(M, N):
    result = []
    for i in range(280):
        result.append(median_absolute_error(M[i], N[i], multioutput='raw_values')[0])
    b = median_absolute_error(M, N)
    xlist = []
    for i in range(1, 281):
        xlist.append(i)
    fig = plt.figure(figsize=(15, 12), facecolor='black', edgecolor='white')
    ax = fig.add_subplot()
    ax.patch.set_facecolor("black")  # 设置 ax1 区域背景颜色
    ax.patch.set_alpha(0.5)  # 设置 ax1 区域背景颜色透明度
    ax.axhline(linewidth=8, color='white')
    ax.axvline(linewidth=8, color='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='x', colors='white', labelsize=23)
    ax.tick_params(axis='y', colors='white', labelsize=23)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.plot(xlist, result)
    # plt.show()
    plt.savefig('ZWSJDWC.jpg')
    return result, b


# 希尔不等系数
def XEBDXS(M, N):
    result = []
    for i in range(280):
        result.append(mean_squared_error(M[i], N[i], multioutput='raw_values')[0] / (
                    (math.pow(sum(M[i]), 2) / 7) ** 0.5 + (math.pow(sum(N[i]), 2) / 7) ** 0.5))
    b = mean_squared_error(M, N) / ((math.pow(sum(M), 2) / 7) ** 0.5 + (math.pow(sum(N), 2) / 7) ** 0.5)
    xlist = []
    for i in range(1, 281):
        xlist.append(i)
    fig = plt.figure(figsize=(15, 12), facecolor='black', edgecolor='white')
    ax = fig.add_subplot()
    ax.patch.set_facecolor("black")  # 设置 ax1 区域背景颜色
    ax.patch.set_alpha(0.5)  # 设置 ax1 区域背景颜色透明度
    ax.axhline(linewidth=8, color='white')
    ax.axvline(linewidth=8, color='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='x', colors='white', labelsize=23)
    ax.tick_params(axis='y', colors='white', labelsize=23)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.plot(xlist, result)
    # plt.show()
    plt.savefig('XEBDXS.jpg')
    return result, b


# 协方差率
def XEBDXS(M, N):
    result = []
    for i in range(280):
        result.append(mean_squared_error(M[i], N[i], multioutput='raw_values')[0] / (
                    (math.pow(sum(M[i]), 2) / 7) ** 0.5 + (math.pow(sum(N[i]), 2) / 7) ** 0.5))
    b = mean_squared_error(M, N) / ((math.pow(sum(M), 2) / 7) ** 0.5 + (math.pow(sum(N), 2) / 7) ** 0.5)
    xlist = []
    for i in range(1, 281):
        xlist.append(i)
    fig = plt.figure(figsize=(15, 12), facecolor='black', edgecolor='white')
    ax = fig.add_subplot()
    ax.patch.set_facecolor("black")  # 设置 ax1 区域背景颜色
    ax.patch.set_alpha(0.5)  # 设置 ax1 区域背景颜色透明度
    ax.axhline(linewidth=8, color='white')
    ax.axvline(linewidth=8, color='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='x', colors='white', labelsize=23)
    ax.tick_params(axis='y', colors='white', labelsize=23)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.plot(xlist, result)
    # plt.show()
    plt.savefig('XEBDXS.jpg')
    return result, b


# 解释方差分数
def JSFCFS(M, N):
    result = []
    for i in range(280):
        result.append(explained_variance_score(M[i], N[i], multioutput='raw_values')[0])
    b = explained_variance_score(M, N)
    xlist = []
    for i in range(1, 281):
        xlist.append(i)
    fig = plt.figure(figsize=(15, 12), facecolor='black', edgecolor='white')
    ax = fig.add_subplot()
    ax.patch.set_facecolor("black")  # 设置 ax1 区域背景颜色
    ax.patch.set_alpha(0.5)  # 设置 ax1 区域背景颜色透明度
    ax.axhline(linewidth=8, color='white')
    ax.axvline(linewidth=8, color='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='x', colors='white', labelsize=23)
    ax.tick_params(axis='y', colors='white', labelsize=23)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.plot(xlist, result)
    # plt.show()
    plt.savefig('JSFCFS.jpg')
    return result, b


# 方差率
def FCL(M, N):
    result = []
    L = 0
    for i in range(280):
        a = math.pow(np.var(M[i]) - np.var(N[i]), 2)
        b = math.pow(sum(M[i]) - sum(N[i]), 2) / 7
        result.append(a / b)
        L += math.pow((sum(M[i]) - sum(N[i])), 2)
    c = math.pow(np.var(M) - np.var(N), 2) / (L / (280 * 7))
    xlist = []
    for i in range(1, 281):
        xlist.append(i)
    fig = plt.figure(figsize=(15, 12), facecolor='black', edgecolor='white')
    ax = fig.add_subplot()
    ax.patch.set_facecolor("black")  # 设置 ax1 区域背景颜色
    ax.patch.set_alpha(0.5)  # 设置 ax1 区域背景颜色透明度
    ax.axhline(linewidth=8, color='white')
    ax.axvline(linewidth=8, color='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='x', colors='white', labelsize=23)
    ax.tick_params(axis='y', colors='white', labelsize=23)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.plot(xlist, result)
    # plt.show()
    plt.savefig('FCL.jpg')
    return result, c


# 均方根误差
def JFGWC(M, N):
    result = []
    for i in range(280):
        result.append(math.sqrt(mean_squared_error(M[i], N[i], multioutput='raw_values')[0]))
    b = math.sqrt(mean_squared_error(M, N))
    xlist = []
    for i in range(1, 281):
        xlist.append(i)
    fig = plt.figure(figsize=(15, 12), facecolor='black', edgecolor='white')
    ax = fig.add_subplot()
    ax.patch.set_facecolor("black")  # 设置 ax1 区域背景颜色
    ax.patch.set_alpha(0.5)  # 设置 ax1 区域背景颜色透明度
    ax.axhline(linewidth=8, color='white')
    ax.axvline(linewidth=8, color='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='x', colors='white', labelsize=23)
    ax.tick_params(axis='y', colors='white', labelsize=23)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.plot(xlist, result)
    # plt.show()
    plt.savefig('JFGWC.jpg')
    return result, b

y_true='E:\\kexinxing\\jcdata\\std_output_cpp.txt'
y_pred='E:\\kexinxing\\jcdata\\AI_output.txt'
M,N=load_data(y_true,y_pred)
result,b=PJJDWC(M,N)