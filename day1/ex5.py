import json

def print_choose():
    print("////////////////////////////////////////////////////////////////////\
    \n1. consult my balance\n2. add a new transaction\
    \n3. consult your transaction history\n4. quit\n\nPleas entre your choose")

def load(f):
    with open(f, 'r') as file:
        data = json.load(fp = file)
    return data

def my_credit(data):
    for i in data:
        if i == 'credit':
            print("Your balance is:", data['credit'], "euros\n")

def write_json_data(dict):
    with open('save.json','w') as r:
        json.dump(dict,r)
  
def add_transaction(data):
    liste = {}
    print("Please entre the category of this transaction")
    category = input()
    liste['category'] = category
    print("Please entre the value of this transaction")
    category = input()
    liste['value'] = category
    data.append(liste)
    print("all up to data")
    return(data), int(category)

def history(data):
    date = 1
    for i in data:
        print('\n',date,'.',i['category'],'\n', 'cost:',i['value'])
        date += 1

key = '0'
data = load('save.json')
while key != '4' :
    print_choose()
    key = input()
    if key == '1':
        my_credit(data)
    if key == '2':
        data['transactions'], value = add_transaction(data['transactions'])
        data['credit'] += value
        write_json_data(data)
    if key == '3':
        history(data['transactions'])
    if key == '4' :
        break