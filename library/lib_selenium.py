from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from time import sleep

wait_time = 10


def wait_and_click(driver, xpath, type='xpath'):
    wait = WebDriverWait(driver, wait_time)
    if type == 'xpath':
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, xpath))).click()
    elif type == 'class':
        wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, xpath))).click()


def wait_and_send_keys(driver, xpath, text_input):
    wait = WebDriverWait(driver, wait_time)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath))).send_keys(text_input)


def get_text(driver, xpath, type='xpath'):
    sleep(2)
    try:
        wait = WebDriverWait(driver, wait_time)
        if type == 'xpath':
            return wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath))).text
        elif type == 'class':
            return wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, xpath))).text
    except:
        return None


def is_displayed(driver, xpath):
    wait = WebDriverWait(driver, wait_time)
    return wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath))).is_displayed()


def is_clickable(driver, xpath):
    wait = WebDriverWait(driver, wait_time)
    return wait.until(expected_conditions.element_to_be_clickable((By.XPATH, xpath))).is_enabled()


def wait_and_select(driver, xpath, value, type='xpath'):
    wait = WebDriverWait(driver, wait_time)
    if type == 'id':
        # select_element = wait.until(expected_conditions.visibility_of_element_located((By.ID, xpath)))
        select_element = driver.find_element_by_id(xpath)
    elif type == 'xpath':
        # select_element =  wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
        select_element = driver.find_element_by_xpath(xpath)

    select_sort = Select(select_element)
    select_sort.select_by_value(value)


def text_is_present(driver, var_text):
    text_xpath = "//*[text()='%s']" % var_text
    try:
        driver.find_element_by_xpath(text_xpath)
        return True
    except:
        return False


def get_extra_info(driver):
    try:
        return get_text(driver, "//div[@class = 'context-info']")
    except:
        return None
