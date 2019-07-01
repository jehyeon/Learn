import json

def main():
  # Read before data
  with open('before.json', 'r', encoding='utf-8') as data:
    json_data = json.load(data)
  
  # Print pretty
  # print(json.dumps(json_data, indent=2, sort_keys=True))

  pages = ['오피스텔(매매)', '오피스텔(전세)', '아파트(매매)', '아파트(전세)']
  period = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']

  converted = []

  for data in json_data['datas']:
    # print('[text]')
    # print(data['type'] + '(' + data['category'] + ')')
    # print(data['period'][:4])
    # print('[index]')
    # print(pages.index(data['type'] + '(' + data['category'] + ')'))
    # print(period.index(data['period'][:4]))

    value = {}
    value['type'] = {}
    value['type']['page'] = pages.index(data['type'] + '(' + data['category'] + ')')
    value['type']['period'] = period.index(data['period'][:4])
    
    prices = [0,]
    for key in data['prices']:
      prices.append(data['prices'][key])

    value['value'] = prices

    # print(value)
    converted.append(value)
  
  # print(json.dumps(converted, indent=2, sort_keys=True))
  with open('after.json', 'w', encoding='utf-8') as make:
    json.dump(converted, make, ensure_ascii=False, indent=2)


if __name__ == '__main__':
  main()