import urllib.request
import threading
import time


URLS = ["https://thumbs.static-thomann.de/thumb/padthumb600x600/pics/bdb/_42/428935/12975949_800.jpg", 
        "https://thumbs.static-thomann.de/thumb/thumb80/pics/bdb/_56/567359/18236435_800.jpg", 
        "https://fast-images.static-thomann.de/pics/bdb/_34/349014/13298451_800.jpg"
        ]


def download_image(url):
    filename = url.split("/")[-1]
    urllib.request.urlretrieve(url, filename)
    print(f"Downloaded {filename}")


def download_width_thread():
    threads = []

    start_time = time.time()

    for url in URLS:
        t = threading.Thread(target=download_image, args=(url,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    stop_time = time.time()

    print(f"Time: {start_time - stop_time}")
    return start_time - stop_time


def no_thread():
    t1 = time.time()
    for url in URLS:
        download_image(url)
    t2 = time.time()
    print(f"Time: {t1 - t2}")
    return t1 -t2

if __name__ == "__main__":
    t1 = download_width_thread()
    t2 = no_thread()
    speed = t2/t1
    print(f"\nThreads: {t1},\nWithout: {t2}")
    print(f"Time diff betveen downloading with or without threads: {t1-t2} sec")
    if speed >= 1:
        print(f"Downloading with threads is {speed} times faster")
    else:
        print(f"Downloading without threads is {speed} times slower")