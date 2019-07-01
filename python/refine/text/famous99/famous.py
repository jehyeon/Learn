import json

def main():
    result = {}
    result['data'] = []

    # Read data
    with open('99.txt', 'r', encoding="utf-8") as f:
        # Split each quote
        # raw_datas is list
        raw_datas = f.readlines()
    
    # Make useful
    for raw_data in raw_datas:
        # 0: quote, 1: person
        raw_data = raw_data.split(' – ')

        temp = {}

        temp['quote'] = raw_data[0]
        # Remove '\n'
        temp['person'] = raw_data[1].replace('\n', '')

        result['data'].append(temp)
    
    with open('result.json', 'w', encoding="utf-8") as f:
        f.write(json.dumps(result))

if __name__ == "__main__":
    main()
