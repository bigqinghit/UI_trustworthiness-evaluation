import json
import random
import shutil


def change(sourceDir, targetDir, changeDir, noise):
    with open(sourceDir) as f:
        in_format = json.loads(f.read())
    with open(changeDir) as f:
        in_format_choice = json.loads(f.read())
    zhibiao = in_format[0]['output']
    choice = in_format_choice[0]['output']
    # print(84*float(noise))
    rand = random.sample(zhibiao.keys(), int(len(zhibiao) * float(noise)))
    # print(rand)
    for i in zhibiao:
        if i in rand:
            if zhibiao[i]==None:
                zhibiao[i]=None
            else:
                # choice[i].pop(zhibiao[i])
                zhibiao[i] = random.choice(choice[i])
    # print(zhibiao)
    shutil.copy(sourceDir, targetDir+'\\'+'noise'+str(noise)+'.json')
    l = [{"step": 0, "data_invalid": False, "output": zhibiao}]
    with open(targetDir+'\\'+'noise'+str(noise)+'.json', 'w') as f:
        json.dump(l, f, indent=4, ensure_ascii=False)


def main(qishi,buchang,zu):
    for i in range(zu):
        noise=format(qishi+buchang*i,'.2f')

        sourceDir = 'E:\\kexinxing\\zhongqi\\jiemian5\\data\\juece\\robust\\output_output-format.json'
        targetDir = 'E:\\kexinxing\\zhongqi\\jiemian5\\data\\juece\\robust\\robust'
        changeDir = 'E:\\kexinxing\\zhongqi\\jiemian5\\data\\juece\\data\\output_U1QGX4HJSXGZ_00000000_choice.json'
        change(sourceDir, targetDir, changeDir, noise)

main(0.01,0.01,20)
