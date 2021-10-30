import requests
from bs4 import BeautifulSoup

def main():
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }

    url = "https://webfiles.york.ac.uk/OPENAIR/IRs/"
    responses = requests.get(url, headers=headers)
    html = responses.text
    soup = BeautifulSoup(html, 'html.parser')  # 文档对象

    names = []
    for k in soup.find_all('a'):
        href = k['href']
        if href.startswith("?") or href.startswith("/"):
            continue
        if names.__contains__(href):
            continue
        names.append(href[:-1])
    for name in names:
        if "%" in name:
            continue
        download_path = "https://webfiles.york.ac.uk/OPENAIR/IRs/"+name+"/"+name+".zip"
        download(download_path,name)
    pass

def download(url,name):
    r = requests.get(url)
    out_path = "./data/"+name+".zip"
    with open(out_path, 'wb') as f:
        f.write(r.content)

if __name__ == '__main__':
    main()
# download("https://webfiles.york.ac.uk/OPENAIR/IRs/central-hall-university-york/central-hall-university-york.zip")
pass
