import time
tik = time.perf_counter()
import json
import os
import shutil
import threading
import requests

from requests.exceptions import ConnectionError


try:
    os.mkdir("web-images")
except FileExistsError:
    pass



url_list = []

def downlaoding_pics():

    with open("task.json", "r") as file:
        jsonfile = json.load(file)

        for url_name in jsonfile['items']:
            for url_adress in url_name:
                url_list.append(url_name[url_adress])
    #print(url_list)


    file_name = ''
    count = 1
    for i in url_list:
        file_name = 'pict_' + str(count) + '.jpg'
        try:
            req = requests.get(i, stream=True)

            with open(os.path.join('web-images',file_name), 'wb') as f:
                shutil.copyfileobj(req.raw, f)
                count += 1
        except ConnectionError:
            print("Connection error!!!!")
            break


    if os.path.exists("web-images"):
        if len(os.listdir("web-images")) == 0:
            os.rmdir("web-images")
        else:
            pass
    else:
        print("File not found in the directory:")

thr1 = threading.Thread(target=downlaoding_pics)

thr1.start()
# downlaoding_pics()
tok = time.perf_counter()
timer = tok - tik
print(timer)
