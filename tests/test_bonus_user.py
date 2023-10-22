import pytest

from selene import browser, be, have
from datetime import datetime

from tests.conftest import opened_page_website, dotenv
from itdvn_project_tests.helpers.helper import close_advertising, captcha
from itdvn_project_tests.controls.utils import resource
from selene.support.shared.jquery_style import s

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
def test_take_bonus(user, setup_browser):
    captcha()

    opened_page_website()

    close_advertising()

    s('.top-header .itvdnicon-login').click()
    s('#login-form [type="email"]').type(user['Email'])
    s('#login-form [type="password"]').type(user['Password'])
    s('#login-form .captcha-solver-info').should(have.text('Solve with 2Captcha')).click()
    s('#login-form .captcha-solver-info').with_(timeout=60).wait_until(have.exact_text('Captcha solved!'))

    s('.login-form-element [type="submit"]').click()

    s('.top-header #top-menu-no-avatar-btn').hover()
    s('.top-header #top-menu-user [href="/ua/cabinet"]').click()

    s('.user-info .cabinet-before-loading-bg').should(be.not_.visible)
    s('.user-info .number[href*="cabinet/bonuses"]').wait_until(be.clickable)

    current_datetime = datetime.now().strftime('%d.%m.%y_%H.%M')
    user_name = "user_1" if user == user_1 else "user_2"
    screenshot_filename = f'screenshot_{user_name}_{current_datetime}.png'

    browser.driver.save_screenshot(resource(f'resources/{screenshot_filename}'))
