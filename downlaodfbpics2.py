from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import urllib.request
linkphoto = []
print("Enter the Fb username")
item = input()
options = Options()

options.add_argument("--headless")
driver = webdriver.Chrome('E:/chromedriver' )

#we use mbasic so that it will be easier to scrap

driver.get('https://mbasic.facebook.com/')
email= driver.find_element_by_name('email')
email.send_keys('yourfbemail@email.com') #your email address here
password  = driver.find_element_by_name('pass')
password.send_keys('*************') #your password here
login  = driver.find_element_by_name('login')
login.click()
ok  = driver.find_element_by_class_name('bj')
ok.click()
driver.get('https://mbasic.facebook.com/search/top/?q='+ item + '&refid=8&_rdr')
name = driver.find_element_by_class_name('ck')
name.click()
"""links  = driver.find_element_by_css_selector('.cg.e.fcg')
link = links.find_elements_by_class_name('ch')
photo = ""
for l in link:
    if 'photos' in l.get_attribute('href'):
        #print(l.get_attribute('href'))
        photo = l.get_attribute('href')
""" 
photo = ""

#find all the links present in the page

link = driver.find_elements_by_tag_name('a')
for l in link:
    #extracting the first link with photos
    if 'photos?' in l.get_attribute('href'):
        print(l.get_attribute('href'))
        photo = l.get_attribute('href')
        break
        

driver.get(photo)
profile = driver.find_element_by_class_name('cs')
profile.click()
alllinks = driver.find_elements_by_tag_name('a')
count = 0
# open another driver to open all the photo link
driver2 = webdriver.Chrome('E:/chromedriver')
driver2.get('https://mbasic.facebook.com/')
email= driver2.find_element_by_name('email')
email.send_keys('yourfbemail@email.com') #your fb email here
password  = driver2.find_element_by_name('pass')
password.send_keys('*************') #your fb password here
login  = driver2.find_element_by_name('login')
login.click()
ok  = driver2.find_element_by_class_name('bj')
ok.click()
for l in alllinks:
    if 'photo'  in l.get_attribute('href'):
        #print(l.get_attribute('href'))
        b = l.get_attribute('href')
        driver2.get(b)
        view = driver2.find_elements_by_tag_name('a')
        for l in view:
            if 'view_full_size' in l.get_attribute('href'):
                #print(l.get_attribute('href'))
                x = l.get_attribute('href')
                linkphoto.append(x)

driver2.close()
photo =[]
for l in linkphoto:
    driver.get(l)
    z = driver.find_element_by_tag_name('img')
    b = z.get_attribute('src')
    photo.append(b)
count = 1;
os.mkdir(item)
for p in photo:
    urllib.request.urlretrieve(p, item + "/"  + str(count)+".jpg")
    count = count + 1;
driver.close()
          
                
                
                
                
                
                
                        
        