import cv2
import numpy as np
import os


def random_noise(image, noise_num):
    '''
    添加随机噪点（实际上就是随机在图像上将像素点的灰度值变为255即白色）
    :param image: 需要加噪的图片
    :param noise_num: 添加的噪音点数目，一般是上千级别的
    :return: img_noise
    '''
    # 参数image：，noise_num：
    img = cv2.imread(image)
    img_noise = img
    rows, cols, chn = img_noise.shape
    # 加噪声
    w = img.shape  # 图片的宽
    # h = img.height  # 图片的高
    for i in range(int(noise_num*w[0]*w[1])):
        x = np.random.randint(0, rows)  # 随机生成指定范围的整数
        y = np.random.randint(0, cols)
        img_noise[x, y, :] = 255
    return img_noise


def doFile(fileDir, filepath, noise_num):
    for home, dirs, files in os.walk(fileDir):
        for filename in dirs:
            file = os.path.join(home, filename)
            # print(file)
            file1 = os.listdir(os.path.join(home, filename))
            # print(file1)
            for i in file1:
                image_noise = random_noise(os.path.join(file, i), noise_num)
                path = filepath + '//' + filename + str(noise_num)
                isExists = os.path.exists(path)
                # 判断结果
                if not isExists:
                    # 如果不存在则创建目录
                    # 创建目录操作函数
                    os.makedirs(path)
                cv2.imwrite(path + "//" + i, image_noise)
    print("运行结束！")

fileDir = "E:\\kexinxing\\zhongqi\\jiemian6\\data\\recognation\\data\\generalization"  # 源图片文件夹路径
filepath = "E:\\kexinxing\\zhongqi\\jiemian6\\data\\recognation\\data\\robust"
doFile(fileDir, filepath, noise_num=0.01)
