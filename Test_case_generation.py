import json
import random
import shutil


# read json docunment
def _get_input_fields(in_format_file_path):
    input_fields = []
    with open(in_format_file_path) as f:
        in_format = json.loads(f.read())
        for k, v in in_format.items():
            if type(v) is dict:
                input_fields.append({
                    'name': k,
                    'lval': v['range'][0],
                    'uval': v['range'][1],
                    'type': v['type']
                })
            elif type(v) is list:
                for sk, sv in v[0].items():
                    if type(sv) is dict:
                        input_fields.append({
                            'name': sk,
                            'lval': sv['range'][0],
                            'uval': sv['range'][1],
                            'type': sv['type']
                        })
            else:
                raise Exception('Unsupported type: %s for %s' % (k, type(v)))
    return input_fields


# Randomly generate the value of the variable
def randomnum(path):
    input_fields = _get_input_fields(path)
    for i in range(len(input_fields)):
        if input_fields[i]['type'] == 'int':
            name = input_fields[i]['name']
            input_fields[i][name] = random.randint(input_fields[i]['lval'], input_fields[i]['uval'])
            input_fields[i].pop('name')
            input_fields[i].pop('lval')
            input_fields[i].pop('uval')
            input_fields[i].pop('type')
        elif input_fields[i]['type'] == 'float':
            name = input_fields[i]['name']
            input_fields[i][name] = random.uniform(input_fields[i]['lval'], input_fields[i]['uval'])
            input_fields[i].pop('name')
            input_fields[i].pop('lval')
            input_fields[i].pop('uval')
            input_fields[i].pop('type')
        elif input_fields[i]['type'] == 'bool':
            name = input_fields[i]['name']
            input_fields[i][name] = random.choice([True, False])
            input_fields[i].pop('name')
            input_fields[i].pop('lval')
            input_fields[i].pop('uval')
            input_fields[i].pop('type')
    return input_fields


# Write the value of the randomly generated variable to the json file
def jsonfile(sourceDir, targetDir, input_fields):
    shutil.copyfile(sourceDir, targetDir + '\\' + 'output-format.json')
    with open(targetDir + '\\' + 'output-format.json') as f:
        in_format = json.loads(f.read())
        for k, v in in_format.items():
            if type(v) is dict:
                for i in range(len(input_fields)):
                    for m, n in input_fields[i].items():
                        if m == k:
                            in_format[k] = n
            elif type(v) is list:
                for sk, sv in v[0].items():
                    if type(sv) is dict:
                        for a in range(len(input_fields)):
                            for b, c in input_fields[a].items():
                                if b == sk:
                                    v[0][sk] = c
    l = [{"step": 0, "input": in_format}]
    with open(targetDir + '\\' + 'output-format.json', 'w') as f:
        json.dump(l, f, indent=4, ensure_ascii=False)



# sourceDir = 'input-format.json'
# targetDir = 'E:\\kexinxing\\zhongqi\\juece\\data\\output'
# input_fields = randomnum(sourceDir)
# jsonfile(sourceDir, targetDir, input_fields)
