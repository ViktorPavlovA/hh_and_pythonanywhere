from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from random import randint
import yaml
import logging
from logging.handlers import SysLogHandler
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains

class Logger:
    def __init__(self) -> None:
        self.logger = logging.getLogger('Up_myresume')
        self.logger.setLevel(logging.INFO)
        journal_handler = SysLogHandler(address='/dev/log')
        self.logger.addHandler(journal_handler)


class HH_client:
    def __init__(self,config:dict)->None:

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        self.password = config['password']
        self.login = config['login']
        self.resume_numbers = config['resume_numbers']
        self.browser = webdriver.Chrome(options=chrome_options)
        self.logger = Logger()
    
    def click1_with_password(self) -> None:
        """ Enter with password"""
        click_on_it = self.browser.find_element(By.CSS_SELECTOR,"button[data-qa ='expand-login-by-password'][class='bloko-link bloko-link_pseudo']")
        click_on_it.click()
    
    def click2_write_login(self) -> None:
        """ Write login """
        login_input = self.browser.find_element(By.CSS_SELECTOR,"div.bloko-form-item:nth-child(7) > fieldset:nth-child(1) > input:nth-child(1)")
        login_input.clear()
        login_input.send_keys(self.login)

    def click3_write_password(self) -> None:
        """ Write password """
        password = self.browser.find_element(By.CSS_SELECTOR,".bloko-input-text-wrapper_icon-right > input:nth-child(1)")
        password.send_keys(self.password)

    def click4_enter(self) -> None:
        """ Enter """
        enter_button = self.browser.find_element(By.CSS_SELECTOR,".account-login-actions > button:nth-child(1) > span:nth-child(1)")
        enter_button.click()
    def click5_main_page(self) -> None:
        """ Enter to main page"""
        resume_button = self.browser.find_element(By.CSS_SELECTOR,"div.supernova-navi-item_lvl-2:nth-child(2) > a:nth-child(1)")
        resume_button.click()
    def click6_up_resume(self) -> None:
        """ Up resume"""
        for i in range(self.resume_numbers):
            try:
              sleep(randint(1, 2))
              button = self.browser.find_element(By.XPATH,'//button[text()="Поднять в поиске"]')
              self.browser.execute_script("arguments[0].click();", button)
              sleep(randint(1, 2))
              self.logger.logger.warning(f"SUCCESS, 2 UP RESUME NUMBER {i}")
            except Exception as e:
                sleep(randint(1, 2))
                self.logger.logger.error(f"ERROR, 2 UP RESUME NUMBER {i}, {e}")

    def __call__(self) -> None:
        """ Main function"""
        for try_ in range(2):
            self.logger.logger.warning(f"{datetime.now()} Starting up your resume!")
            self.browser.get("https://spb.hh.ru/account/login?backurl=%2F&hhtmFrom=main")
            sleep(randint(1,2))
            self.click1_with_password()
            sleep(randint(1,2))
            self.click2_write_login()
            sleep(randint(1,2))
            self.click3_write_password()
            sleep(randint(1,2))
            self.click4_enter()
            sleep(randint(1,2))
            self.click5_main_page()
            sleep(randint(1,2))
            self.click6_up_resume()
            sleep(randint(1,2))
            self.browser.close()


if __name__ == '__main__':
    with open('./cfg/config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    hh_client = HH_client(config)

    hh_client()