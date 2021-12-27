from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
# useragent = "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36"
# search_query = 'dog'
# search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={search_query}"
# #Firefox
# profile = webdriver.FirefoxProfile("/home/amir/.mozilla/firefox/")
# profile.set_preference("general.useragent.override", useragent)
# options = webdriver.FirefoxOptions()
# options.set_preference("dom.webnotifications.serviceworker.enabled", False)
# options.set_preference("dom.webnotifications.enabled", False)

# browser = webdriver.Firefox(executable_path="/home/amir/Documents/python/selenium_webscrap/geckodriver",firefox_profile=profile,options=options)

# browser.get('http://www.google.com')
# #assert 'google' in browser.title

# elem = browser.find_element_by_name('p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)

# browser.quit()


def search_google(search_query):
    options = webdriver.FirefoxOptions()
    #options.add_argument('--headless')
    browser = webdriver.Firefox(executable_path="/home/amir/Documents/python/selenium_webscrap/geckodriver",options=options)
    search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={search_query}"
    images_url = []

    # open browser and begin search
    browser.get(search_url)
    elements = browser.find_elements_by_class_name('rg_i')
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    count = 0
    for e in elements:
        # get images source url
        e.click()
        time.sleep(3)
        element = browser.find_elements_by_class_name('v4dQwb')

        # Google image web site logic
        if count == 0:
            big_img = element[0].find_element_by_class_name('n3VNCb')
        else:
           big_img = element[1].find_element_by_class_name('n3VNCb')

        images_url.append(big_img.get_attribute("src"))

        # write image to file
        try:
            reponse = requests.get(images_url[count])
            
            if reponse.status_code == 200:
                with open(f"./result/search{count+1}.jpg","wb") as file:
                    file.write(reponse.content)

            count += 1
            print("Image Downloaded number:",count)
        except:
            count += 1
            print("Error")

        # Stop get and save after 5
        if count == 200:
            break

    return images_url

items = search_google('dog')
