import os
import pytest

from selene import browser
from selenium import webdriver as webdriver_selenium
from selenium.webdriver.chrome.options import Options
from dotenv import dotenv_values, load_dotenv
from itdvn_project_tests.controls import attach


@pytest.fixture(scope='session', autouse=True)
def env():
    load_dotenv()


dotenv = dotenv_values()

web_url = dotenv.get('BASE_URL')


def opened_page_website():
    browser.open(web_url)


DEFAULT_BROWSER_VERSION = "114.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='114.0'
    )


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    url = os.getenv('URL')

    driver = webdriver_selenium.Remote(
        command_executor=f"{url}/wd/hub",
        options=options
    )
    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
