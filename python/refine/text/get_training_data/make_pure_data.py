# -*- coding: utf-8 -*-
# FileName  : make_pure_data.py
# Author    : Lee Jehyeon
# Date      : 20180426

import pt_json

# Get goal index, GI is goal index
def getGI(raw_data):
    count = 0
    for ut in raw_data:
        if ut == ']': break
        count += 1

    return count

# Get goal name
def getGoalName(raw_data):
    temp = getGI(raw_data)
    return raw_data[raw_data.find(':')+1:temp]

# pureData is mean utterance
def pureData(raw_data):
    # '(', ')', '{', '}' 기호 삭제
    excepted_symbol = ["(", ")", "{", "}"]
    for i in excepted_symbol:
        raw_data = raw_data.replace(i, "")

    # goal 삭제
    while '[' in raw_data:
        start = raw_data.find('[')
        end = raw_data.find(']')
        raw_data = raw_data[:start] + raw_data[end+1:]

    # 앞 뒤 공백 및 중복 공백 제거
    return " ".join(raw_data.split())

# Get parameters
def getParam(raw_data):
    params = []
    for i in range(getGI(raw_data), len(raw_data)):
        param = ""
        if raw_data[i] == "(":
            done = False
            while (not done):
                param += raw_data[i]
                if raw_data[i] == "]": done = True
                i += 1
        
        for i in range(0,len(params)):
            if params[i] == "": params.pop(i)
        params.append(param)
        
    return params

def makeEasyToReadable(in_dic):
    with open('cla_datas.txt', 'w', encoding="utf-8") as f:
        f.write(pt_json.test(in_dic))
    
    with open('raw_datas.txt', 'w', encoding="utf-8") as f:
        f.write(str(in_dic))
    
    print("Write raw_datas & cla_datas txt")

# Classfying datas
def classifyDatas(raw_datas):
    classified = {}

    # goal별로 파라미터 종류와 갯수 정리
    for raw_data in raw_datas:
        goal_name = getGoalName(raw_data)

        if not goal_name in classified:
            classified[goal_name] = {'count': 0,'param_spec': [], 'yet': [], 'param_count': {}}
        # goal 마다 데이터 개수 
        classified[goal_name]['count'] += 1
        # goal 별 데이터 분류
        classified[goal_name]['yet'].append(raw_data)
        
        for param in getParam(raw_data):
            if not param == '':
                start = param.find(':')
                end = param.rfind(':')
                if start == end:
                    end = param.rfind(']')
                param = param[start+1:end]

                param = param[param.rfind('.')+1:]
                if not param in classified[goal_name]['param_spec']:
                    classified[goal_name]['param_spec'].append(param)
    
    for goal_name in classified.keys():
        param_list = classified[goal_name]['param_spec']
        for data in classified[goal_name]['yet']:
            i_want_go_home = '' 
            for i in range(len(param_list)):
                # print(param_list[i])
                if param_list[i] in data:
                    i_want_go_home += chr(i+65)
            i_want_go_home = ''.join(sorted(i_want_go_home))

            if i_want_go_home == '':
                i_want_go_home = ' '
           
            if not i_want_go_home in list(classified[goal_name]['param_count']):
                classified[goal_name]['param_count'][str(i_want_go_home)] = []
        
            classified[goal_name]['param_count'][str(i_want_go_home)].append(data)    
                
    return classified