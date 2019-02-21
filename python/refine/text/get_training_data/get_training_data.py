# -*- coding: utf-8 -*-

# Importing packages
from openpyxl import Workbook
import configparser
import os
import datetime

import re

'''
    Use config init
'''

# DEFAULT config file name
CONFIG_FILE = 'config.ini'

APP_FOLDER_ROUTE = './[AppName]'
RESOURCES = '/resources'
LOCALES = 'ko-KR'
TRAINGS = '/training'
SAVE_ROUTE = './datas'

DEBUG_MODE = False

# Make config.ini
def make_config(_config_filename):
    config = configparser.ConfigParser()
    config['DEFAULT']['app_folder'] = APP_FOLDER_ROUTE
    config['DEFAULT']['resources']  = RESOURCES
    config['DEFAULT']['locales']    = LOCALES
    config['DEFAULT']['trainings']  = TRAINGS
    config['DEFAULT']['save_route'] = SAVE_ROUTE

    with open(_config_filename, 'w') as configfile:
        config.write(configfile)

    if DEBUG_MODE: print("Make config.ini is done")

    return config

# Read config.ini
def read_config(_config_filename):
    config = configparser.ConfigParser()
    config.read(_config_filename)

    return config


'''
    Get data
'''

# Load data in one file
def load_datas(_file_name):    
    utterances = []

    with open(_file_name, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.find('utterance') > 0:
                start = line.find('[')
                end = line.rfind('")')
                if end < 0:
                    end = line.rfind(')')
                if DEBUG_MODE: print(line[start:end])
                utterances.append(line[start:end])

    return utterances

# Store each training data
def store_datas(_config):
    _app_folder = _config['DEFAULT']['app_folder']
    _resources  = _config['DEFAULT']['resources']
    _locales    = _config['DEFAULT']['locales']
    _trainings  = _config['DEFAULT']['trainings']

    datas = []

    locales = _locales.split(',')

    for locale in locales:
        # training data number is (0-9, a-z)
        for i in range(0, 36):
            if i < 26:
                data_number = chr(97 + i)
            else:
                data_number = str(i - 26)

            if DEBUG_MODE: print("load file - " + _app_folder + _resources + '/' + locale + _trainings + '/t-' + data_number + '.training.bxb')

            try:     
                datas += load_datas(_app_folder + _resources + '/' + locale + _trainings + '/t-' + data_number + '.training.bxb')
            except:
                if DEBUG_MODE: print("File is none")

    if DEBUG_MODE: print("File load done.")

    return datas

# Save datas
def save_datas(_datas, _save_route):
    # Excel setting
    wb = Workbook()
    wsl = []
    sheet_num = 0
    
    wsl.append(wb.create_sheet('datas', sheet_num))

    for index, data in enumerate(_datas):
        # if DEBUG_MODE: print(sheet_num, 'A' + str(index+1))
        wsl[sheet_num]['A' + str(index+1)] = get_goal(data)
        wsl[sheet_num]['B' + str(index+1)] = data
        wsl[sheet_num]['C' + str(index+1)] = get_nl(data)

    if not os.path.isdir(_save_route):
        os.mkdir(_save_route)
    wb.save(_save_route + '/data.xlsx')

# Refine datas
def get_goal(_utterance):
    return _utterance[_utterance.find(':')+1:_utterance.find(']')]

def get_nl(_utterance):
    goal = _utterance

    excepted_symbols = ['(', ')', '{', '}']
    
    for symbol in excepted_symbols:
        goal = goal.replace(symbol, '')

    while '[' in goal:
        start = goal.find('[')
        end = goal.find(']')
        goal = goal[:start] + goal[end+1:]

    return goal.strip()


'''
    Main process
'''

def main():
    if not os.path.isfile(CONFIG_FILE):
        make_config(CONFIG_FILE)

    config = read_config(CONFIG_FILE)

    save_datas(store_datas(config), config['DEFAULT']['save_route'])
    
if __name__ == "__main__":
    main()