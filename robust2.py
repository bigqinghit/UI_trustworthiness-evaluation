from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
import os
import numpy as np
import random


def shelter(impath, mianji):
    img2 = Image.open(impath)
    w = img2.width  # 图片的宽
    h = img2.height  # 图片的高
    # print(w, h)
    num_w = random.sample(range(int(int(mianji*w*h) / 256) + 3, min(int(mianji*w*h) // 2,255)), 1)
    # print(num_w)
    xline = random.sample(range(0, w - num_w[0]), 1)
    yline = random.sample(range(0, h - int(int(mianji*w*h) // num_w[0]) - 1), 1)
    xline.append(xline[0] + num_w[0])
    yline.append(yline[0] + int(mianji*w*h) / num_w[0])
    # print(xline[0], xline[1], yline[0], yline[1])

    draw = ImageDraw.Draw(img2)
    draw.rectangle((xline[0], yline[0], xline[1], yline[1]), fill=(0, 0, 0))
    img2 = np.asarray(img2) / 255.00
    del draw
    return img2
    # plt.imshow(img2)
    # plt.title("Add obstacle")
    # plt.savefig("obstacle_image.jpg")


def doFile(fileDir, filepath, mianji):
    for home, dirs, files in os.walk(fileDir):
        for filename in dirs:
            file = os.path.join(home, filename)
            # print(file)
            file1 = os.listdir(os.path.join(home, filename))
            # print(file1)
            for i in file1:
                image_noise = shelter(os.path.join(file, i), mianji)
                path = filepath + '\\' + filename
                isExists = os.path.exists(path)
                # 判断结果
                if not isExists:
                    # 如果不存在则创建目录
                    # 创建目录操作函数
                    os.makedirs(path)

                plt.figure(figsize=(256, 256), dpi=1)
                plt.gca().xaxis.set_major_locator(plt.NullLocator())
                plt.gca().yaxis.set_major_locator(plt.NullLocator())
                plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
                plt.imshow(image_noise)
                plt.axis('off')
                # plt.title("Add obstacle")
                plt.savefig(path + "\\" + i)
    print("运行结束！")

# fileDir = "E:\\kexinxing\\recognition_black\\test\\generalization"  # 源图片文件夹路径
# filepath = "E:\\kexinxing\\recognition_black\\test\\robustness\\robustness_zhedang\\0.04"
# doFile(fileDir, filepath, 0.04)
