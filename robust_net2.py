from sklearn.metrics import mean_squared_error, mean_absolute_error,median_absolute_error
import math
import os
import matplotlib.pyplot as plt
import numpy as np

# 平均绝对误差
def PJJDWC(M, N):
    b = mean_absolute_error(M, N)
    return b

# 均方根误差
def JFGWC(M, N):
    b = math.sqrt(mean_squared_error(M, N))
    return b

# 中位数绝对误差
def ZWSJDWC(M, N):
    b = median_absolute_error(M, N)
    return b

def load_data(y_true, y_pred1,y_pred2):
    f = open(y_pred1, encoding='gbk')
    txt = []
    for line in f:
        txt.append(line.strip())
    N = []
    for i in txt:
        if 'GRoup' not in i:
            part = []
            for j in range(len(i.split('\t'))):
                part.append(float(i.split('\t')[j]))
            N.append(part)
    f = open(y_pred2, encoding='gbk')
    txt = []
    for line in f:
        txt.append(line.strip())
    N1 = []
    for i in txt:
        if 'GRoup' not in i:
            part = []
            for j in range(len(i.split('\t'))):
                part.append(float(i.split('\t')[j]))
            N1.append(part)
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
    return M,N,N1

def PJJDWC_data(y_true, y_pred, y_pred1, threshold, lapse):
    for home, dirs, files in os.walk(y_pred):
        xlist = []
        ylist = []
        ylist1 = []
        for i in files:
            pred_path=y_pred+'\\'+i
            pred_path1 = y_pred1 + '\\' + i
            M,N,N1=load_data(y_true,pred_path,pred_path1)
            x = int(i.split('.')[0])
            xlist.append(x)
            ylist.append(PJJDWC(M,N))
            ylist1.append(PJJDWC(M, N1))
    fig = plt.figure(figsize=(15, 12), facecolor='black', edgecolor='white')
    ax = fig.add_subplot()
    ax.patch.set_facecolor("black")  # 设置 ax1 区域背景颜色
    ax.patch.set_alpha(0.5)  # 设置 ax1 区域背景颜色透明度

    ax.axhline(linewidth=8, color='white')
    ax.axvline(linewidth=8, color='white')
    font1 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 33,
             }
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='x', colors='white', labelsize=23)
    ax.tick_params(axis='y', colors='white', labelsize=23)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    l1, = plt.plot(xlist, ylist, linewidth=5)
    l2, = plt.plot(xlist, [ylist[0] * threshold] * len(ylist), linewidth=5)
    l3, = plt.plot(xlist, [ylist[0] * lapse] * len(ylist), linewidth=5)
    l4, = plt.plot(xlist, ylist1, linewidth=5)
    ax.vlines([5, 15, 20], 0, 0.1, linestyles='dashed', colors='red')
    my_x_ticks = np.arange(1, 21, 1)  # 原始数据有13个点，故此处为设置从0开始，间隔为1
    plt.xticks(my_x_ticks)
    plt.legend(handles=[l1, l4,l2, l3], labels=['model1','model2','threshold', 'lapse'],prop=font1)
    plt.xlabel('noise',font1)
    plt.ylabel('mean absolute error',font1)
    plt.savefig('PJJDWC_r.jpg')
    plt.cla()
    # plt.show()
    return ylist,ylist1


def ZWSJDWC_data(y_true, y_pred, y_pred1,threshold, lapse):
    for home, dirs, files in os.walk(y_pred):
        xlist = []
        ylist = []
        ylist1 = []
        for i in files:
            pred_path = y_pred + '\\' + i
            pred_path1 = y_pred1 + '\\' + i
            M, N, N1 = load_data(y_true, pred_path, pred_path1)
            x = int(i.split('.')[0])
            xlist.append(x)
            ylist.append(ZWSJDWC(M, N))
            ylist1.append(ZWSJDWC(M, N1))
    fig = plt.figure(figsize=(15, 12), facecolor='black', edgecolor='white')
    ax = fig.add_subplot()
    ax.patch.set_facecolor("black")  # 设置 ax1 区域背景颜色
    ax.patch.set_alpha(0.5)  # 设置 ax1 区域背景颜色透明度

    ax.axhline(linewidth=8, color='white')
    ax.axvline(linewidth=8, color='white')
    font1 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 33,
             }
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='x', colors='white', labelsize=23)
    ax.tick_params(axis='y', colors='white', labelsize=23)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    l1, = plt.plot(xlist, ylist, linewidth=3)
    l2, = plt.plot(xlist, [ylist[0] * threshold] * len(ylist), linewidth=5)
    l3, = plt.plot(xlist, [ylist[0] * lapse] * len(ylist), linewidth=5)
    l4, = plt.plot(xlist, ylist1, linewidth=3)
    ax.vlines([5, 15, 20], 0, 0.005, linestyles='dashed', colors='red')
    my_x_ticks = np.arange(1, 21, 1)  # 原始数据有13个点，故此处为设置从0开始，间隔为1
    plt.xticks(my_x_ticks)
    plt.legend(handles=[l1, l4,l2, l3], labels=['model1','model2','threshold', 'lapse'],prop=font1)
    plt.xlabel('noise',font1)
    plt.ylabel('median absolute error',font1)
    plt.savefig('ZWSJDWC_r.jpg')
    plt.cla()
    # plt.show()
    return ylist,ylist1

