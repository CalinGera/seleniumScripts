import time
from selenium import webdriver

from config.settings import *

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver.exe")
driver.get("http://demo.guru99.com/test/radio.html")

class TestingRadioButton():

    def selectElements(self, lista):
        for x in lista:
            isSelected = x.is_selected()
            if x.is_selected():
                print("button is selected "+ x.get_attribute("value"))
            else:
                print("button just selected " + x.get_attribute("value"))
                x.click()
                time.sleep(5)


    def RadioButton(self):
        radio = driver.find_elements_by_xpath("//input[@type='radio']")

        self.selectElements(radio)

    def checkBox(self):
        checkbox = driver.find_elements_by_xpath("//input[@type='checkbox']")

        self.selectElements(checkbox)

radio = TestingRadioButton()
radio.RadioButton()

checkbox = TestingRadioButton()
checkbox.checkBox()

driver.quit()
#//input[@type='radio']