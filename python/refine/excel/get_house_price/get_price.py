import os
import datetime
import openpyxl
import json

RAW_DATAS_FOLDER = './raw_datas/'

# .xlsx data is from http://rtdown.molit.go.kr/rtms/rqs/initRtRentList.do
# raw_data_files = os.listdir(RAW_DATAS_FOLDER)
raw_data_files = ['오피스텔(매매)_실거래가_20190211.xlsx']      # for test

result = {}
for raw_data in raw_data_files:
    now = datetime.datetime.now()
    key = '{0}{1}-{2}{3}{4}'.format(now.month, now.day, now.hour, now.minute, now.second)

    # Active Sheet 얻기
    wb = openpyxl.load_workbook(RAW_DATAS_FOLDER + raw_data)
    ws = wb.active

    datas = []
    # row 데이터 추출
    for cols in ws.rows:
        if type(cols) == type(()):
            datas.append([col.value.strip() for col in cols if type(col.value) == str])

    
    search_opt = {}
    info = []           # info[0]: summary / info[1:]: datas
    for data in datas:
        # search option 가져오기
        if len(data) == 1 and ':' in str(data):
            search_opt[data[0].split(':')[0].strip()] = data[0].split(':')[1].strip()
        elif len(data) > 1: info.append(data)
    
    result[key] = {}
    result[key]['search_option'] = search_opt
    result[key]['datas'] = info

    # temp
    temp = {}
    for data in info[1:]:
        try:
            # for check
            if temp[data[0].split(' ')[1]]['tot_price'] == 0:
                pass
        except:
            temp[data[0].split(' ')[1]] = {}
            temp[data[0].split(' ')[1]]['tot_price'] = 0
            temp[data[0].split(' ')[1]]['index'] = 0

        finally:
            temp[data[0].split(' ')[1]]['tot_price'] += float(''.join(data[8].split(','))) / float(data[5])
            temp[data[0].split(' ')[1]]['index'] += 1

    for key in temp.keys():
        print(key + ' ' + str(temp[key]['tot_price'] / temp[key]['index']))

# 나중에 데이터 덮어쓰기가 아닌 업데이트로 수정 예정
# with open('datas.json', 'w', encoding='utf-8') as f:
#     json.dump(result, f)
