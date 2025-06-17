import time
from selenium.webdriver.common.by import By
from pages.homepage import Homepage
from pages.product import ProductPage



def test_open_s6(browser):
    homepage = Homepage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')

    # browser.get('https://demoblaze.com/')
    # galaxy_s6 = browser.find_element(By.XPATH , '//a[text()="Samsung galaxy s6"]')  # Исправлено find.element на find_element
    # galaxy_s6.click()
    # title = browser.find_element(By.CSS_SELECTOR, 'h2')
    # assert title.text == 'Samsung galaxy s6'

def test_2_monitors(browser):
    homepage = Homepage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(3)
    homepage.check_products_count(2)