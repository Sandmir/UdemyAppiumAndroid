from time import sleep


def test_find_course_in_wishlist(app):

    driver = app.driver
    app.session.login_email()
    # check upgrade popup
    if len(driver.find_elements_by_xpath("//android.widget.Button[@text='NOT NOW']"))>0:
        driver.find_elements_by_xpath("//android.widget.Button[@text='NOT NOW']")[0].click()
    app.session.open_main_menu()
    app.main.open_wishlist()
    sleep(2)
    driver.find_element_by_android_uiautomator(
         "new UiScrollable(new UiSelector()).scrollIntoView(text(\"English Punctuation Made Simple!\"));")