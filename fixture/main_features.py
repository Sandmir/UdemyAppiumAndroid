from time import sleep
from appium.webdriver.common.touch_action import TouchAction


class MainFunc:

    wishlist_xpath = "//android.widget.TextView[@text = 'Wishlist']"
    all_categories_id = "featured_row_categories_recycler_view"
    search_button_id = "action_search"
    feature_carusel_id = "feature_img"
    navigate_up_cont = "Navigate up"
    browse_button_id = "browse_button"
    search_input_id = "search_bar_text"
    courses_id = "discoverCourseBox"
    wishlist_button_id = "wishlist_button"

    item_name_id = "textView4"
    courses_title_id = "featureCourseBoxCourseTitle"
    left_action_id = "left_action"



    def __init__(self, app):
        self.app = app
        self.action = TouchAction(self.app.driver)

    def item_in_list(self, course_name):
        driver = self.app.driver
        action = TouchAction(driver)
        current_page = driver.page_source
        previous_page = ""
        found_course = False
        while current_page != previous_page:
            arr = driver.find_elements_by_id("featureCourseBoxCourseTitle")
            for i in arr:
                if i.text == course_name:
                    our_course = True
                    break
            if found_course: break
            sleep(2)
            action.press(x=500, y=400).move_to(x=500, y=-50).release().perform()
            previous_page = current_page
            current_page = driver.page_source
        return found_course

    def open_wishlist(self):
        self.app.driver.find_element_by_xpath(self.wishlist_xpath).click()

    def go_back_from_search(self):
        self.app.driver.find_element_by_id(self.left_action_id).click()

    def go_back(self):
        self.app.driver.find_element_by_accessibility_id(self.navigate_up_cont).click()

    def scroll_up(self):
        self.action.press(x=500, y=500).move_to(x=500, y=130).release().perform()

    def scroll_down(self):
        self.action.press(x=500, y=500).move_to(x=500, y=-30).release().perform()

    def get_course_name(self):
        return self.app.driver.find_element_by_id(self.item_name_id).text

    def select_first_course(self):
        self.app.driver.find_elements_by_id(self.courses_id)[0].click()

    def search_course(self):
        self.app.driver.find_element_by_id(self.search_button_id).click()
        self.app.driver.find_element_by_id(self.search_input_id).send_keys("Java Script")
        sleep(2)
        self.app.driver.find_elements_by_class_name("android.widget.LinearLayout")[0].click()
        sleep(2)



