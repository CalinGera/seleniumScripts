import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from config.settings import *

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver.exe")
driver.get("http://demo.guru99.com/test/radio.html")

class DragAndDrop():

    def testingDragAndDrop(self):

        driver.get(URL)
        driver.maximize_window()

        pathIframe = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(pathIframe)
        
        fromElement = driver.find_element_by_id("draggable")
        toElement = driver.find_element_by_id("droppable")

        action = ActionChains(driver)
        action.drag_and_drop(fromElement, toElement)
        action.perform()

        time.sleep(5)

        print("here")

dragAndDrop = DragAndDrop()
dragAndDrop.testingDragAndDrop()
driver.quit()