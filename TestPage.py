from DATA import Data
from SEARCHRESULTS import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import pytest

class Test:
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.quit()

    @pytest.mark.html
    def testTitle(self, boot):
        self.driver.get(Data.WebData().url)
        assert self.driver.title == Data.WebData().searchPageTitle
        print("Success: Page Title is verified")

    @pytest.mark.html
    def searchResult(self, boot):
        self.driver.get(Data.WebData().url)
        locator.WebLocator().clickButton(self.driver, locator.WebLocator().NAME_FILTER_XPATH)
        locator.WebLocator().enterTextbyName(self.driver, locator.WebLocator().NAME_INPUT_NAME, Data.WebData().name)
        locator.WebLocator().clickButton(self.driver, locator.WebLocator().BIRTHDAY_FILTER_XPATH)
        locator.WebLocator().enterTextbyName(self.driver, locator.WebLocator().BIRTHDAY_INPUT_NAME,Data.WebData().birthday)
        locator.WebLocator().clickButton(self.driver, locator.WebLocator().AWARDS_FILTER_XPATH)
        locator.WebLocator().clickButton(self.driver, locator.WebLocator().BEST_ACTOR_XPATH)
        locator.WebLocator().clickButton(self.driver, locator.WebLocator().SEE_RESULTS_BUTTON_XPATH)
        assert self.driver.current_url == Data.WebData().resultUrl
        print("Success the results page is matched")



