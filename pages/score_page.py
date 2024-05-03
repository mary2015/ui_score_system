import time

import pytest
from selenium.webdriver.common.by import By

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from constants import Constants
from selenium.webdriver.support.ui import Select


class ScorePage:

    def submit_input(self, driver, name, email, score, role):
        driver.find_element(By.ID, "name").send_keys(name)
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "number").send_keys(score)
        role_dropdown = Select(driver.find_element(By.ID, "role"))
        role_dropdown.select_by_value(role)
        submit = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        submit.click()
        time.sleep(1)

    # def submit_invalid_score(self, driver, name, email, score, role):
    #     driver.find_element(By.ID, "name").send_keys(name)
    #     driver.find_element(By.ID, "email").send_keys(email)
    #     driver.find_element(By.ID, "number").send_keys(score)
    #     role_dropdown = Select(driver.find_element(By.ID, "role"))
    #     role_dropdown.select_by_value(role)
    #     submit = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    #     submit.click()

    # def submit_invalid_email(self, driver, name, email, score, role):
    #     driver.find_element(By.ID, "name").send_keys(name)
    #     driver.find_element(By.ID, "email").send_keys(email)
    #     driver.find_element(By.ID, "number").send_keys(score)
    #     role_dropdown = Select(driver.find_element(By.ID, "role"))
    #     role_dropdown.select_by_value(role)
    #     submit = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    #     submit.click()
    #
    # def submit_without_name(self, driver, email, role, score):
    #     driver.find_element(By.ID, "email").send_keys(email)
    #     driver.find_element(By.ID, "number").send_keys(score)
    #     role_dropdown = Select(driver.find_element(By.ID, "role"))
    #     role_dropdown.select_by_value(role)
    #     submit = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    #     submit.click()

    def submit_without_input(self, driver):
        submit = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        submit.click()
        time.sleep(1)
