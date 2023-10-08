def readtxt(filePath):
    f = open(filePath,"r")   #设置文件对象
    str = f.read()     #将txt文件的所有内容读入到字符串str中
    print(str)
    f.close()   #将文件关闭
    return str

# readtxt("E:\\kexinxing\\recognition_black\\AISAFETY\\result_ACAC.txt")