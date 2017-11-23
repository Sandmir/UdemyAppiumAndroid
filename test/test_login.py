
def test_login_valid_credentials(app):
    app.session.login_email()
    app.session.open_main_menu()
    user_name = app.driver.find_element_by_id(app.session.username_title_id).text
    assert user_name == "Marina Senyutina"


def test_login_invalid_psw(app):
    app.session.login_email(psw='123456')
    error_msg = app.driver.find_element_by_id(app.session.error_psw_snackbar_id).text
    assert error_msg == "Please check your email and password."


def test_login_invalid_username(app):
    app.session.login_email(username='marina@gmail.com')
    error_msg = app.driver.find_element_by_id(app.session.error_psw_snackbar_id).text
    assert error_msg == "Please check your email and password."


def test_signin_button_disable_short_psw(app):
    app.session.login_email(psw='12345')
    sing_button_enable = app.driver.find_element_by_id(app.session.signin_button_id).get_attribute("enabled")
    assert sing_button_enable == 'false'

def test_logout(app):
    app.session.login_email()
    app.session.open_main_menu()
    app.session.logout()
    app.main.submit()
    actual_rez = app.driver.find_element_by_id(app.session.signin_button_id).is_displayed()
    assert actual_rez == True, "User cant't logout"




