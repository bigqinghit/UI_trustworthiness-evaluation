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
            print(file)
            file1 = os.listdir(os.path.join(home, filename))
            print(file1)
            for i in file1:
                image_noise = random_noise(os.path.join(file, i), noise_num)
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
        noise_num=qishi+buchang*i
        print(noise_num)
        # fileDir = "D:\\data\\recognition\\data\\generalization"  # 源图片文件夹路径
        # tarDir = "D:\\data\\recognition\\data\\robust"
        tarDir1=tarDir+"\\robustness_noise\\"+str(format(noise_num,'.2f'))
        if not os.path.exists(tarDir1):
            os.makedirs(tarDir1)
        doFile(fileDir, tarDir1, noise_num)
