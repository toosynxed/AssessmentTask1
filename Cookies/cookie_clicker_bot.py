import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class CookieClickerBot:
    def __init__(self) -> None:
        self.variables_setup()
        self.driver_setup()
        self.open_website()
        time.sleep(1)
        self.data_consent()
        self.choose_language()
        time.sleep(2)
        self.find_elements()


    def variables_setup(self) -> None:
        self.click_frequency = 0.01
        self.stop_clicking = False


    def driver_setup(self) -> None:
        service = Service(executable_path="chromedriver.exe")
        options = Options()
        options.add_experimental_option("detach", True)


        self.driver = webdriver.Chrome(service=service, options=options)


    def open_website(self) -> None:
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")


    def data_consent(self) -> None:
        self.consent_button = self.driver.find_element(By.CLASS_NAME, "fc-button-label")
        self.consent_button.click()


    def choose_language(self) -> None:
        language_button = self.driver.find_element(By.ID, "langSelect-EN")
        language_button.click()


    def find_elements(self) -> None:
        self.cookie_button = self.driver.find_element(By.ID, "bigCookie")
        self.shop = self.driver.find_element(By.ID, "store")
        print(self.shop)

    
    def click_cookie(self):
        while not self.stop_clicking:
            self.cookie_button.click()
            self.find_upgrades()
            time.sleep(self.click_frequency)



    def find_upgrades(self) -> None:
        upper_upgrade_list = self.driver.find_elements(By.CLASS_NAME, "crate.upgrade.enabled")
        if upper_upgrade_list:
            upper_upgrade_list[-1].click()
        upgrades_list = self.driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
        if upgrades_list:
            upgrades_list[-1].click()


    def quit(self) -> None:
        self.stop_clicking = True
        self.driver.quit()