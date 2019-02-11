from __future__ import unicode_literals
from bs4 import BeautifulSoup
import youtube_dl
import requests

def getYoutubeData(search_keyword):
  # Get data from url
  url = 'https://www.youtube.com/'
  search_url = url + 'results?search_query=' + search_keyword
  html = requests.get(search_url).text.encode('utf-8')
  soup = BeautifulSoup(html, 'html.parser')

  # Refine data  
  result_list = []
  for a in soup.find_all('a'):
    if 'title' in a.attrs and 'aria-describedby' in a.attrs:
      result_list.append(a)
  
  return result_list

def main():
  # I will update GUI
  ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192'
    }],
	'nocheckcertificate': True
  }

  # Input search keyword
  keyword = input('keyword: ')
  # input() has a possibility to causes unexpected EOF while parsing, so use raw_input()

  # Remove keyword blink
  keyword = keyword.replace(' ', '')

  result_list = getYoutubeData(keyword)

  # pretty useful print
  number = 1
  for result in result_list:
    print(str(number) + '. ' + result.text)
    print('https://www.youtube.com' + result['href'] + '\n')
    number += 1


  choose = input('What your want: ')
  
  print('https://www.youtube.com' + result_list[int(choose)-1]['href'])
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com' + result_list[int(choose)-1]['href']])
if __name__ == '__main__':
  main()
