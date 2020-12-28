import argparse
import sys
import json


def validateData(data, keys):
    listOfKeys = data[0].keys()
    for dictionary in data:
        if not dictionary.keys() == listOfKeys:
            return False

    for key in keys:
        if key not in listOfKeys:
            return False
    return True

def processData(inputJson, keys):
    result = {}
    it_result = result
    for data in inputJson:
        i = 0
        for currentKey in keys:
            if i+1 < len(keys):
                if data[currentKey] not in it_result:
                    it_result[data[currentKey]] = {}
                it_result = it_result[data.pop(currentKey)]
            else:
                if data.get(currentKey) in it_result:
                        it_result[data.pop(currentKey)].append(data)
                else:
                        it_result[data.pop(currentKey)] = [data]
            i+=1
        it_result = result

    return result

def _not_listed(self, nlevels, data):
        not_listed = []
        for key in data:
            if key not in nlevels:
                not_listed.append({key: data[key]})

        return not_listed


def processInputFile(from_file, file):
    with open(file, 'r') as out:
        out = json.loads(out.read())
    return out

def processInput():
    input_text = ''
    for line in sys.stdin.readlines():
        input_text += line
    json_data = json.loads(input_text)
    return json_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('keys', type=str, nargs='+')
    parser.add_argument('-f',type=str,nargs='?')
    args = parser.parse_args()

    if args.f:
        jsonIn = processInputFile(from_file=True, file=args.f)
    else:
        jsonIn = processInput()

    if validateData(jsonIn, args.keys):
        result=processData(jsonIn, args.keys)
        sys.stdout.write(json.dumps(result, indent=2, sort_keys=True))
        sys.stdout.close()
    else:
        print("Error to parse JSON")