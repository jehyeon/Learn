import json

DEBUG_MODE = False

def main():
    # 새로운 파일 타입이 생길 경우 추가 바람
    diffs = {
        'dialogs': [],
        'models': [],
        'trainings': [],
        'views': [],
        'codes': [],
        'others': []
    }

    # 파일 읽기
    with open('diff.txt', 'r', encoding='utf8') as f:
        datas = f.readlines()

    # 데이터 정제
    isFolder = False
    folder_name = ''
    for index, data in enumerate(datas):
        # 빈 값 제거
        if not len(data) == 1:
            # 폴더 이름인 경우 folder_name에 추가            
            if data[0] == ' ':
                if isFolder == True:
                    folder_name += data[1:].replace('\n','/')
                    
                    if DEBUG_MODE: print(folder_name)
                # 다시 폴더 이름인 경우 초기화 (isFolder == False and data[0] == ' ')
                else:
                    folder_name = data[1:].replace('\n','/')
                    isFolder = True

                    if DEBUG_MODE: print('\n<Folder name>\n' + folder_name)

            else:
                # 파일 이름인 경우 isFolder를 False로 변경
                if isFolder == True: isFolder = not(isFolder)
                
                if data[0] == '+': continue

                # 파일 따입에 따라 분류 (필요 시 추가 바람)
                if 'dialog' in data:
                    diffs['dialogs'].append({
                        'file_name': folder_name + data.replace('\n',''),
                        'line_diff': datas[index+1].replace('\n','')
                    })
                elif 'model' in data:
                    diffs['models'].append({
                        'file_name': folder_name + data.replace('\n',''),
                        'line_diff': datas[index+1].replace('\n','')
                    })
                elif 'training' in data:
                    diffs['trainings'].append({
                        'file_name': folder_name + data.replace('\n',''),
                        'line_diff': datas[index+1].replace('\n','')
                    })
                elif 'view' in data:
                    diffs['views'].append({
                        'file_name': folder_name + data.replace('\n',''),
                        'line_diff': datas[index+1].replace('\n','')
                    })
                elif 'js' in data:
                    diffs['codes'].append({
                        'file_name': folder_name + data.replace('\n',''),
                        'line_diff': datas[index+1].replace('\n','')
                    })
                else:
                    diffs['others'].append({
                        'file_name': data.replace('\n',''),
                        'line_diff': datas[index+1].replace('\n','')
                    })


    if DEBUG_MODE:
        print('\n<JSON Pretty>')                                    
        print(json.dumps(diffs, indent=4, sort_keys=True))

    with open('result.txt', 'w', encoding='utf8') as f:
        for key in diffs.keys():

            f.write('\nUpdate ' + key + '\n')
            f.write(str(len(diffs[key])) + ' files' + '\n')

            # line process
            tot_add, tot_minus = 0, 0
            for diff in diffs[key]:
                add, minus = enumerate(diff['line_diff'].split(' '))
                tot_add += int(add[1])
                tot_minus += int(minus[1])

                f.write(diff['file_name'] + '\n')
            
            f.write(str(tot_add) + ' ' + str(tot_minus) + ' lines\n')

if __name__ == '__main__':
    main()