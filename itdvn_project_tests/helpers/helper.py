from selene import browser, be, command


def close_advertising():
    # browser.with_(timeout=10).element('.promocode').should(be.visible).perform(command.js.remove)
    browser.with_(timeout=10).element('.cookies-message').should(be.visible).perform(command.js.remove)
    # browser.with_(timeout=10).element('#share').should(be.visible).perform(command.js.remove)
