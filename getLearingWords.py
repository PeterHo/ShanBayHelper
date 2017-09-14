import time

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
    master = driver.find_element_by_id("master")
    words = master.find_elements_by_class_name("word")
    for word in words:
        print(str(index) + ". " + word.text + "<br>")
        index += 1

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
    time.sleep(2)
    return True


def begin(username, password):
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

    print('''
<html>
<head>
    <style>
        body {
            margin: 50px;
        }
    </style>
</head>
<body>
    ''')

    while getWordListAndGoToNextPage(driver):
        pass

    print('''
</body>
</html>
    ''')

    driver.quit()
