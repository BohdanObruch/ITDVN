from selene import browser, have, be, command

from tests.conftest import dotenv

api_key = dotenv.get('API_KEY')


def close_advertising():
    if browser.element('.cookies-message').matching(be.visible):
        browser.with_(timeout=10).element('.promocode').should(be.visible).perform(command.js.remove)
        browser.with_(timeout=10).element('.cookies-message').should(be.visible).perform(command.js.remove)
        browser.with_(timeout=10).element('#share').should(be.visible).perform(command.js.remove)


def captcha():
    browser.open('chrome-extension://infdcenbdoibcacogknkjleclhnjdmfh/popup/popup.html')
    browser.element('.api-control input').type(api_key)
    browser.element('.api-control button').click()
    browser.element('[data-lang="enabledSolveAutomaticallyOn"]').should(have.text('Automatic captcha solving enabled'))

    browser.driver.switch_to.new_window()
