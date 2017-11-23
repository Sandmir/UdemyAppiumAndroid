from time import sleep


def test_add_item(app):
    driver = app.driver
    app.session.login_email()
    app.main.search_course()
    app.main.select_first_course()
    course_name = app.main.get_course_name()
    app.main.scroll_down()

    actual_mode_wishlist = driver.find_element_by_id(app.main.wishlist_button_id).text
    if actual_mode_wishlist != "Wishlisted":
        driver.find_element_by_id(app.main.wishlist_button_id).click()
        actual_mode_wishlist = driver.find_element_by_id(app.main.wishlist_button_id).text
    assert actual_mode_wishlist == "Wishlisted"

    app.main.scroll_up()
    app.main.go_back()
    app.main.go_back_from_search()
    sleep(1)
    app.session.open_main_menu()
    app.main.open_wishlist()
    found_course = app.main.item_in_list(course_name)
    assert found_course == True, "Course is not on the Wishlist: %s" % course_name


def test_delete_first_item(app):
    driver = app.driver
    app.session.login_email()
    app.session.open_main_menu()
    app.main.open_wishlist()
    app.main.select_first_course()
    course_name = app.main.get_course_name()
    app.main.scroll_down()
    driver.find_element_by_id(app.main.wishlist_button_id).click()
    app.main.scroll_up()
    app.main.go_back()
    found_course = app.main.item_in_list(course_name)
    assert found_course == False, "Course is on the Wishlist: %s" % course_name
