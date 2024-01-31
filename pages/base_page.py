from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser, url=None):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def remove_footer(self):
        return self.browser.execute_script("document.getElementsByTagName('footer')[0].remove()")

    def scroll_into_view_state_and_use_action(self):
        state_dropdown = self.element_is_clickable((By.ID, "state"))
        return self.browser.execute_script("arguments[0].scrollIntoView();", state_dropdown)
        actions = ActionChains(self.browser)
        actions.move_to_element(state_dropdown).perform()

    def scroll_into_view_city_and_use_action(self):
        city_dropdown = self.element_is_clickable((By.ID, "city"))
        return self.browser.execute_script("arguments[0].scrollIntoView();", city_dropdown)
        actions = ActionChains(self.browser)
        actions.move_to_element(city_dropdown).perform()

    def remove_fixeban(self):
        js_code_fixedban = "var element = document.getElementById('fixedban'); element.parentNode.removeChild(element);"
        self.browser.execute_script(js_code_fixedban)

    def scroll_into_view_submit_and_use_action(self):
        submit_button = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID, "submit")))
        return self.browser.execute_script("arguments[0].scrollIntoView();", submit_button)
        actions = ActionChains(self.browser)
        actions.move_to_element(submit.button).perform()