import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selene import browser


def before_all(context):
    if os.environ.get('DOCKER') == "true":
        browser.set_driver(webdriver.Remote(command_executor='http://selenoid:4444/wd/hub',
                                            desired_capabilities={
        "browserName": "chrome",
        "version": "latest",
        'chromeOptions': {
            'args': ['--no-sandbox', '--start-maximized', '--disable-infobars', '--disable-extensions'],
            'prefs': {
                "download.default_directory": "/tmp/downloads",
                "download.prompt_for_download": False,
                'profile.default_content_setting_values.automatic_downloads': 1
            }
        },
        'enableVNC': True,
        'screenResolution': '1920x1080x24'
    }))
        browser.driver().set_window_size(1920, 1080)
        context.session_id = browser.driver().session_id
    elif os.environ.get('DOCKER') == "false":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        browser.set_driver(webdriver.Chrome(chrome_options=chrome_options))
    else:
        if os.environ.get('BROWSER', 'chrome') == "chrome":
            chromedriver = ChromeDriverManager().install()
            browser.set_driver(
                webdriver.Chrome(executable_path=chromedriver, chrome_options=capabilities(context)))
            context.session_id = browser.driver().session_id


def capabilities(context):
    chromeOptions = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": "{}/tmp/downloads".format(os.getcwd()),
        "download.prompt_for_download": False,
        'profile.default_content_setting_values.automatic_downloads': 1
    }
    chromeOptions.add_experimental_option("prefs", prefs)
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--start-maximized")
    chromeOptions.add_argument("--disable-infobars")
    chromeOptions.add_argument("--disable-extensions")
    return chromeOptions

def after_all(context):
    browser.quit_driver()
