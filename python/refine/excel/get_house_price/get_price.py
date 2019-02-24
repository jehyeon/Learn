import os
import datetime
import openpyxl
import json

DEBUG_MODE = True
RAW_DATAS_FOLDER = './raw_datas/'

# .xlsx data is from http://rtdown.molit.go.kr/rtms/rqs/initRtRentList.do
raw_data_files = os.listdir(RAW_DATAS_FOLDER)
# raw_data_files = ['오피스텔(전월세)_실거래가_20190222.xlsx']      # for test

result = {'datas': []}
for raw_data in raw_data_files:

    try:
        # Active Sheet 얻기
        wb = openpyxl.load_workbook(RAW_DATAS_FOLDER + raw_data)
        ws = wb.active

        # row 데이터 추출
        datas = []
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

        # 데이터 정제
        # 매매 / raw[5]: 전용면적, raw[8]: 거래금액(만원)
        # 전월세 / raw[5]: 전월세 구분, raw[6]: 전용면적, raw[9]: 보증금(만원), raw[10]: 월세(만원)
        prices = {}
        if '매매' in search_opt['실거래 구분']: pr_index, ar_index = 8, 5
        elif '전월세' in search_opt['실거래 구분']: pr_index, ar_index = 9, 6

        for index, raw in enumerate(info[1:]):
            # 월세는 계산 안함
            if raw[5] == '월세': pass
            else:
                area_name = raw[0].split()[1]
                if not area_name in prices.keys():
                    prices[area_name] = []
                try:
                    prices[area_name].append(float(raw[pr_index].replace(',',''))/float(raw[ar_index]))
                
                # 전용면적이 없는 데이터가 있음 (해당 데이터는 미포함)
                except:
                    if DEBUG_MODE:
                        print(index)

        for area_name in prices.keys():
            prices[area_name] = int(sum(prices[area_name])/len(prices[area_name]))
        
        if DEBUG_MODE:
            print(search_opt)
            print(prices)

        result['datas'].append({
            'type': search_opt['실거래 구분'].split('(')[0],
            'period': search_opt['계약일자'],
            'category': search_opt['실거래 구분'].split('(')[1][:-1].replace('월',''),
            'prices': prices
        })

        if DEBUG_MODE:
            print(result['datas'])
    except:
        if DEBUG_MODE:
            print(raw_data)
    
with open('datas.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, sort_keys=True, indent=4)
