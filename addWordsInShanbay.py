import time

import requests
import sys

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

theEnd = False
index = 1


def getWordListAndGoToNextPage(driver):
    global theEnd
    global index
    master = driver.find_element_by_id("learnings-library")
    words = master.find_elements_by_class_name("learning")

    s = requests.Session()
    for c in driver.get_cookies():
        s.cookies.set(c['name'], c['value'])

    for word in words:
        idStr = word.get_attribute("id")
        id = idStr[9:]
        resp = s.put("https://www.shanbay.com/api/v1/bdc/learning/" + id, {"retention": 1})
        # print(idStr, id, resp.text)

    if theEnd:
        return False

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".jquery-bootstrap-pagination.pagination")))

    pagination = driver.find_element_by_css_selector(".jquery-bootstrap-pagination.pagination")
    links = pagination.find_elements_by_tag_name("a")

    nextPage = links[-1].get_attribute("data-page")
    lastestPage = links[-2].get_attribute("data-page")

    if nextPage == lastestPage:
        theEnd = True

    links[-1].click()
    print("page", index)
    index += 1
    time.sleep(2)
    return True


def add(username, password):
    # driver = webdriver.PhantomJS()
    driver = webdriver.Firefox()

    driver.get("https://www.shanbay.com/web/account/login/")

    usernameInput = driver.find_element_by_name("username")
    passwordInput = driver.find_element_by_name("password")

    usernameInput.send_keys(username)
    passwordInput.send_keys(password)
    passwordInput.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "task-1")))

    driver.get("https://www.shanbay.com/bdc/learnings/library/#master_tab")

    while getWordListAndGoToNextPage(driver):
        pass

    driver.quit()


if __name__ == '__main__':
    add(sys.argv[1], sys.argv[2])
