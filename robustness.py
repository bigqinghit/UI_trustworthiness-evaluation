from sklearn.metrics import accuracy_score, precision_score, recall_score
import os
import matplotlib.pyplot as plt


def Accuracy(y_pred, y_true):
    acc = accuracy_score(y_true, y_pred)
    print("准确率：", acc)
    return acc


def Precision(y_pred, y_true):
    pre = precision_score(y_true, y_pred, average='macro')
    print("精确率(macro)：", pre)  # 0.2222222222222222
    # print("精确率(micro)：", precision_score(y_true, y_pred, average='micro'))  # 0.3333333333333333
    # print("精确率(weighted)：", precision_score(y_true, y_pred, average='weighted'))  # 0.2222222222222222
    return pre


def Recall(y_pred, y_true):
    rec = recall_score(y_true, y_pred, average='macro')
    print("召回率(macro)：", rec)  # 0.3333333333333333
    # print("召回率(micro)：", recall_score(y_true, y_pred, average='micro'))  # 0.3333333333333333
    # print("召回率(weighted)：", recall_score(y_true, y_pred, average='weighted'))  # 0.3333333333333333
    return rec


def load_data(pred_path, true_path, label_num):
    f = open(pred_path, encoding='gbk')
    y_pred = []
    for line in f:
        y_pred.append(int(line.strip()))
    # print(y_pred)

    f = open(true_path, encoding='gbk')
    y_true = []
    for line in f:
        y_true.append(int(line.strip()))
    # print(y_true)

    label = [i for i in range(label_num)]
    return y_pred, y_true, label


def run_A(filepath, threshold, lapse):
    xlist = []
    ylist = []
    for home, dirs, files in os.walk(filepath):
        for file in dirs:  # zhedang0.01,zhedang0.02,zhedang0.03
            x = int(file.split('.')[1])
            # print(x)
            xlist.append(x)
            path = os.path.join(filepath, file)
            filenames = os.listdir(path)
            for name in filenames:
                # print(name)
                if name == 'y_pred.txt':
                    pred_path = os.path.join(path, name)
                if name == 'y_true.txt':
                    true_path = os.path.join(path, name)

            y_pred, y_true, label = load_data(pred_path, true_path, 20)
            y = Accuracy(y_pred, y_true)
            # print(y)
            ylist.append(y)

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
    ax.vlines([5, 15, 20], 0,1,linestyles='dashed', colors='red')
    plt.legend(handles=[l1, l2, l3], labels=['Accuracy', 'threshold', 'lapse'], prop=font1)
    plt.xlabel('noise', font1)
    plt.ylabel('Accuracy', font1)
    plt.savefig('Accuracy.jpg')
    plt.cla()
    # plt.show()
    return ylist


def run_P(filepath, threshold, lapse):
    xlist = []
    ylist = []
    for home, dirs, files in os.walk(filepath):
        for file in dirs:  # zhedang0.01,zhedang0.02,zhedang0.03
            x = int(file.split('.')[1])
            # print(x)
            xlist.append(x)
            path = os.path.join(filepath, file)
            filenames = os.listdir(path)
            for name in filenames:
                # print(name)
                if name == 'y_pred.txt':
                    pred_path = os.path.join(path, name)
                if name == 'y_true.txt':
                    true_path = os.path.join(path, name)

            y_pred, y_true, label = load_data(pred_path, true_path, 20)
            y = Precision(y_pred, y_true)
            # print(y)
            ylist.append(y)
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
    plt.savefig('Precision.jpg')
    plt.cla()
    # plt.show()
    return ylist


def run_R(filepath, threshold, lapse):
    xlist = []
    ylist = []
    for home, dirs, files in os.walk(filepath):
        for file in dirs:  # zhedang0.01,zhedang0.02,zhedang0.03
            x = int(file.split('.')[1])
            # print(x)
            xlist.append(x)
            path = os.path.join(filepath, file)
            filenames = os.listdir(path)
            for name in filenames:
                # print(name)
                if name == 'y_pred.txt':
                    pred_path = os.path.join(path, name)
                if name == 'y_true.txt':
                    true_path = os.path.join(path, name)

            y_pred, y_true, label = load_data(pred_path, true_path, 20)
            y = Recall(y_pred, y_true)
            # print(y)
            ylist.append(y)

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
    plt.legend(handles=[l1, l2, l3], labels=['Recall', 'threshold', 'lapse'], prop=font1)
    # plt.legend(handles=[l1, l2, l3], labels=['Recall', 'threshold', 'lapse'])
    plt.xlabel('noise', font1)
    plt.ylabel('Recall', font1)
    plt.savefig('Recall.jpg')
    plt.cla()
    # plt.show()
    return ylist

# run_R('E:\\kexinxing\\zhongqi\\recognition\\zhibiao\\y\\robust_zhedang_txt',0.95,0.9)
