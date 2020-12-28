import argparse
import sys
import json

def validateData(data, keys):
    listOfKeys = data[0].keys()
    ##Test if all dict data has the same key
    for dictionary in data:
        if not dictionary.keys() == listOfKeys:
            return False

    for key in keys:
        if key not in listOfKeys:
            return False
    return True

def processData(inputJson, keys):
    result = {} #create a new dict to hold the result
    it_result = result

    for data in inputJson:
        i = 0
        valuesArray = []
        for currentKey in keys:
            if i+1 < len(keys):
                if data[currentKey] not in it_result:
                    it_result[data[currentKey]] = {}
                it_result = it_result[data[currentKey]]
            i += 1
        for key in data:
            if key not in keys:
                valuesArray.append({key: data[key]})
        it_result[data[currentKey]] = valuesArray
        it_result = result

    return result

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

    jsonIn = [
                      {
                        "country": "US",
                        "city": "Boston",
                        "currency": "USD",
                        "amount": 100
                      },
                      {
                        "country": "FR",
                        "city": "Paris",
                        "currency": "EUR",
                        "amount": 20
                      },
                      {
                        "country": "FR",
                        "city": "Lyon",
                        "currency": "EUR",
                        "amount": 11.4
                      },
                      {
                        "country": "ES",
                        "city": "Madrid",
                        "currency": "EUR",
                        "amount": 8.9
                      },
                      {
                        "country": "UK",
                        "city": "London",
                        "currency": "GBP",
                        "amount": 12.2
                      },
                      {
                        "country": "UK",
                        "city": "London",
                        "currency": "FBP",
                        "amount": 10.9
                      }
                    ]

    keys=["currency","country","city"]

    if validateData(jsonIn, keys):
        result=processData(jsonIn, keys)
        sys.stdout.write(json.dumps(result, indent=2, sort_keys=True))
        sys.stdout.close()
    else:
        print("Error to parse JSON")