def JFGWC_data(y_true, y_pred, y_pred1,threshold, lapse):
    for home, dirs, files in os.walk(y_pred):
        xlist = []
        ylist = []
        ylist1 = []
        for i in files:
            pred_path = y_pred + '\\' + i
            pred_path1 = y_pred1 + '\\' + i
            M, N, N1 = load_data(y_true, pred_path, pred_path1)
            x = int(i.split('.')[0])
            xlist.append(x)
            ylist.append(JFGWC(M, N))
            ylist1.append(JFGWC(M, N1))
    # print(ylist)
    # print(ylist1)
    fig = plt.figure(figsize=(15, 12), facecolor='black', edgecolor='white')
    ax = fig.add_subplot()
    ax.patch.set_facecolor("black")  # 设置 ax1 区域背景颜色
    ax.patch.set_alpha(0.5)  # 设置 ax1 区域背景颜色透明度

    ax.axhline(linewidth=8, color='white')
    ax.axvline(linewidth=8, color='white')
    font1 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 33,
             }
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='x', colors='white', labelsize=23)
    ax.tick_params(axis='y', colors='white', labelsize=23)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    l1, = plt.plot(xlist, ylist, linewidth=5)
    l2, = plt.plot(xlist, [ylist[0] * threshold] * len(ylist), linewidth=5)
    l3, = plt.plot(xlist, [ylist[0] * lapse] * len(ylist), linewidth=5)
    l4, = plt.plot(xlist, ylist1, linewidth=5)
    ax.vlines([5, 15, 20], 0, 0.3, linestyles='dashed', colors='red')
    my_x_ticks = np.arange(1, 21, 1)  # 原始数据有13个点，故此处为设置从0开始，间隔为1
    plt.xticks(my_x_ticks)
    plt.legend(handles=[l1, l4,l2, l3], labels=['model1','model2','threshold', 'lapse'],prop=font1)
    plt.xlabel('noise', font1)
    plt.ylabel('mean squared error', font1)
    plt.savefig('JFGWC_r.jpg')
    plt.cla()
    # plt.show()
    return ylist,ylist1

def calculate(y_true, y_pred, y_pred1):
    cal=0
    cal1=0
    for home, dirs, files in os.walk(y_pred):
        xlist = []
        ylist = []
        ylist1 = []
        for i in files:
            pred_path = y_pred + '\\' + i
            pred_path1 = y_pred1 + '\\' + i
            M, N, N1 = load_data(y_true, pred_path, pred_path1)
            x = int(i.split('.')[0])
            xlist.append(x)
            ylist.append(ZWSJDWC(M, N))
            ylist1.append(ZWSJDWC(M, N1))
            ylist.append(PJJDWC(M, N))
            ylist1.append(PJJDWC(M, N1))
            ylist.append(JFGWC(M, N))
            ylist1.append(JFGWC(M, N1))
    for i in range(len(ylist)):
        if ylist[i]>ylist1[i]:
            cal1+=1
        elif ylist1[i]>ylist[i]:
            cal+=1
        else:
            cal+=1
            cal1+=1
    return cal,cal1


# y_true='E:\\kexinxing\\jcdata\\std_output_cpp.txt'
# y_pred='E:\\kexinxing\\jcdata\\noise_compare\\AI'
# y_pred1='E:\\kexinxing\\jcdata\\noise_compare\\FPGA'
# PJJDWC_data(y_true,y_pred,y_pred1,30,60)
# ZWSJDWC_data(y_true,y_pred,y_pred1,30,60)
# JFGWC_data(y_true,y_pred,y_pred1,30,60)
#分割文件
# a=open('E:\\kexinxing\\jcdata\\noise_compare\\noise_AI_output.txt','r').readlines()
# n=20 #份数
# qty=len(a)//n if len(a)%n==0 else len(a)//n+1  #每一份的行数
# for i in range(n):
#     f=open(str(i+1)+'.txt', 'a')
#     f.writelines(a[i*qty:(i+1)*qty])
#     f.close()

# a=open('E:\\kexinxing\\jcdata\\noise_compare\\noise_FPGA_output.txt','r').readlines()
# n=20 #份数
# qty=len(a)//n if len(a)%n==0 else len(a)//n+1  #每一份的行数
# for i in range(n):
#     f=open(str(i+1)+'.txt', 'a')
#     f.writelines(a[i*qty:(i+1)*qty])
#     f.close()