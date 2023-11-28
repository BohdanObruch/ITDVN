from selene import browser, have, be, command
from tests.conftest import dotenv

api_key = dotenv.get('API_KEY')


def close_advertising():
    if browser.element('.cookies-message').matching(be.visible):
        if browser.with_(timeout=10).element('.promocode').matching(be.visible):
            browser.with_(timeout=10).element('.promocode').should(be.visible).perform(command.js.remove)
        if browser.with_(timeout=10).element('.cookies-message').matching(be.visible):
            browser.with_(timeout=10).element('.cookies-message').should(be.visible).perform(command.js.remove)
        if browser.with_(timeout=10).element('#share').matching(be.visible):
            browser.with_(timeout=10).element('#share').should(be.visible).perform(command.js.remove)
    if browser.with_(timeout=10).element('.promocode').matching(be.visible):
        browser.with_(timeout=10).element('.promocode').should(be.visible).perform(command.js.remove)


def captcha():
    # browser.open('/')
    # browser.switch_to_tab(0).close_current_tab().switch_to_tab(0)
    browser.open('chrome-extension://ifibfemgeogfhoebkmokieepdoobkbpo/popup/popup.html')

    browser.element('#login-form [name="apiKey"]').type(api_key)
    browser.element('#login-form [data-lang="login"]').click()
    browser.element('[data-lang="enablePlugin"]').wait_until(have.text('ENABLE PLUGIN'))

    browser.driver.switch_to.new_window()
