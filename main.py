import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

theEnd = False

def getWordListAndGoToNextPage(driver):
    global theEnd
    master = driver.find_element_by_id("master")
    words = master.find_elements_by_class_name("word")
    for word in words:
        print(word.text)

    if theEnd:
        return False

    pagination = driver.find_element_by_css_selector(".jquery-bootstrap-pagination.pagination")
    links = pagination.find_elements_by_tag_name("a")

    nextPage = links[-1].get_attribute("data-page")
    lastestPage = links[-2].get_attribute("data-page")

    if nextPage == lastestPage:
        theEnd = True

    links[-1].click()
    time.sleep(2)
    return True

def begin():
    # driver = webdriver.PhantomJS()
    driver = webdriver.Firefox()

    driver.get("https://www.shanbay.com/web/account/login/")

    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    username.send_keys("username")
    password.send_keys("password")
    password.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "task-1")))

    driver.get("https://www.shanbay.com/bdc/learnings/library/#master_tab")

    while getWordListAndGoToNextPage(driver):
        pass

    driver.quit()

if __name__ == '__main__':
    begin()

