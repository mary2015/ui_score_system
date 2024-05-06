import time

from selenium.webdriver.common.by import By


class LoginPage:
    def login(self, driver, user_name, password):
        driver.get("https://spa4h429l.otpyrc.dev/")
        driver.implicitly_wait(3)
        sign_in = driver.find_element(By.CSS_SELECTOR, "body > form:nth-child(3) > button")
        sign_in.click()
        user_name_ele = driver.find_element(By.NAME, "identifier")
        user_name_ele.send_keys(user_name)
        password_ele = driver.find_element(By.NAME, "credentials.passcode")
        password_ele.send_keys(password)
        driver.implicitly_wait(10)
        submit_ele = driver.find_element(By.XPATH, '//*[@id="form20"]/div[2]/input')

        submit_ele.click()
        driver.implicitly_wait(10)
        # okta_submit_ele = driver.find_element(By.NAME, 'credentials.passcode')
        # okta_submit_ele.send_keys(OTP)

        # input("input something")
        time.sleep(10)
        verify_ele = driver.find_element(By.CSS_SELECTOR, '#form63 > div.o-form-button-bar > input')
        print(verify_ele)
        time.sleep(10)
        verify_ele.click()
        time.sleep(10)

    def home_page(self, driver):
        id_ele = driver.find_element(By.XPATH, "//tr[2]/td[2]")
        print(id_ele)
        displayName = driver.find_element(By.XPATH, "//tr[4]/td[2]")
        print(displayName)
        userName = driver.find_element(By.XPATH, "//tr[6]/td[2]")
        print(userName)
        return id_ele.text, displayName.text, userName.text

    def sign_out(self, driver):
        sign_out_ele = driver.find_element(By.XPATH, '/html/body/form[1]/button')
        sign_out_ele.click()
