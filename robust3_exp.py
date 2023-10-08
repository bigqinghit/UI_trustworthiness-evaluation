import cv2
import numpy as np
import os

def gasuss_noise(image, var, mean=0):
    '''
        添加高斯噪声
        image:原始图像
        mean : 均值
        var : 方差,越大，噪声越大
    '''
    image = cv2.imread(image)
    image = np.array(image/255, dtype=float)#将原始图像的像素值进行归一化，除以255使得像素值在0-1之间
    noise = np.random.normal(mean, var ** 0.5, image.shape)#创建一个均值为mean，方差为var呈高斯分布的图像矩阵
    out = image + noise#将噪声和原始图像进行相加得到加噪后的图像
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)#clip函数将元素的大小限制在了low_clip和1之间了，小于的用low_clip代替，大于1的用1代替
    out = np.uint8(out*255)#解除归一化，乘以255将加噪后的图像的像素值恢复
    #cv.imshow("gasuss", out)
    noise = noise*255
    return out

def doFile(fileDir, filepath, var):
    for home, dirs, files in os.walk(fileDir):
        for filename in dirs:
            file = os.path.join(home, filename)
            print(file)
            file1 = os.listdir(os.path.join(home, filename))
            print(file1)
            for i in file1:
                image_noise = gasuss_noise(os.path.join(file, i), var, mean=0)
                path = filepath + '//' + filename
                isExists = os.path.exists(path)
                # 判断结果
                if not isExists:
                    # 如果不存在则创建目录
                    # 创建目录操作函数
                    os.makedirs(path)
                cv2.imwrite(path + "//" + i, image_noise)

def main(fileDir,tarDir,qishi,buchang,zu):
    for i in range(zu):
        var=qishi+buchang*i
        print(var)
        # fileDir = "D:\\data\\recognition\\data\\generalization"  # 源图片文件夹路径
        # tarDir = "D:\\data\\recognition\\data\\robust"
        tarDir1=tarDir+"\\robustness_gasuss\\"+str(format(var,'.2f'))
        if not os.path.exists(tarDir1):
            os.makedirs(tarDir1)
        doFile(fileDir, tarDir1, var)