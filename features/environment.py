from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

def before_all(context):
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()

def after_step(context, step):
    context.browser.implicitly_wait(5)
    #sleep(2.5)


def after_all(context):
    context.browser.quit()
