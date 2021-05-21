from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='C:\Python\workspace\instabot\chromedriver\chromedriver.exe')

driver.get('https://www.instagram.com')

username = 'andrewlorenphoto'
password = 'DTgQsz00TyYL'

sleep(2)

cookies_popup = driver.find_element_by_class_name("bIiDR")
cookies_popup.click()

sleep(2)

username_input = driver.find_element_by_css_selector("input[name='username']")
password_input = driver.find_element_by_css_selector("input[name='password']")

username_input.send_keys(username)
password_input.send_keys(password)

login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(3)

profiles = ['film.moreno']

likes = 1

while likes <= 1:
    for p in profiles:
        driver.get(f'https://www.instagram.com/{p}/')
        
        sleep(2)
        
        followers = driver.find_element_by_xpath("//a[@href='/{}/followers/']".format(p))
        followers.click()
        
        fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
        
        scroll = 0
        while scroll < 5: # scroll 5 times
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            sleep(1)
            scroll += 1

        fList = [my_elem.get_attribute("href") for my_elem in driver.find_elements_by_xpath("//div[@class='isgrP']//a")]
        fList_unique = list(dict.fromkeys(fList))

        
        #fList  = driver.find_elements_by_xpath("//div[@class='isgrP']//a").get_attribute('href')
        print(fList_unique)
        #for f in fList:
        #    print(f.get_attribute('href'))
    
        #sleep(2)
        
        for f in fList_unique[0:2]:
            driver.get(f)
            sleep(5)
    
        likes+=1

driver.close()

