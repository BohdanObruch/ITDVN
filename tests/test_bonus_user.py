import time
import pytest

from selene import browser, be
from datetime import datetime

from test_examples2 import get_user_info
from tests.conftest import opened_page_website, dotenv
from itdvn_project_tests.helpers.helper import close_advertising
from itdvn_project_tests.controls.utils import resource

user_1_email = dotenv.get('USER_1_Email')
user_1_pass = dotenv.get('USER_1_Password')
user_2_email = dotenv.get('USER_2_Email')
user_2_pass = dotenv.get('USER_2_Password')

user_1 = {
    "Email": user_1_email,
    "Password": user_1_pass}
#
user_2 = {
    "Email": user_2_email,
    "Password": user_2_pass}


@pytest.mark.parametrize("user", [user_1, user_2])
def test_go_to_the_site(user, setup_browser):
    opened_page_website()

    close_advertising()
    old_point = get_user_info(user)

    browser.element('.top-header .itvdnicon-login').click()
    browser.element('#login-form [type="email"]').type(user['Email'])
    browser.element('#login-form [type="password"]').type(user['Password'])
    browser.element('.login-form-element [type="submit"]').click()

    browser.element('.top-header #top-menu-no-avatar-btn').hover()
    browser.element('.top-header #top-menu-user [href="/ua/cabinet"]').click()

    browser.element('.user-info .number[href="/ua/cabinet/bonuses"]').should(be.visible)

    current_datetime = datetime.now().strftime('%d.%m.%y_%H.%M')
    user_name = "user_1" if user == user_1 else "user_2"
    screenshot_filename = f'screenshot_{user_name}_{current_datetime}.png'

    browser.driver.save_screenshot(resource(screenshot_filename))


