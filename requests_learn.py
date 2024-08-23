import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}
for satrt_num in range(0,250,25):
    url = f'https://movie.douban.com/top250?start={satrt_num}&filter='
    response = requests.get(url=url, headers=headers)
    print(response.status_code)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    all_title = soup.find_all("span",attrs={"class":"title"})
    for title in all_title:
        title_str = title.string
        if '/' not in title_str:
            print(title_str)
