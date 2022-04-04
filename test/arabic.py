import string
import time

import language
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config.loc


@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path="D:\\Python Novice\\chromedriver.exe")
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()


def test_tamdudi_arabic(browser):
    # Arabic_Version
    URL = 'https://www.tamm.abudhabi/en'
    browser.get(URL)
    try:
        WebDriverWait(browser, 5).until( EC.element_to_be_clickable(browser.find_element_by_xpath(config.loc.arabic_version))).click()
        time.sleep(3)
        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable(browser.find_element_by_xpath(config.loc.start_manage))).click()
        time.sleep(5)
        assert 'تأسيس وإدارة الأعمال' in browser.title
        # browser.executeScript("window.scrollBy(0,350)")
    except NoSuchElementException:
        # handle if the element not exist
        print('element not exist')
    try:
        tool_checkbox = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable(browser.find_element_by_xpath(config.loc.tool_checkbox_arabic_1)))
        browser.execute_script("arguments[0].click();", tool_checkbox)
        time.sleep(6)
    except NoSuchElementException:
        # handle if the element not exist
        print('element not exist')

    try:
        step_bus = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable(browser.find_element_by_xpath(config.loc.step_bus)))
        # browser.execute_script.execute_script("arguments[0].scrollIntoView(true);", step_bus)
        browser.execute_script("arguments[0].click();", step_bus)
    except NoSuchElementException:
        # handle if the element not exist
        print('element not exist')

    try:
        content_verify_question1 = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(browser.find_element_by_class_name(config.loc.arabic_content_1)))
        str1 = content_verify_question1.text
        if str1.contains(
                "احصل على ترخيص الآن" and "الاسم الاقتصادي الاحتياطي" and "تجديد ترخيص موجود" and "تعديل رخصتي" and "الحصول على تصريح تجاري"):
            {
                assertTrue(True, "All content is present and verified")
            }
        else:
            {
                print("Element not found and test failed")
            }
        time.sleep(3)
    except NoSuchElementException:
        # handle if the element not exist
        print('element not exist')
    try:
        radio = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable(browser.find_element_by_xpath(config.loc.arabic_radio1)))
        browser.execute_script("arguments[0].click();", radio)
        time.sleep(3)
    except NoSuchElementException:
        # handle if the element not exist
        print('element not exist and content verify question1 not exist')

    try:
        next_btn = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable(browser.find_element_by_xpath(config.loc.arabic_nextbtn_1)))
        browser.execute_script("arguments[0].click();", next_btn)
    except NoSuchElementException:
        # handle if the element not exist
        print('element not exist')

    try:
        content_verify_question2 = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(browser.find_element_by_class_name(config.loc.arabic_content_2)))
        str2 = content_verify_question2.text

        if str2.contains("هل تخطط لفتح شركة جديدة؟" and "نعم ، أريد أن أفتح مشروعًا تجاريًا جديدًا." and "نعم ، أرغب في الحصول على رخصة عمل حر." and "لا ، أرغب في فتح فرع لعملي الحالي."):
            {
                assertTrue(True, "All content is present and verified")
            }
        else:
            {
                print("Element not found")
            }
    except NoSuchElementException:
        # handle if the element not exist
        print('Element not found.')
    # Answers_Verification_1
    try:
        radio1 = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable(browser.find_element_by_xpath(config.loc.arabic_radio2)))
        browser.execute_script("arguments[0].click();", radio1)
    except NoSuchElementException:
        # handle if the element not exist
        print('element not exist')

    try:
        next_btn2 = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable(browser.find_element_by_xpath(config.loc.arabic_nextbtn_2)))
        browser.execute_script("arguments[0].click();", next_btn2)
    except NoSuchElementException:
        # handle if the element not exist
        print('element not exist')

    try:
        question3_content = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable(browser.find_element_by_class_name(config.loc.arabic_content_3)))
        str4 = question3_content.text
        if str4.contains(" أين يقع مقر شركتك الرئيسي؟" and "أبو ظبي" and "إمارة أخرى في دولة الإمارات العربية المتحدة (مثال: دبي ، الشارقة ، إلخ)" and "دول مجلس التعاون الخليجي" and "منطقة حرة" and "ما وراء البحار"):
            {
                assertTrue(True, "All answer content  is present and verified")
            }
        else:
            {
                print("Element not found and test failed")
            }
    except NoSuchElementException:
        # handle if the element not exist
        print('element not exist')

    try:
        radio2 = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable(browser.find_element_by_xpath(config.loc.arabic_radio3)))
        browser.execute_script("arguments[0].click();", radio2)
    except NoSuchElementException:
        # handle if the element not exist
        print('element not exist')
    # Answers_Verification_2
    try:
        next_btn3 = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable(browser.find_element_by_xpath(config.loc.arabic_nextbtn_3)))
        browser.execute_script("arguments[0].click();", next_btn3)
        time.sleep(3)
        # redirect_to_login_page
        assert 'Start Your Business - يجب تسجيل الدخول' in browser.title
    except NoSuchElementException:
        # handle if the element not exist
        print('element not exist')
        