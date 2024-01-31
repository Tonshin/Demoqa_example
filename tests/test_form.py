import time
from pages.page_form import PageForm
from data.data import *


def test_form(browser):

    page_form = PageForm(browser)
    page_form.open()
    page_form.input_first_name(first_name)
    page_form.input_last_name(last_name)
    page_form.input_email(email)
    page_form.click_gender()
    page_form.input_number(number)
    page_form.select_date()
    page_form.input_subject(subject)
    page_form.select_hobbies()
    time.sleep(2)
    page_form.input_picture()
    time.sleep(2)
    page_form.input_address(address)
    page_form.remove_footer_and_fixeban()
    page_form.select_state_and_city()
    page_form.click_submit()
    time.sleep(10)
    page_form.check_the_results()
    time.sleep(10)