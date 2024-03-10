"""main file"""
from DATA import Data
from SEARCHRESULTS import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class IMDbsearch:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)

    def boot(self):
        self.driver.get(Data.WebData().url)
        self.driver.maximize_window()
        self.wait.until(EC.url_to_be(Data.WebData().url))

    def quit(self):
        self.driver.quit()

    def testSearchResults(self):
        try:
            self.boot()
            self.driver.get(Data.WebData().url)
            locator.WebLocator().clickButton(self.driver, locator.WebLocator().NAME_FILTER_XPATH)
            locator.WebLocator().enterTextbyName(self.driver, locator.WebLocator().NAME_INPUT_NAME, Data.WebData().name)

            locator.WebLocator().clickButton(self.driver, locator.WebLocator().BIRTHDAY_FILTER_XPATH)
            locator.WebLocator().enterTextbyName(self.driver, locator.WebLocator().BIRTHDAY_INPUT_NAME, Data.WebData().birthday)

            locator.WebLocator().clickButton(self.driver, locator.WebLocator().AWARDS_FILTER_XPATH)
            locator.WebLocator().clickButton(self.driver, locator.WebLocator().BEST_ACTOR_XPATH)

            locator.WebLocator().clickButton(self.driver, locator.WebLocator().SEE_RESULTS_BUTTON_XPATH)

            assert self.driver.current_url == Data.WebData().resultUrl
            print("Search results are success")
            if self.driver.current_url == Data.WebData().resultUrl:
                print("The search results are matching with result url")
        except NoSuchElementException as e:
            print("Error!")
        finally:
            self.quit()

obj = IMDbsearch()
obj.testSearchResults()


"""
Output: Search results are success
Successfully search the results

"""
