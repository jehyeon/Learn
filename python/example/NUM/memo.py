# FileName  : Memo.py
# Author    : Lee, Jehyeon

import json
import os
import datetime

def read_data():
    with open('data.json', 'r') as f:
        data = f.read()
    jsonData = json.loads(data)
    return jsonData

def new_data(data, new_data):
    with open('data.json', 'w') as f:
        data['data'].append(new_data) 
        data['count'] = len(data['data'])
        stringData = json.dumps(data, indent=2)
        f.write(stringData)

date_dummy = 'None'

while True:
    memos = read_data()
    print('1. New Memo\n2. View Memo\n3. Exit')
    ans = input("-> ")
        
    if ans == '1':
        insert_data = {}
        insert_data['id'] = memos['count'] + 1

        print("Insert Title: ", end='')
        insert_data['title'] = input()
        print("Insert Content: ", end='')
        insert_data['content'] = input()

        insert_data['history'] = {
            "date": str(datetime.datetime.now()),
            "name": os.getenv('USERNAME')
        }

        # print(insert_data)
        new_data(memos, insert_data)

    elif ans == '2':
        # title과 content만
        for memo in memos['data']:
            print('Title: {0}\nContent: {1}\n'.format(memo['title'], memo['content']))
    
    elif ans == '3':
        break
    else:
        print("PLEASE SELECT 1, 2, 3\n")
        
