"""
Locator file
"""
from selenium.webdriver.common.by import By

class WebLocator:
    def __init__(self):
        self.NAME_FILTER_XPATH = '//*[@id="nameTextAccordion"]'
        self.NAME_INPUT_NAME = 'name-text-input'
        self.BIRTHDAY_FILTER_XPATH = '//*[@id="birthdayAccordion"]'
        self.BIRTHDAY_INPUT_NAME = 'birthday-input'
        self.AWARDS_FILTER_XPATH = '//*[@id="awardsAccordion"]'
        self.BEST_ACTOR_XPATH = '//*[@id="accordion-item-awardsAccordion"]/div/section/button[4]'

        self.SEE_RESULTS_BUTTON_XPATH = '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button'

    def clickButton(self, driver, locator):
        driver.find_element(by=By.XPATH, value=locator).click()

    def enterTextbyXpath(self, driver, locator, textValue):
        driver.find_element(by=By.XPATH, value=locator).send_keys(textValue)

    def enterTextbyName(self, driver, locator, textValue):
        driver.find_element(by=By.NAME, value=locator).send_keys(textValue)
