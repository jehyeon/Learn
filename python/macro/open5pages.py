# open5pages.py

from bs4 import BeautifulSoup
import webbrowser
import requests
import time

def getSoup(url):
    html = requests.get(url).text.encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    return soup

##### for wemake #####
# 첫 번째 return 값의 href return
def getHref(soup, _text):
    # '.box_listwrap a' : 전체 상품 목록
    for data in soup.select('.box_listwrap a'):
        if _text in data.select('p')[0].text:
            return(data['href'])
    return 'fail'

def main():
    done = False
    count = 0       # 요청 시도 횟수
    want = input("Insert your Item = ")

    while (not done):
        startTime = time.time()
        href = getHref(getSoup('https://front.wemakeprice.com/special/5000195'), want)
        if href == 'fail':
            print('Try \'' + want + '\' ' + str(count) + ' times - ' + str(time.time() - startTime)[:5])
            count += 1
        else:
            done = True

    for i in range(5):
        print('Success access to ' + href)
        if href.find('front') > 0:
            webbrowser.open('http:' + href)
        else:
            webbrowser.open(href)

if __name__ == '__main__':
    main()