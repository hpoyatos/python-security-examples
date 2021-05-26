from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time

firefox = webdriver.Firefox()
firefox.get('https://www.google.com.br')

searchBox = firefox.find_element_by_css_selector(".gLFyf")
searchBox.send_keys("DevOps")
searchBox.send_keys(Keys.RETURN)

time.sleep(5)

link = firefox.find_element_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[1]/a")
link.click()