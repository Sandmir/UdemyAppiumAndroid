from time import sleep
from library.lib_appium import click_button_by_name, scroll_left


def test_scroll_horizontal_main_view_add(app):
    driver = app.driver
    click_button_by_name(driver, "Browse")
    sleep(2)
    list_course = []
    scroll_left(driver)
    count = len(driver.find_elements_by_id("course_name"))
    while count>0:
        course_name = driver.find_elements_by_id("course_name")[0].text
        list_course.append(course_name)
        scroll_left(driver)
        count = len(driver.find_elements_by_id("course_name"))
    assert len(course_name) > 0, "User can't see course adds"

def test_scroll_horizontal_all_category(app):
    driver = app.driver
    click_button_by_name(driver, "Browse")
    sleep(2)
    list_category = []
    category = driver.find_elements_by_id("category_title")
    current_page = driver.page_source
    previous_page = ""
    while current_page != previous_page:
        for item in category:
            if item.text not in list_category:
               list_category.append(item.text)
        scroll_left(driver, y=900)
        previous_page = current_page
        current_page = driver.page_source
    assert len(list_category) > 0, "User can't see any categories"
