import time

from behave import when, given, then

from web.web import *


@given('Navigate to google')
def step_definition(context):
    open('https://www.google.com.ua')


@when('I fill "{text}" text in search field')
def step_definition(context, text):
    set_field('.gLFyf.gsfi', text)


@when('I click on "Search" button')
def step_definition(context):
    click('ul>li:nth-child(1)[data-view-type="1"]')
    time.sleep(10)

@then('I should see "{article}" article')
def step_definition(context, article):
    verify_element_contains_text('//div[contains(text(),"{}")]'.format(article), article)
