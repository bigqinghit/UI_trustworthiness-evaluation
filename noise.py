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
    rand = random.sample(zhibiao.keys(), int(len(zhibiao) * noise))
    # print(rand)
    for i in zhibiao:
        if i in rand:
            if zhibiao[i]==None:
                zhibiao[i]=None
            else:
                choice[i].pop(zhibiao[i])
                zhibiao[i] = random.choice(choice[i])
    # print(zhibiao)
    shutil.copyfile(sourceDir, targetDir)
    l = [{"step": 0, "data_invalid": False, "output": zhibiao}]
    with open(targetDir, 'w') as f:
        json.dump(l, f, indent=4, ensure_ascii=False)


# sourceDir = 'E:\\kexinxing\\zhongqi\\jiemian4\\data\\juece\\data\\output_U1QGX4HJSXGZ_00000000_1.json'
# targetDir = 'E:\\kexinxing\\zhongqi\\jiemian4\\data\\juece\\data\\output_U1QGX4HJSXGZ_00000000_change_1.json'
# changeDir = 'E:\\kexinxing\\zhongqi\\jiemian4\\data\\juece\\data\\output_U1QGX4HJSXGZ_00000000_choice_1.json'
# change(sourceDir, targetDir, changeDir, noise=0.5)
