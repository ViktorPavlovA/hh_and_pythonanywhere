#don't fogget write mail and password in:  if __name__ == '__main__':
#up_our_resume2(browser) < -- if you haven't second resume comment it
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from random import randint

class hh_client:
    def login_hh(self,password,login):
        def click_1(browser):
            """
                                                     CSS_code for example

            <button type="button" data-qa="expand-login-by-password" class="bloko-link bloko-link_pseudo">Войти с&nbsp;паролем</button>


            """
            __click_on_it = browser.find_element(By.CSS_SELECTOR,"button[data-qa ='expand-login-by-password'][class='bloko-link bloko-link_pseudo']")
            __click_on_it.click()
            sleep(randint(1,2))
        def click_and_auth(browser,password,login):
            __login = browser.find_element(By.CSS_SELECTOR,"input[name ='username'][class='bloko-input']")
            __login.clear()
            __login.send_keys(login)
            sleep(randint(1,2))
            __csspassword = browser.find_element(By.CSS_SELECTOR,"input[data-qa ='login-input-password'][class='bloko-input bloko-input_password']")
            __csspassword.clear()
            __csspassword.send_keys(password)
            sleep(randint(1, 2))
            __login_button = browser.find_element(By.CSS_SELECTOR,"button[class ='bloko-button bloko-button_kind-primary'][type='submit'][data-qa='account-login-submit']")
            __login_button.click()
            sleep(randint(1, 2))
        def up_our_resume1(browser):
            __resume_click =browser.find_element(By.CSS_SELECTOR,"a[data-page-analytics-experiment-event ='resume_list_header']")
            __resume_click.click()
            sleep(randint(1, 2))
            __button_up = browser.find_element(By.CSS_SELECTOR,"button[data-qa='resume-update-button'][class='bloko-link']")
            __button_up.click()
            sleep(randint(1, 2))

        def up_our_resume2(browser):
            __resume_click = browser.find_element(By.CSS_SELECTOR,"a[data-page-analytics-experiment-event ='resume_list_header']")
            __resume_click.click()
            sleep(randint(1, 2))
            __button_up = browser.find_element(By.CSS_SELECTOR,"button[class='bloko-button bloko-button_kind-secondary bloko-button_scale-small bloko-button_stretched'][data-qa='resume-update-button']")
            __button_up.click()
            sleep(randint(1, 2))


        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        browser = webdriver.Chrome(options=chrome_options)
        browser.get("https://spb.hh.ru/account/login?backurl=%2F&hhtmFrom=main")
        click_1(browser)
        click_and_auth(browser,password,login)
        up_our_resume1(browser)
        up_our_resume2(browser) #if you have 1 resume comment it with using #
        browser.close()


if __name__ == '__main__':
    #write here your email and password
    loginhh = "email"
    passwordhh = "password"
    hh = hh_client()
    while True:
        for i in range(14400):
            if i%100 ==0:
                print(f"{i}/{14400}")
            sleep(1)
            if i == 14400 - 1:
                try:
                    hh.login_hh(passwordhh, loginhh)
                    print(f"Up resume")
                except:
                    try:
                        hh.login_hh(passwordhh, loginhh)
                    except: pass


