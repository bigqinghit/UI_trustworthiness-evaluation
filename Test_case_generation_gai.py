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
def randomnum(path,tardir):
    input_fields = _get_input_fields(path)
    input = {}
    select = []
    for i in range(len(input_fields)):
        if input_fields[i]['name'] == 'nTargetDataListNum':
            name = input_fields[i]['name']
            input_fields[i][name] = random.randint(input_fields[i]['lval'], input_fields[i]['uval'])
            input.update({name: input_fields[i][name]})
            select.append(name)
            no1 = input_fields.index({'name': 'bValid', 'lval': 0, 'uval': 1, 'type': 'bool'})
            no2 = input_fields.index({'name': 'fEastPosDL_m', 'lval': -1200, 'uval': 20000, 'type': 'float'})
            input_determine = []
            for value in range(no1, no2 + 1):
                name1 = input_fields[value]['name']
                select.append(name1)
            for j in range(input_fields[i][name]):
                input_single = {}
                for value in range(no1, no2 + 1):
                    if input_fields[value]['type'] == 'int':
                        name = input_fields[value]['name']
                        input_fields[value][name] = random.randint(input_fields[value]['lval'],
                                                                   input_fields[value]['uval'])
                        input_single.update({name: input_fields[value][name]})
                    elif input_fields[value]['type'] == 'float':
                        name = input_fields[value]['name']
                        input_fields[value][name] = random.uniform(input_fields[value]['lval'],
                                                                   input_fields[value]['uval'])
                        input_single.update({name: input_fields[value][name]})
                    elif input_fields[value]['type'] == 'bool':
                        name = input_fields[value]['name']
                        input_fields[value][name] = random.choice([True, False])
                        input_single.update({name: input_fields[value][name]})
                input_determine.append(input_single)
            input.update({"aaTargetData": input_determine})

        elif input_fields[i]['name'] == 'nMslPropertyNum':
            name = input_fields[i]['name']
            input_fields[i][name] = random.randint(input_fields[i]['lval'], input_fields[i]['uval'])
            input.update({name: input_fields[i][name]})
            select.append(name)
            no1 = input_fields.index({'name': 'MslPro_bValid', 'lval': 0, 'uval': 1, 'type': 'bool'})
            no2 = input_fields.index({'name': 'fAFPoleAL_km', 'lval': 0, 'uval': 800, 'type': 'float'})
            input_determine = []
            for value in range(no1, no2 + 1):
                name1 = input_fields[value]['name']
                select.append(name1)
            for j in range(input_fields[i][name]):
                input_single = {}
                for value in range(no1, no2 + 1):
                    if input_fields[value]['type'] == 'int':
                        name = input_fields[value]['name']
                        input_fields[value][name] = random.randint(input_fields[value]['lval'],
                                                                   input_fields[value]['uval'])
                        input_single.update({name: input_fields[value][name]})
                        # select.append(name)
                    elif input_fields[value]['type'] == 'float':
                        name = input_fields[value]['name']
                        input_fields[value][name] = random.uniform(input_fields[value]['lval'],
                                                                   input_fields[value]['uval'])
                        input_single.update({name: input_fields[value][name]})
                        # select.append(name)
                    elif input_fields[value]['type'] == 'bool':
                        name = input_fields[value]['name']
                        input_fields[value][name] = random.choice([True, False])
                        input_single.update({name: input_fields[value][name]})
                        # select.append(name)
                input_determine.append(input_single)
            input.update({"sMslProperty": input_determine})

        elif input_fields[i]['name'] == 'nAIMInfoInfoNum':
            name = input_fields[i]['name']
            input_fields[i][name] = random.randint(input_fields[i]['lval'], input_fields[i]['uval'])
            input.update({name: input_fields[i][name]})
            select.append(name)
            no1 = input_fields.index({'name': 'AIM_bValid', 'lval': 0, 'uval': 1, 'type': 'bool'})
            no2 = input_fields.index({'name': 'fMTDistance', 'lval': 0, 'uval': 20000, 'type': 'float'})
            input_determine = []
            for value in range(no1, no2 + 1):
                name1 = input_fields[value]['name']
                select.append(name1)
            for j in range(input_fields[i][name]):
                input_single = {}
                for value in range(no1, no2 + 1):
                    if input_fields[value]['type'] == 'int':
                        name = input_fields[value]['name']
                        input_fields[value][name] = random.randint(input_fields[value]['lval'],
                                                                   input_fields[value]['uval'])
                        input_single.update({name: input_fields[value][name]})
                        # select.append(name)
                    elif input_fields[value]['type'] == 'float':
                        name = input_fields[value]['name']
                        input_fields[value][name] = random.uniform(input_fields[value]['lval'],
                                                                   input_fields[value]['uval'])
                        input_single.update({name: input_fields[value][name]})
                        # select.append(name)
                    elif input_fields[value]['type'] == 'bool':
                        name = input_fields[value]['name']
                        input_fields[value][name] = random.choice([True, False])
                        input_single.update({name: input_fields[value][name]})
                        # select.append(name)
                input_determine.append(input_single)
            input.update({"sAIMInfo": input_determine})

        elif input_fields[i]['name'] == 'nTargetInListNum':
            name = input_fields[i]['name']
            input_fields[i][name] = random.randint(input_fields[i]['lval'], input_fields[i]['uval'])
            input.update({name: input_fields[i][name]})
            select.append(name)
            no1 = input_fields.index({'name': 'bTargetWpnTypeMatchValid', 'lval': 0, 'uval': 1, 'type': 'bool'})
            no2 = input_fields.index({'name': 'nDLTargetLot', 'lval': 0, 'uval': 8, 'type': 'int'})
            input_determine = []
            for value in range(no1, no2 + 1):
                name1 = input_fields[value]['name']
                select.append(name1)
            for j in range(input_fields[i][name]):
                input_single = {}
                for value in range(no1, no2 + 1):
                    if input_fields[value]['type'] == 'int':
                        name = input_fields[value]['name']
                        input_fields[value][name] = random.randint(input_fields[value]['lval'],
                                                                   input_fields[value]['uval'])
                        input_single.update({name: input_fields[value][name]})
                        # select.append(name)
                    elif input_fields[value]['type'] == 'float':
                        name = input_fields[value]['name']
                        input_fields[value][name] = random.uniform(input_fields[value]['lval'],
                                                                   input_fields[value]['uval'])
                        input_single.update({name: input_fields[value][name]})
                        # select.append(name)
                    elif input_fields[value]['type'] == 'bool':
                        name = input_fields[value]['name']
                        input_fields[value][name] = random.choice([True, False])
                        input_single.update({name: input_fields[value][name]})
                        # select.append(name)
                input_determine.append(input_single)
            input.update({"sTargetInListData": input_determine})

        elif input_fields[i]['name'] == 'nAlarmNum':
            name = input_fields[i]['name']
            input_fields[i][name] = random.randint(input_fields[i]['lval'], input_fields[i]['uval'])
            input.update({name: input_fields[i][name]})
            select.append(name)
            no1 = input_fields.index({'name': 'AlarmInfo_bValid', 'lval': 0, 'uval': 1, 'type': 'bool'})
            no2 = input_fields.index({'name': 'fMisAzi', 'lval': -0.017453, 'uval': 0.017453, 'type': 'float'})
            input_determine = []
            for value in range(no1, no2 + 1):
                name1 = input_fields[value]['name']
                select.append(name1)
            for j in range(input_fields[i][name]):
                input_single = {}
                for value in range(no1, no2 + 1):
                    if input_fields[value]['type'] == 'int':
                        name = input_fields[value]['name']
                        input_fields[value][name] = random.randint(input_fields[value]['lval'],
                                                                   input_fields[value]['uval'])
                        input_single.update({name: input_fields[value][name]})
                        # select.append(name)
                    elif input_fields[value]['type'] == 'float':
                        name = input_fields[value]['name']
                        input_fields[value][name] = random.uniform(input_fields[value]['lval'],
                                                                   input_fields[value]['uval'])
                        input_single.update({name: input_fields[value][name]})
                        # select.append(name)
                    elif input_fields[value]['type'] == 'bool':
                        name = input_fields[value]['name']
                        input_fields[value][name] = random.choice([True, False])
                        input_single.update({name: input_fields[value][name]})
                        # select.append(name)
                input_determine.append(input_single)
            input.update({"sAlarmInfo": input_determine})

        elif input_fields[i]['name'] == 'bIsProCanSelect':
            name = input_fields[i]['name']
            input_determine = []
            for j in range(7):
                name = input_fields[value]['name']
                input_fields[value][name] = random.choice([True, False])
                input_determine.append(input_fields[value][name])
                select.append(name)
            input.update({"bIsProCanSelect": input_determine})

        elif input_fields[i]['name'] == 'bFlame':
            name = input_fields[i]['name']
            input_determine = []
            for j in range(3):
                name = input_fields[value]['name']
                input_fields[value][name] = random.choice([True, False])
                input_determine.append(input_fields[value][name])
                select.append(name)
            input.update({"bFlame": input_determine})

        elif input_fields[i]['name'] == 'nTargetAlloc':
            name = input_fields[i]['name']
            input_determine = []
            for j in range(3):
                name = input_fields[value]['name']
                input_fields[value][name] = random.choice([True, False])
                input_determine.append(input_fields[value][name])
                select.append(name)
            input.update({"nTargetAlloc": input_determine})

        elif input_fields[i]['name'] not in select:
            if input_fields[i]['type'] == 'int':
                name = input_fields[i]['name']
                input_fields[i][name] = random.randint(input_fields[i]['lval'],
                                                       input_fields[i]['uval'])
                select.append(name)
            elif input_fields[i]['type'] == 'float':
                name = input_fields[i]['name']
                input_fields[i][name] = random.uniform(input_fields[i]['lval'],
                                                       input_fields[i]['uval'])
                select.append(name)
            elif input_fields[i]['type'] == 'bool':
                name = input_fields[i]['name']
                input_fields[i][name] = random.choice([True, False])
                select.append(name)
            input.update({name: input_fields[i][name]})
    input1 = [{"step": 0, "input": input}]
    json_str = json.dumps(input1, indent=4)
    with open(tardir+ '\\' + 'output-format.json', 'w') as json_file:
        json_file.write(json_str)
    return input1


# sourceDir = 'input-format.json'
# tardir='E:\\kexinxing\\zhongqi\\juece\\data\\output'
# input1 = randomnum(sourceDir,tardir)
