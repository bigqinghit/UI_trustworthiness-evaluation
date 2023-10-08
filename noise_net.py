import random
import os

def change(sourceDir, targetDir, noise):
    f = open(sourceDir, encoding='gbk')
    txt = []
    for line in f:
        txt.append(line.strip().split('{')[1].split('}')[0])
    all = []
    for i in txt:
        part = []
        for j in range(len(i.split(',')) - 1):
            part.append(float(i.split(',')[j]))
        all.append(part)
    rand = random.sample(all, int(len(all) * noise))
    for m in all[:280]:
        if m in rand:
            for num in range(1, len(m)):
                m[num] = random.choice([m[num] * (1 + noise), m[num] * (1 - noise)])
    with open(targetDir + '\\noise' + str(format(noise, '.2f')) + '.txt', 'w') as g:
        for w in all:
            g.write('{' + str(w) + '}' + '\n')


def main(sourceDir,targetDir,qishi,buchang,zu):
    for i in range(zu):
        noise=qishi+buchang*i
        print(noise)
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)
        change(sourceDir, targetDir, noise)
# sourceDir = 'E:\\kexinxing\\jcdata\\std_input_cpp.txt'
# targetDir = 'E:\\kexinxing\\jcdata\\noise'
# main(sourceDir,targetDir,0.01,0.01,20)
