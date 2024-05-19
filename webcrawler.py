import requests
from bs4 import BeautifulSoup
import queue
import datetime

searched_urls = set()
crwlQueue = queue.Queue()

def crawler(url):
    try:
        rqst = requests.get(url)
        soup = BeautifulSoup(rqst.text, "lxml")
        for n in soup.find_all("a"):
            path = n.get("href")
            if "http" not in path:
                prntUrl = url + path
                if len(path) > 2:
                    print(storingUrls(prntUrl))

            elif path in searched_urls:
                continue
            
            else:
                prntUrl = path
                print(storingUrls(prntUrl))

    except Exception:
        print(f"Error occurred crawling:{url}")
        return None

    crawler(crwlQueue.get())

def storingUrls(url):
    crwlQueue.put(url)
    searched_urls.add(url)
    return url
start = datetime.datetime.now()
crawler("https://superuser.com/")
print('Done in: ', datetime.datetime.now() - start, 'seconds.')