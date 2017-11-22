import time
import allure



class SessionHelper:

    # describe locators here!!!

    error_email_text = "This email address is not valid"
    error_email_id = "textinput_error"
    error_psw_snackbar_id = "snackbar_text"
    error_psw_snackbar_text = "Please check your email and password."

    signin_button_id = "signin_button"

    username_title_id = "userTitle"
    signout_button_xpath = "//android.widget.TextView[@text = 'Sign out']"

    def __init__(self, app):
        self.app = app

    def login_email(self, username = 'marina_sen@list.ru',psw = 'Portnov12345'):
        driver = self.app.driver
        driver.find_element_by_id(self.signin_button_id).click()
        driver.find_element_by_id("login_with_email").click()
        driver.find_element_by_id("email_edit").send_keys(username)
        driver.find_element_by_id("nextBtn").click()
        driver.find_element_by_id("password").send_keys(psw)
        driver.find_element_by_id(self.signin_button_id).click()

    def open_main_menu(self):
        self.app.driver.find_element_by_accessibility_id("open_drawer").click()
        time.sleep(3)

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_xpath(self.signout_button_xpath).click()

    def forget_psw(self, username=''):
        with allure.step('Forget PSW'):
            driver = self.app.driver
            pass

    def return_to_home_page(self):
        pass

