from sklearn.metrics import accuracy_score, precision_score, recall_score
import os
import matplotlib.pyplot as plt
import json


def Accuracy(y_pred, y_true):
    acc = accuracy_score(y_true, y_pred)
    print("准确率：", acc)
    return acc


def Precision(y_pred, y_true):
    pre = precision_score(y_true, y_pred, average='macro')
    # print("精确率(macro)：", pre)  # 0.2222222222222222
    print("精确率(micro)：", precision_score(y_true, y_pred, average='micro'))  # 0.3333333333333333
    # print("精确率(weighted)：", precision_score(y_true, y_pred, average='weighted'))  # 0.2222222222222222
    return pre


def Recall(y_pred, y_true):
    rec = recall_score(y_true, y_pred, average='macro')
    print("召回率(macro)：", rec)  # 0.3333333333333333
    # print("召回率(micro)：", recall_score(y_true, y_pred, average='micro'))  # 0.3333333333333333
    # print("召回率(weighted)：", recall_score(y_true, y_pred, average='weighted'))  # 0.3333333333333333
    return rec


def load_data(pred_path, true_path):
    with open(true_path, encoding='gbk') as f:
        in_format = json.loads(f.read())
    with open(pred_path, encoding='gbk') as f:
        in_format_change = json.loads(f.read())
    zhibiao = in_format[0]['output']
    change = in_format_change[0]['output']
    y_pred = []
    y_true = []
    for i in zhibiao:
        if zhibiao[i] == False:
            zhibiao[i] = 0
        elif zhibiao[i] == True:
            zhibiao[i] = 1
        elif zhibiao[i] == None:
            zhibiao[i] = 100
        y_true.append(zhibiao[i])
    for i in change:
        if change[i] == False:
            change[i] = 0
        elif change[i] == True:
            change[i] = 1
        elif change[i] == None:
            change[i] = 100
        y_pred.append(change[i])
    return y_pred, y_true


def run_A(pred_path, true_path, threshold, lapse):
    for home, dirs, files in os.walk(pred_path):
        xlist = []
        ylist = []
        for i in files:
            y_pred, y_true = load_data(pred_path + '\\' + i, true_path)
            ylist.append(Accuracy(y_pred, y_true))
            x = int(i.split('.')[1])
            xlist.append(x)
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
    ax.tick_params(axis='x', colors='white', labelsize=23)
    ax.tick_params(axis='y', colors='white', labelsize=23)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    l1, = plt.plot(xlist, ylist, linewidth=5)
    l2, = plt.plot(xlist, [ylist[0] * threshold] * len(ylist), linewidth=5)
    l3, = plt.plot(xlist, [ylist[0] * lapse] * len(ylist), linewidth=5)
    ax.vlines([5, 15, 20], 0, 1, linestyles='dashed', colors='red')
    plt.legend(handles=[l1, l2, l3], labels=['Accuracy', 'threshold', 'lapse'], prop=font1)
    plt.xlabel('noise', font1)
    plt.ylabel('Accuracy', font1)
    plt.savefig('Accuracy_j.jpg')
    plt.cla()
    # plt.show()
    return ylist
    # plt.plot(xlist, ylist)
    # plt.plot(xlist, [ylist[0] * threshold] * len(ylist))
    # plt.plot(xlist, [ylist[0] * lapse] * len(ylist))
    # plt.legend(['Accuracy', 'threshold', 'lapse'])
    # plt.xlabel('Accuracy')
    # plt.ylabel('noise')
    # plt.title('Accuracy')
    # # plt.show()
    # plt.savefig('Accuracy_j.jpg')
    # plt.cla()
    # return ylist


def run_P(pred_path, true_path, threshold, lapse):
    for home, dirs, files in os.walk(pred_path):
        xlist = []
        ylist = []
        for i in files:
            y_pred, y_true = load_data(pred_path + '\\' + i, true_path)
            ylist.append(Precision(y_pred, y_true))
            x = int(i.split('.')[1])
            xlist.append(x)
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
    ax.tick_params(axis='x', colors='white', labelsize=23)
    ax.tick_params(axis='y', colors='white', labelsize=23)
    ax.grid(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    l1, = plt.plot(xlist, ylist, linewidth=5)
    l2, = plt.plot(xlist, [ylist[0] * threshold] * len(ylist), linewidth=5)
    l3, = plt.plot(xlist, [ylist[0] * lapse] * len(ylist), linewidth=5)
    ax.vlines([5, 15, 20], 0, 1, linestyles='dashed', colors='red')
    plt.legend(handles=[l1, l2, l3], labels=['Precision', 'threshold', 'lapse'], prop=font1)
    plt.xlabel('noise', font1)
    plt.ylabel('Precision', font1)
    plt.savefig('Precision_j.jpg')
    plt.cla()
    # plt.show()
    return ylist
    # plt.plot(xlist, ylist)
    # plt.plot(xlist, [ylist[0] * threshold] * len(ylist))
    # plt.plot(xlist, [ylist[0] * lapse] * len(ylist))
    # plt.legend(['Precision', 'threshold', 'lapse'])
    # plt.xlabel('Precision')
    # plt.ylabel('noise')
    # plt.title('Precision')
    # # plt.show()
    # plt.savefig('Precision_j.jpg')
    # plt.cla()
    # return ylist


def run_R(pred_path, true_path, threshold, lapse):
    for home, dirs, files in os.walk(pred_path):
        xlist = []
        ylist = []
        for i in files:
            y_pred, y_true = load_data(pred_path + '\\' + i, true_path)
            ylist.append(Recall(y_pred, y_true))
            x = int(i.split('.')[1])
            xlist.append(x)
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
    ax.vlines([5, 15, 20], 0, 1, linestyles='dashed', colors='red')
    plt.legend(handles=[l1, l2, l3], labels=['Recall', 'threshold', 'lapse'], prop=font1)
    plt.xlabel('noise', font1)
    plt.ylabel('Recall', font1)
    plt.savefig('Recall_j.jpg')
    plt.cla()
    # plt.show()
    return ylist
    # plt.plot(xlist, ylist)
    # plt.plot(xlist, [ylist[0] * threshold] * len(ylist))
    # plt.plot(xlist, [ylist[0] * lapse] * len(ylist))
    # plt.legend(['Recall', 'threshold', 'lapse'])
    # plt.xlabel('Recall')
    # plt.ylabel('Recall')
    # plt.title('Recall')
    # # plt.show()
    # plt.savefig('Recall_j.jpg')
    # plt.cla()
    # return ylist

# true_path = 'E:\\kexinxing\\zhongqi\\juece\\data\\Shared-Solution\\output_U1QGX4HJSXGZ_00000000.json'
# pred_path = 'E:\\kexinxing\\zhongqi\\juece\\data\\Shared-Solution\\robust'
# run_P(pred_path, true_path, 0.95, 0.9)
