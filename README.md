# Automating Desktop Wallpaper Changer

## Description:
This program run on the background and change the desktop wallpaper every 2-5 minutes.

## How to run:
Download main.py file and then run:
```
.\venv\Scripts\activate
python main.py   
```
## Tools and Requirements:
* Python 3.10
* PyCharm
* Unsplash API Key (https://unsplash.com/developers)

## Approach:  
I used Python to build this program and for getting images from internet I used the unsplash's API. 
So I used requests, a python's library to get the json data from the API and filtered out the image links, and number of pages.
Then randomly I choose one page and a random wallpaper from the choosen page.
Then with the help of ctypes library SystemParameterInfoW() function is called which is used to change the wallpaper of the desktop.
The interval for changing the wallpaper is set to 3 min (180 sec).
