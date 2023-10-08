import imgaug.augmenters as iaa
from skimage import io
from matplotlib import pyplot as plt
import shutil

def unblance(img,targetdir):
    # img = r"1.jpg"
    img = io.imread(img)

    res_img={}

    augtmp = iaa.Affine(rotate=(-180, 180))
    res = augtmp.augment_image(img)
    res_img["FSBH"]=res

    #仿射变换，设置参数
    #augtmp = iaa.Affine(
    #    scale={"x": (0.8, 1.2), "y": (0.8, 1.2)}, #缩放
    #    translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)}, #平移
    #    rotate=(-20, 60),                        #旋转
    #    shear=(-8, 8) )
    #res = augtmp.augment_image(img)
    #plt.imshow(res)
    #plt.show()

    augtmp = iaa.Fliplr(1.0)
    res = augtmp.augment_image(img)
    res_img["FZ"]=res

    augtmp = iaa.Crop(px=(0, 200), keep_size=True)
    res = augtmp.augment_image(img)
    res_img["CJ"]=res

    augtmp = iaa.ContrastNormalization((0.75, 1.5))
    res = augtmp.augment_image(img)
    res_img["CJ"]=res

    augtmp = iaa.AdditiveGaussianNoise(loc=1, scale=(0.01, 0.08*255))
    res = augtmp.augment_image(img)
    res_img["GSZY"]=res

    augtmp = iaa.GaussianBlur(sigma=0.1)
    res = augtmp.augment_image(img)
    res_img["GSMH"]=res

    augtmp= iaa.AverageBlur(k=2)
    res = augtmp.augment_image(img)
    res_img["PJMH"]=res

    augtmp = iaa.MedianBlur(k=3)
    res = augtmp.augment_image(img)
    res_img["ZZMH"]=res

    augtmp = iaa.MotionBlur()
    res = augtmp.augment_image(img)
    res_img["YDMH"]=res

    augtmp = iaa.BilateralBlur()
    res = augtmp.augment_image(img)
    res_img["SBMH"]=res

    augtmp = iaa.WithColorspace(to_colorspace="HSV")
    res = augtmp.augment_image(img)
    res_img["SCKJ"]=res

    augtmp = iaa.AddToHueAndSaturation((-20, 20), per_channel=True)
    res = augtmp.augment_image(img)
    res_img["SJSDBHD"]=res

    augtmp = iaa.Grayscale(alpha=1.0)
    res = augtmp.augment_image(img)
    res_img["HDT"]=res

    augtmp = iaa.CLAHE(clip_limit=(1, 10))
    res = augtmp.augment_image(img)
    res_img["GBYSKJ"]=res

    augtmp = iaa.GammaContrast(gamma=3)
    res = augtmp.augment_image(img)
    res_img["Gamma"]=res

    augtmp = iaa.SigmoidContrast(gain=10)
    res = augtmp.augment_image(img)
    res_img["Sigmoid"]=res

    augtmp = iaa.LogContrast(gain=5)
    res = augtmp.augment_image(img)
    res_img["Log"]=res

    augtmp = iaa.LinearContrast(alpha=10)
    res = augtmp.augment_image(img)
    res_img["XXDBD"]=res

    for k,v in res_img.items():
        print(k)
        plt.imshow(v)
        plt.axis('off')
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        plt.margins(0, 0)

        # plt.show()
        plt.savefig(k+'.jpg')
        shutil.copy(k+'.jpg', targetdir+'\\'+k+'.jpg')

# unblance('1.jpg')