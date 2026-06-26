import threading
from concurrent.futures import ThreadPoolExecutor,as_completed
import requests

urls =[

    "https://www.python.org/",
    "https://numpy.org/",
    "https://edition.cnn.com/",
    "https://www.netflix.com/pl/",
    "https://www.youtube.com/"
]

def download_page(url):
    response = requests.get(url,timeout=10)
    response.raise_for_status()
    return url,len(response.text)

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(download_page, url) for url in urls]

    for future in as_completed(futures):
        url, size = future.result()
        print(f"{url} -> {size} znaków")
