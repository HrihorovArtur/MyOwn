import selene
from selene.api import *
from selene.support.conditions import be
from selenium.webdriver.support.wait import WebDriverWait
from selene.wait import wait_for
from selene.browser import open_url


def open(url):
    selene.browser.open_url(url)

def get_element(selector):
    if '//' in selector:
        return s(by.xpath(selector))
    else:
        return s(selector)

def wait_for_element(selector, visible=True, timeout=20):
    if visible:
        wait_for(get_element(selector), be.visible, timeout=timeout)
    else:
        wait_for(get_element(selector), be.not_(be.visible), timeout=timeout)


def click(selector):
    wait_for_element(selector)
    get_element(selector).click()

def set_field(selector, value):
    wait_for_element(selector)
    get_element(selector).send_keys(value)

def verify_element_contains_text(selector, value):
    wait_for_element(selector)
    assert value in get_element(selector).text, "Element {} do not contains {} text".format(selector, value)
