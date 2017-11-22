from appium import webdriver

from fixture.main_features import MainFunc
from fixture.session import SessionHelper


class Application:

    def __init__(self):

        # app_dir = os.path.dirname(os.path.abspath(__file__)) + "/../support/com.udemy.android-4.0.4-APK4Fun.com.apk"

        capabilities = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'platformVersion': '7.0',
            'app':"/Privite/Study/Python/UdemyAppiumAndroid/support/com.udemy.android-4.0.4-APK4Fun.com.apk"
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
        self.driver.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.main  = MainFunc(self)




    def destroy(self):
        # self.driver.quit()
        pass


