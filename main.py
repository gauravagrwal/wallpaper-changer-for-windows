import requests
import json
import random
import ctypes
import time
from os import path

access_key = 'Paste your ACCESS_KEY here'
url = 'https://api.unsplash.com/search/photos?query=wallpaper&orientation=landscape&client_id=' + access_key
local_path = path.expanduser('~\\Desktop')
walle_path = local_path + '\\wallpaper.jpg'

while True:
    try:
        # getting wallpapers
        wall = requests.get(url)
        json_data = json.loads(wall.text)

        # getting total number of page results
        page = int(json_data['total_pages'])

        # choosing a random page
        random_page = random.randrange(1, page)
        url = url + '&page=' + str(random_page)
        wall = requests.get(url)
        json_data = json.loads(wall.text)

        # selecting a random wallpaper from page
        items = len(json_data['results'])
        selected_item = random.randrange(1, items)
        wallpaper_url = json_data['results'][selected_item]['urls']['full']

        download = requests.get(wallpaper_url)
        open(walle_path, 'wb').write(download.content)

        # now change desktop background
        ctypes.windll.user32.SystemParametersInfoW(20, 0, walle_path, 0)

        # changing wallpaper after every 3 min
        time.sleep(180)
    except:
        print('ERROR!')
        time.sleep(5)