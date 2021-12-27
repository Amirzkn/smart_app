import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import requests
import os
from PIL import Image
import io
import hashlib
import json
options = webdriver.ChromeOptions()  

settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": ""
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
    "isHeaderFooterEnabled": False,
    "mediaSize": {
        "height_microns": 210000,
        "name": "ISO_A5",
        "width_microns": 148000,
        "custom_display_name": "A1"
    },
    "customMargins": {},
    "marginsType": 2,
    "scaling": 175,
    "scalingType": 3,
    "scalingTypePdf": 3,
    "isCssBackgroundEnabled": True
}
prefs = {
   'printing.print_preview_sticky_settings.appState': json.dumps(settings)
}
options.add_experimental_option('prefs', prefs)



options.add_argument("--start-maximized")
options.add_argument("--kiosk")
options.add_argument("user-data-dir=chrome-data") 
wd = webdriver.Chrome(executable_path="/home/amir/Documents/python/selenium_wb/chromedriver",options=options) 

search_url='https://towardsdatascience.com/'       
wd.get(search_url)    
#elements = wd.find_elements_by_class_name('rg_i')
#time.sleep(4)
#wd.find_element_by_tag_name('body').send_keys(Keys.END)
#time.sleep(3)
wd.execute_script('window.print();')
wd.quit()