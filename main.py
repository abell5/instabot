from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as bs
import random
import yaml

with open(r'creds.yaml') as file:
    creds = yaml.load(file, Loader=yaml.FullLoader)

driver = webdriver.Chrome(executable_path='/Users/andrew/Documents/workspace/instabot/chromedriver/chromedriver')

driver.get('https://www.instagram.com')

username = creds['username']
password = creds['password']

min_wait_time = 6
max_wait_time = 8

def get_wait_time(min_wait_time,max_wait_time):
    return random.randint(min_wait_time, max_wait_time)	

sleep(get_wait_time(min_wait_time,max_wait_time))

#cookies_popup = driver.find_element_by_class_name("bIiDR")
#cookies_popup.click()

#sleep(get_wait_time(min_wait_time,max_wait_time))

username_input = driver.find_element_by_css_selector("input[name='username']")
password_input = driver.find_element_by_css_selector("input[name='password']")

username_input.send_keys(username)
password_input.send_keys(password)

login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(get_wait_time(min_wait_time,max_wait_time))

profiles = ['stefan_froehlich','thefilmmagazine','nibera_35mm','neilkrug','evazubeck','23h46min','retronyc','f1rstoftheroll','analogue_people','filmphotomag','thomhavlik','magazine35mm','in.film.we.trust','prianalog','film.wave','shootfilmmag']
random.shuffle(profiles)

likes = 1

while likes <= 30:
    for p in profiles:
        driver.get(f'https://www.instagram.com/{p}/')
        
        sleep(get_wait_time(min_wait_time,max_wait_time))
        
        followers = driver.find_element_by_xpath("//a[@href='/{}/followers/']".format(p))
        followers.click()
        
        sleep(get_wait_time(min_wait_time,max_wait_time))
        
        fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
        
        scroll = 0
        while scroll < 10:
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            sleep(1)
            scroll += 1

        fList = [my_elem.get_attribute("href") for my_elem in driver.find_elements_by_xpath("//div[@class='isgrP']//a")]
        fList_unique = list(dict.fromkeys(fList))
        random.shuffle(fList_unique)
        
        for f in fList_unique:
            driver.get(f)
                       
            sleep(get_wait_time(min_wait_time,max_wait_time))
            
            driver.execute_script("window.scrollTo(0, 200);")
            
            sleep(get_wait_time(min_wait_time,max_wait_time))
            
            try:
                pic = driver.find_element_by_class_name("kIKUG")  
                pic.click()
            
                sleep(get_wait_time(min_wait_time,max_wait_time))
                
                like = driver.find_element_by_class_name('fr66n')
                soup = bs(like.get_attribute('innerHTML'),'html.parser')
                if(soup.find('svg')['aria-label'] == 'Like'):
                    like.click()
                    likes+=1
                    print("Like counter: ", likes)
                    
                sleep(get_wait_time(min_wait_time,max_wait_time))               
                
            except:
                print("No pics")
                
            if likes >= 30:
                break
        
            sleep(30)
        

driver.close()

