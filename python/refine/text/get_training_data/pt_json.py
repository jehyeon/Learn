
def pretty(data):
    
    cla_data = []
    if type(data) == dict:
        data = str(data)

    tab_level = 0
    # print(data)
    for i in data:
        cla_data.append(i)
        if i == '{':
            tab_level += 1
            # print('tab!!')
        if i == '}':
            tab_level -= 1

        if i == '{' or i == ',':
            cla_data.append('\n')
            for tab in range(tab_level):
                cla_data.append('\t')

    return "".join(cla_data)

def test(data):
    cla_data = ''
    for i in data:
        cla_data += i + '\n' + '\n'
        for j in data[i]:
            cla_data += j + '\n'
            if type(data[i][j]) != int:
                for k in data[i][j]:
                    cla_data += '\t' + k + '\n'
            else: cla_data += '\t' + str(data[i][j]) + '\n'
            
            cla_data += '\n'
        cla_data += '\n'
    return cla_data