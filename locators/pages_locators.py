from selenium.webdriver.common.by import By


class PagesLocators:

    FIRST_NAME = (By.CSS_SELECTOR, "[placeholder='First Name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    EMAIL = (By.ID, "userEmail")
    GENDER = (By.XPATH, "//label[@for='gender-radio-1']")
    NUMBER = (By.XPATH, "//input[@placeholder='Mobile Number']")
    DOB = (By.CSS_SELECTOR, ".react-datepicker__input-container")
    MONTH_DOB = (By.XPATH, "//select[@class='react-datepicker__month-select']")
    MONTH_CHECK = (By.XPATH, "//select[@class='react-datepicker__month-select']/option[@value='5']")
    YEAR_DOB = (By.CSS_SELECTOR, '.react-datepicker__year-select')
    YEAR_CHECK = (By.XPATH, "//div[@class='react-datepicker__year-dropdown-container react-datepicker__year-dropdown-container--select']/select/option[@value='1997']")
    DATE = (By.XPATH, "//div[@aria-label='Choose Tuesday, June 3rd, 1997']")
    SUBJECT = (By.ID, "subjectsInput")
    HOBBIES = (By.CSS_SELECTOR, "#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label")
    PICTURE_INPUT_BUTTON = (By.ID, "uploadPicture")
    ADDRESS = (By.ID, "currentAddress")
    STATE_DROPDOWN_BUTTON = (By.ID, "state")
    STATE_VALUE_CHOICE = (By.XPATH, "//div[@id='state']//div[contains(text(), 'NCR')]")
    CITY_DROPDOWN_BUTTON = (By.ID, "city")
    CITY_VALUE_CHOICE = (By.XPATH, "//div[@id='city']//div[contains(text(), 'Delhi')]")
    SUBMIT = (By.ID, "submit")

    # Locators for asserts

    RESULT_TXT = (By.ID, "example-modal-sizes-title-lg")
    STUDENT_NAME_TABLE = (By.XPATH, "//td[2]")
    EMAIL_IN_TABLE = (By.XPATH, "//tr[2]/td[2]")
    GENDER_IN_TABLE = (By.XPATH, "//tr[3]/td[2]")
    NUMBER_IN_TABLE = (By.XPATH, "//tr[4]/td[2]")
    DATE_IN_TABLE = (By.XPATH, "//tr[5]/td[2]")
    SUBJECTS_IN_TABLE = (By.XPATH, "//tr[6]/td[2]")
    HOBBIES_IN_TABLE = (By.XPATH, "//tr[7]/td[2]")
    PICTURE_IN_TABLE = (By.XPATH, "//tr[8]/td[2]")
    ADDRESS_IN_TABLE = (By.XPATH, "//tr[9]/td[2]")
    STATE_AND_CITY_IN_TABLE = (By.XPATH, "//tr[10]/td[2]")

