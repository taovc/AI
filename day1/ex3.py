import json

def load(f):
    with open(f, 'r') as file:
        data = json.load(fp = file)
    return data

class Budget:
    _data = ''
    _transactions = {}
    def __init__(self, path):
        with open(path, 'r') as file:
            Budget._data = json.load(file)

    def get_category(self):
        value_category = []
        for i in Budget._data['transactions']:
            value_category.append(i['category'])
            Budget._transactions[i['category']] = i['value']
        return value_category

    def show_transactions(self, key):
        if key == 'transpot' :
            print "You spend", -Budget._transactions['transpot'], "euros"
        if key == 'salary' :
            print "You received", Budget._transactions['salary'], "euros"

wallet = Budget("1.json")
for i in wallet.get_category():
    print(i)
    wallet.show_transactions(i)
