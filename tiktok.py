BenchMarkList = []
DataList = []

from selenium import webdriver
from threading import Timer
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
opts = Options()
PROXY = "37.130.38.21:8080"
opts.add_argument("user-agent=Googlebot")
opts.add_argument(('--proxy-server=%s' % PROXY))

def login(driver, email, password):
    driver.get('https://www.tiktok.com/login/phone-or-email/email?lang=en')
    time.sleep(2)
    # driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "jsx-3665539393", " " ))]').click()
    # time.sleep(8)
    # driver.find_element_by_link_text('Use phone / email / username').click()
    # driver.find_element_by_link_text('Log in with email or username').click()
    # driver.find_element_by_link_text('Sign up with email').click()
    driver.find_element_by_xpath('//input[@placeholder="Email or Username"]').send_keys(email)
    driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys(password)
    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "login-button-86o6Z", " " ))]').click()

PATH = '/Users/adimaggio2021/PycharmProjects/youtube/venv/lib/python3.7/site-packages/selenium/webdriver/chrome/chromedriver'
driver = webdriver.Chrome(PATH, options=opts)
login(driver, 'fobos47233@ainbz.com', 'hillsMountains3344@')

time.sleep(40)

driver.get("https://www.tiktok.com/foryou?lang=en")

def scroll_function():
    driver.execute_script("window.scrollBy(0,600);");



def like(driver):
    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "like", " " ))]').click()

def follow(driver, url):

    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "share-follow", " " ))]').click()


count = 0
while count < 10000:
    time.sleep(1);
    count += 1
    scroll_function()
    if count % 10 == 0:
        element = driver.find_elements_by_css_selector(".event-delegate-mask")
        print(len(element))
        element = element[len(element)-1]
        element2 = driver.find_elements_by_css_selector(".jsx-804431821")
        element2 = element2[len(element2)-1]
        print(element2.text)
        DataList.append(element2.text)
        element.click()
        time.sleep(6)
        print(driver.current_url)
        BenchMarkList.append(driver.current_url)
        like(driver)
        driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "close", " " ))]').click()
#     if count % 25 == 0:
#         driver.findElement(By.cssSelector(".event-delegate-mask")).click()
#         driver.find_element_by_link_text('Copy Link').click()
#         BenchMark = driver.getCurrentUrl()
#         BenchMarkList.append(BenchMark)
#         element.sendKeys(Keys.ESCAPE)
#     if count > 3000:
#         driver.findElement(By.cssSelector(".event-delegate-mask")).click()
#         driver.find_element_by_link_text('Copy Link').click()
#         Data = driver.getCurrentUrl()
#         DataList.append(Data)
#         element.sendKeys(Keys.ESCAPE)
# f = open("data.txt", "w")
#
# for item in DataList:
#     f.write("%s\n" % item)