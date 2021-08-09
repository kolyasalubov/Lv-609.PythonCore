from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time

def login():
    """Logs into website, creates selenium object driver"""
    print("browser started at: %s" % datetime.now().time())
    driver = webdriver.Chrome("c:\Program Files\Selenium_driver\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://login.iaai.com/")
    time.sleep(1)
    driver.find_element_by_id("Email").send_keys("volodymyrchyk@yahoo.com")
    time.sleep(1)
    driver.find_element_by_id("Password").send_keys("Mamasha1958")
    time.sleep(1)
    driver.find_element_by_tag_name("button").click()
    time.sleep(3)
    return driver

def parse(driver, storinka):
    """Saves innerHTML of the current page into a file with the page number"""
    info = driver.find_element_by_class_name("table-body").get_attribute("innerHTML")
    file = str(storinka) + ".txt"
    with open(file, "w") as h:
        h.write(info)
        print("page %s written into a file" % storinka)

def start(url, driver, storinka):
    """Load the url, returns the number of all pages in the search result, parses the page"""
    print("page 1 at: %s" % datetime.now().time())
    driver.get(url)
    time.sleep(5)
    ActionChains(driver).move_by_offset(752, 609).click().perform()
    time.sleep(3)
    storinky = int(int(driver.find_element_by_id("TotalVehicleAmount").get_attribute("innerHTML").strip())/100)
    time.sleep(2)
    parse(driver, storinka)
    return storinky

def turn(driver, storinka):
    """Parses the page, switches to the next page, returns the number of the current page"""
    storinka += 1
    print("page %s opened at: %s" % (storinka, datetime.now().time()))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element_by_class_name("btn-next").click()
    time.sleep(6)
    parse(driver, storinka)
    return storinka


#buynow url
#url = "https://www.iaai.com/Search?url=lFb3IaERRynXthnECnK8fT1%2bFf5GuXZh3iSqF167eI0%3d"
#engine_damage url
#url = "https://www.iaai.com/Search?url=xr6%2fRrPYIJCI8MwjZ3I8msGMEMaaHSajQnHtkFs07Io%3d"# engine damage
url = "https://www.iaai.com/Search?url=vPTGzfNwmtEbna0CRQf%2fkwuomUIgjLqzA%2b38JO02DFY%3d"# stationary

storinka = 1
driver = login()
storinky = start(url, driver, storinka)
for i in range(storinky):
    storinka = turn(driver, storinka)

driver.close()


