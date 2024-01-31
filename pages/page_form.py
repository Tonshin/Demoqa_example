from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.pages_locators import PagesLocators as locator
from selenium.webdriver.common.keys import Keys
from data.data import *
import allure
from selenium import webdriver
import os

@allure.feature("Check Page Form")
class PageForm(BasePage):
    def __init__(self, browser, url=None):
        super().__init__(browser, url)
        self.url = 'https://demoqa.com/automation-practice-form'

    @allure.title("Chek inpu first name")
    def input_first_name(self, first_name):
        self.element_is_visible(locator.FIRST_NAME).send_keys(first_name)

    @allure.title("Check input last name")
    def input_last_name(self, last_name):
        self.element_is_visible(locator.LAST_NAME).send_keys(last_name)

    @allure.title("Check input email")
    def input_email(self, email):
        self.element_is_visible(locator.EMAIL).send_keys(email)

    @allure.title("Click gender")
    def click_gender(self):
        self.element_is_visible(locator.GENDER).click()

    @allure.title("Check input number")
    def input_number(self, number):
        self.element_is_visible(locator.NUMBER).send_keys(number)

    @allure.title("Select Date")
    def select_date(self):
        self.element_is_visible(locator.DOB).click()
        self.element_is_visible(locator.MONTH_DOB).click()
        self.element_is_visible(locator.MONTH_CHECK).click()
        self.element_is_visible(locator.YEAR_DOB).click()
        self.element_is_clickable(locator.YEAR_CHECK).click()
        self.element_is_clickable(locator.DATE).click()

    @allure.title("Check input subjects")
    def input_subject(self, subject):
        subjects_input = self.element_is_visible(locator.SUBJECT)
        subjects_input.send_keys(subject)
        subjects_input.send_keys(Keys.ENTER)

    @allure.title("Check select hobbies")
    def select_hobbies(self):
        self.element_is_visible(locator.HOBBIES).click()

    @allure.title("Check input picture")
    def input_picture(self):
        picture_input = self.element_is_clickable(locator.PICTURE_INPUT_BUTTON)
        file = r"C:\Users\1\PycharmProjects\DemoQa\data\Example1.jpg"
        picture_input.send_keys(file)

    @allure.title("Check input address")
    def input_address(self, address):
        self.element_is_visible(locator.ADDRESS).send_keys(address)

    def remove_footer_and_fixeban(self):
        self.remove_footer()
        self.remove_fixeban()

    @allure.title("Select state and city")
    def select_state_and_city(self):
        state_dropdown = self.element_is_clickable(locator.STATE_DROPDOWN_BUTTON)
        self.scroll_into_view_state_and_use_action()
        state_dropdown.click()
        self.element_is_clickable(locator.STATE_VALUE_CHOICE).click()
        city_dropdown = self.element_is_clickable(locator.CITY_DROPDOWN_BUTTON)
        self.scroll_into_view_city_and_use_action()
        city_dropdown.click()
        self.element_is_clickable(locator.CITY_VALUE_CHOICE).click()

    @allure.title("Check submit")
    def click_submit(self):
        submit_button = self.element_is_clickable(locator.SUBMIT)
        self.scroll_into_view_submit_and_use_action()
        submit_button.click()

    def check_the_results(self):

        result_txt = self.element_is_visible(locator.RESULT_TXT).text
        assert result_txt == "Thanks for submitting the form", "Text is not in element"

        student_name_table = self.element_is_visible(locator.STUDENT_NAME_TABLE)
        assert student_name_table.text.strip() == first_name + " " + last_name, "Element is empty"

        email_in_table = self.element_is_visible(locator.EMAIL_IN_TABLE)
        assert email_in_table.text.strip() == email, "Email is empty"

        gender_in_table = self.element_is_visible(locator.GENDER_IN_TABLE)
        assert gender_in_table.text.strip() == "Male", "Gender is empty"

        number_in_table = self.element_is_visible(locator.NUMBER_IN_TABLE)
        assert number_in_table.text.strip() == number, "Number is empty"

        date_in_table = self.element_is_visible(locator.DATE_IN_TABLE)
        assert date_in_table.text.strip() != "", "Date is empty"

        subjects_in_table = self.element_is_visible(locator.SUBJECTS_IN_TABLE)
        assert subjects_in_table.text.strip() == subject, "Subjects is not in table"

        hobbies_in_table = self.element_is_visible(locator.HOBBIES_IN_TABLE)
        assert hobbies_in_table.text.strip() != "", "Hobbies field is empty"

        picture_in_table = self.element_is_visible(locator.PICTURE_IN_TABLE)
        assert picture_in_table.text.strip() != "", "Picture is empty"

        address_in_table = self.element_is_visible(locator.ADDRESS_IN_TABLE)
        assert address_in_table.text.strip() != "", "Address is empty field"

        state_and_city_in_table = self.element_is_visible(locator.STATE_AND_CITY_IN_TABLE)
        assert state_and_city_in_table.text.strip() != "", "State and city is empty field"