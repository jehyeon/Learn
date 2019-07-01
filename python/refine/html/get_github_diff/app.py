# Get working history from git file diff

from bs4 import BeautifulSoup

LOADFILE = './files.html'       # Default file name when saving html on diff screen (git)
SAVEFILE = './result.txt'

def main():
    # Read File (.html)
    with open(LOADFILE, 'r', encoding='utf8') as f:
        raw_data = f.read()

    # Set soup
    soup = BeautifulSoup(raw_data, 'html.parser')
    
    # Refine datas
    header = [diff for diff in soup.select('.file-info')]
    content = [diff for diff in soup.select('.js-file-content')]
    add_content = []
    ## for additional line
    for index, data in enumerate(content):
        add_content.append('')
        add_content[index] = [a.text.strip() for a in data.find_all('td', {'class': 'blob-code-addition'}) if a.text.strip()]    
        
    lines = [diff.span['aria-label'] for diff in header]
    files = [diff.a.text for diff in header]

    
    # line -> "File renamed without changes" -> int("File") occurs error
    # temporary disabled (ver 1)
    '''
    ## Total line change
    add_line = sum([int(line.split()[0]) for line in lines])
    delete_line = sum([int(line.split()[3]) for line in lines])

    # ver 1
    v1_data = "Total +" + str(add_line) + ", -" + str(delete_line) + '\n'
    v1_data += '\n'.join([file for file in files])
    '''

    # ver 2
    v2_data = {'tr_file' : [], 'tr_line' : [], 'capsule_info' : [], 'code_file' : [], 'code_line' : []}
    for index in range(len(files)):
        if '/capsule.bxb' in files[index]:
            text = ''.join(add_content[index])
            capsule = files[index].split('/')[1]
            capsule += " " + text[text.find('('):text.find(')')+1]
            v2_data['capsule_info'].append(capsule)

        elif '/training/' in files[index]:
            v2_data['tr_file'].append(files[index])
            v2_data['tr_line'].append(lines[index])
        
        else:
            v2_data['code_file'].append(files[index])
            v2_data['code_line'].append(lines[index])

    data = 'git diff list\n\n'
    data += '* capsule version\n'
    data += '\n'.join(v2_data['capsule_info']) + '\n\n'
    data += '* modified file ' + str(len(v2_data['code_file'])) + '\n'
    data += '\n'.join(v2_data['code_file']) + '\n\n'
    data += '* training (TO BE UPDATE)\n'
    data += '\n'.join(v2_data['tr_file'])

    print(data)
    # data = v1_data

    # Save datas
    with open(SAVEFILE, 'w', encoding='utf8') as f:
        f.write(data)

if __name__ == '__main__':
    main()
