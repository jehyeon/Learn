# Delete training data 

ROUTE   = './can-central/primary/contactApp'
GOAL    = 'viv.contactApp.DeleteContact:continue'

def delete(file_name, goal_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            origin = f.read()
        print("open: " + file_name)

        while not origin.find(goal_name) == -1:
            
            point   = origin.find(goal_name)
            start   = origin[:point].rfind('train')
            end     = origin[point:].find('}') + point
            origin  = origin[:start] + origin[end+2:]

        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(origin)

    except:
        print(file_name + "is not exist")

def main():
    for i in range(0, 36):
        if i < 26:
            data_number = chr(97 + i)
        else:
            data_number = str(i - 26)
        file_name = ROUTE + '/resources/ko-KR/training/t-' + data_number + '.training.6t'
        delete(file_name, GOAL)

if __name__ == '__main__':
    main()