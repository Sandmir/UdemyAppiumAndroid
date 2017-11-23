from behave import *

# use_step_matcher("re")


@given('Login with: username "{user}" and psw "{password}"')
def step_impl(context,user, password):
    context.app.session.login_email(user,password)

@then("Go to main menu")
def step_impl(context):
    context.app.session.open_main_menu()


@then('Verify username: "{user}"')
def step_impl(context, user):
    user_name = context.app.driver.find_element_by_id(context.app.session.username_title_id).text
    assert user_name == user


@then('Verify error message "{msg}" is displayed')
def step_impl(context, msg):
    error_msg = context.app.driver.find_element_by_id(context.app.session.error_psw_snackbar_id).text
    assert error_msg == msg


@step("Logout")
def step_impl(context):
    context.app.session.logout()
    context.app.main.submit()

@then('Verify button "Sign in" is displayed')
def step_impl(context):
    actual_rez = context.app.driver.find_element_by_id(context.app.session.signin_button_id).is_displayed()
    assert actual_rez == True, "User cant't logout"