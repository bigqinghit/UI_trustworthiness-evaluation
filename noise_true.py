import json
import random
import shutil
import os


def change(sourceDir, targetDir, noise,num):
    with open(sourceDir) as f:
        in_format = json.loads(f.read())
    zhibiao = in_format[0]['input']
    rand = random.sample(zhibiao.keys(), int(len(zhibiao) * num))
    # print(rand)
    for i in zhibiao:
        if i in rand:
            if type(zhibiao[i]) is float:
                zhibiao[i] = random.choice([zhibiao[i] * (1 + noise), zhibiao[i] * (1 - noise)])
            elif type(zhibiao[i]) is int:
                zhibiao[i] = random.choice([int(zhibiao[i] * (1 + noise)), int(zhibiao[i] * (1 - noise))])
            elif type(zhibiao[i]) is bool:
                choice = [True, False]
                b = choice.pop(zhibiao[i])
                zhibiao[i] = random.choice([b])
    # shutil.copyfile(sourceDir, targetDir+'\\'+'change'+str(format(noise,'.2f'))+'.json')
    l = [{"step": 0, "input": zhibiao}]
    with open(targetDir+'\\'+'change'+str(format(noise,'.2f'))+'.json', 'w') as f:
        json.dump(l, f, indent=4, ensure_ascii=False)

def main(sourceDir,targetDir,qishi,buchang,zu,num):
    for i in range(zu):
        noise=qishi+buchang*i
        print(noise)
        # sourceDir = 'D:\\Shared-Input\\output-format.json'
        # targetDir = 'D:\\data\\juece\\robust\\robust'
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)
        change(sourceDir, targetDir, noise,num[i])
# sourceDir = 'E:\\kexinxing\\zhongqi\\juece\\data\\Shared-Input\\output-format.json'
# targetDir = 'E:\\kexinxing\\zhongqi\\juece\\data\\Shared-Input\\output-format_change.json'
# change(sourceDir, targetDir, noise=0.1)
