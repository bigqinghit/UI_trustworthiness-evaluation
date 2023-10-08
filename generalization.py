from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc, confusion_matrix, \
    cohen_kappa_score, roc_auc_score, hamming_loss, jaccard_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import label_binarize
import seaborn as sns


class Generalization:
    # y_true: 一维数组，或标签指示符 / 稀疏矩阵，实际（正确的）标签.
    # y_pred: 一维数组，或标签指示符 / 稀疏矩阵，分类器返回的预测标签.
    # labels: 列表，可选值.当average != binary时被包含的标签集合，如果average是None的话还包含它们的顺序.在数据中存在的标签可以被排除，比如计算一个忽略多数负类的多类平均值时，数据中没有出现的标签会导致宏平均值（marco
    # average）含有0个组件.对于多标签的目标，标签是列索引.默认情况下，y_true和y_pred中的所有标签按照排序后的顺序使用.
    # pos_label: 字符串或整型，默认为1.如果average = binary并且数据是二进制时需要被报告的类.若果数据是多类的或者多标签的，这将被忽略；设置labels = [pos_label]
    # 和average != binary就只会报告设置的特定标签的分数.
    # average: 字符串，可选值为[None, ‘binary’ (默认), ‘micro’, ‘macro’, ‘samples’, ‘weighted’].多类或
    # 者多标签目标需要这个参数.如果为None，每个类别的分数将会返回.否则，它决定了数据的平均值类型.
    # ‘binary’: 仅报告由pos_label指定的类的结果.这仅适用于目标（y_
    # {true, pred}）是二进制的情况.
    # ‘micro’: 通过计算总的真正性、假负性和假正性来全局计算指标.
    # ‘macro’: 为每个标签计算指标，找到它们未加权的均值.它不考虑标签数量不平衡的情况.
    # ‘weighted’: 为每个标签计算指标，并通过各类占比找到它们的加权均值（每个标签的正例数）.它解决了’macro’的标签不平衡问题；它可以产生不在精确率和召回率之间的F - score.
    # ‘samples’: 为每个实例计算指标，找到它们的均值（只在多标签分类的时候有意义，并且和函数accuracy_score不同）.
    # sample_weight: 形状为[样本数量]
    # 的数组，可选参数.样本权重.

    def Accuracy(self, y_pred, y_true):
        acc = accuracy_score(y_true, y_pred)  # 0.5
        # print("准确率：", acc)
        return acc

    def Precision(self, y_pred, y_true):
        pre1=precision_score(y_true, y_pred, average='macro')
        pre2=precision_score(y_true, y_pred, average='micro')
        pre3=precision_score(y_true, y_pred, average='weighted')
        # print("精确率(macro)：", precision_score(y_true, y_pred, average='macro'))  # 0.2222222222222222
        # print("精确率(micro)：", precision_score(y_true, y_pred, average='micro'))  # 0.3333333333333333
        # print("精确率(weighted)：", precision_score(y_true, y_pred, average='weighted'))  # 0.2222222222222222
        return pre1,pre2,pre3

    def Recall(self, y_pred, y_true):
        re1=recall_score(y_true, y_pred, average='macro')
        re2=recall_score(y_true, y_pred, average='micro')
        re3=recall_score(y_true, y_pred, average='weighted')
        # print("召回率(macro)：", recall_score(y_true, y_pred, average='macro'))  # 0.3333333333333333
        # print("召回率(micro)：", recall_score(y_true, y_pred, average='micro'))  # 0.3333333333333333
        # print("召回率(weighted)：", recall_score(y_true, y_pred, average='weighted'))  # 0.3333333333333333
        return re1,re2,re3

    def F_1(self, y_pred, y_true):
        f1=f1_score(y_true, y_pred, average='macro')
        f2=f1_score(y_true, y_pred, average='micro')
        f3=f1_score(y_true, y_pred, average='weighted')
        # print("F1系数(macro)：", f1_score(y_true, y_pred, average='macro'))  # 0.26666666666666666
        # print("F1系数(micro)：", f1_score(y_true, y_pred, average='micro'))  # 0.3333333333333333
        # print("F1系数(weighted)：", f1_score(y_true, y_pred, average='weighted'))  # 0.26666666666666666
        return f1,f2,f3

    def Confusionmatrix(self, y_pred, y_true, label):
        sns.set()
        fig = plt.figure(figsize=(15, 12), facecolor='black', edgecolor='white')
        ax = fig.subplots()
        C2 = confusion_matrix(y_true, y_pred, labels=label)
        sns.heatmap(C2, annot=True, ax=ax)  # 画热力图
        # ax.set_title('confusion matrix',color='white', labelsize=23)  # 标题
        ax.patch.set_facecolor("black")  # 设置 ax1 区域背景颜色
        ax.patch.set_alpha(0.5)  # 设置 ax1 区域背景颜色透明度
        ax.grid(False)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        font1 = {'family': 'Times New Roman',
                 'weight': 'normal',
                 'size': 33,
                 }
        ax.tick_params(axis='x', colors='white', labelsize=23)
        ax.tick_params(axis='y', colors='white', labelsize=23)
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.set_xlabel('predict',font1)  # x轴
        ax.set_ylabel('true',font1)  # y轴
        plt.savefig('Confusionmatrix.jpg')
        plt.cla()
        # plt.show()

    def ROC(self, y_pred, y_true):
        fpr, tpr, thersholds = roc_curve(y_true, y_pred, pos_label=2)
        # print("ROC曲线:")
        # for i, value in enumerate(thersholds):
        #     print("%f %f %f" % (fpr[i], tpr[i], value))
        roc_auc = auc(fpr, tpr)
        fig = plt.figure(figsize=(15, 12), facecolor='black', edgecolor='white')
        ax = fig.add_subplot()
        ax.patch.set_facecolor("black")  # 设置 ax1 区域背景颜色
        ax.patch.set_alpha(0.5)  # 设置 ax1 区域背景颜色透明度
        ax.grid(False)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
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
        plt.plot(fpr, tpr,  label='ROC (area = {0:.2f})'.format(roc_auc), lw=5,color='white')
        plt.xlim([-0.05, 1.05])  # 设置x、y轴的上下限，以免和边缘重合，更好的观察图像的整体
        plt.ylim([-0.05, 1.05])
        plt.xlabel('False Positive Rate',font1)
        plt.ylabel('True Positive Rate',font1)  # 可以使用中文，但需要导入一些库即字体
        # plt.title('ROC Curve')
        plt.legend(loc="lower right",prop=font1)
        plt.savefig('ROC.jpg',facecolor=fig.get_facecolor(), edgecolor='none')
        plt.cla()
        # plt.show()

    def AUC(self, y_pred, y_true, labels):
        # Binarize ytest with shape (n_samples, n_classes)
        ytest = label_binarize(y_true, classes=labels)
        # Binarize ypreds with shape (n_samples, n_classes)
        ypreds = label_binarize(y_pred, classes=labels)
        auc_score = roc_auc_score(ytest, ypreds, average='macro', multi_class='ovo')
        # print("AUC面积：", auc_score)
        return auc_score

    # def PRline(self, y_true, y_scores):
    #     plt.figure("P-R Curve")
    #     plt.title('Precision/Recall Curve')
    #     plt.xlabel('Recall')
    #     plt.ylabel('Precision')
    #     # y_true为样本实际的类别，y_scores为样本为正例的概率
    #     # y_true = np.array([1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0])
    #     # y_scores = np.array(
    #     #     [0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.62, 0.5, 0.86, 0.8, 0.47, 0.44, 0.67, 0.43, 0.4, 0.52, 0.4,
    #     #      0.35, 0.1])
    #     precision, recall, thresholds = precision_recall_curve(y_true, y_scores)
    #     plt.plot(recall, precision)
    #     plt.show()

    def kappa(self, y_pred, y_true):
        k = cohen_kappa_score(y_true, y_pred)  # (label除非是你想计算其中的分类子集的kappa系数，否则不需要设置)
        # print("kappa系数：", k)
        return k

    def haimingdistance(self, y_pred, y_true):
        ham_distance = hamming_loss(y_true, y_pred)
        # print("海明距离：", ham_distance)
        return ham_distance

    def jiekade(self, y_pred, y_true):
        j_score = jaccard_score(y_true, y_pred, average='micro')
        # print("杰卡德相似系数：", j_score)
        return j_score


def load_data(pred_path,true_path,label_num):
    f=open(pred_path, encoding='gbk')
    y_pred=[]
    for line in f:
        y_pred.append(int(line.strip()))
    # print(y_pred)

    f=open(true_path, encoding='gbk')
    y_true=[]
    for line in f:
        y_true.append(int(line.strip()))
    # print(y_true)

    label=[i for i in range(label_num)]
    # print(label)
    return y_pred,y_true,label

# y_pred,y_true,label=load_data("y_pred.txt","y_true.txt",20)
#
# Generalization().Accuracy(y_pred, y_true)
# Generalization().Precision(y_pred, y_true)
# Generalization().Recall(y_pred, y_true)
# Generalization().F_1(y_pred, y_true)
# Generalization().Confusionmatrix(y_pred, y_true, label)
# Generalization().ROC(y_pred, y_true)
# Generalization().AUC(y_pred, y_true, label)
# Generalization().kappa(y_pred, y_true)
# Generalization().haimingdistance(y_pred, y_true)
# Generalization().jiekade(y_pred, y_true)