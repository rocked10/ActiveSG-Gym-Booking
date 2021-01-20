from selenium.webdriver import Firefox
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import time

# specify file location and initialize driver
firefox_binary = FirefoxBinary(r"C:\Program Files\Mozilla Firefox")
driver = Firefox()


driver.get("https://members.myactivesg.com/bookfacility")


def open_list(elem):
    element = driver.find_element_by_id(f"{elem}_filter_chosen")
    time.sleep(2)
    element.click()


def select_input(text, pos):
    element = driver.find_elements_by_class_name("chosen-search-input")[pos]
    element.send_keys(text)
    element.send_keys(Keys.RETURN)


# Select Activity
open_list("activity")
select_input("Gym", 0)

# Select Location
open_list("venue")
select_input("Choa Chu Kang ActiveSG Gym", 1)


element = driver.find_element_by_id("date_filter").clear()
element = driver.find_element_by_id("date_filter")
element.send_keys("Thu, 22 Jan 2021")


# search
search_button = driver.find_element_by_id("search")
search_button.click()