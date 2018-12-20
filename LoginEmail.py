# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from details import username, password_user


class LoginEmail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/home/traiana/Desktop/HW_2/QA/testing/chromedriver')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_email_real_credentials(self):
        driver = self.driver
        driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        self.assertIn("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin", driver.current_url)
        
        user = driver.find_element_by_id("identifierId")
        user.click()
        user.clear()
        user.send_keys(username)
        user.send_keys(Keys.ENTER)

        psw = driver.find_element_by_name("password")
        psw.clear()
        psw.send_keys(password_user)
        psw.send_keys(Keys.ENTER)

        logo = driver.find_element_by_id("sdgBod")
        self.assertTrue(logo.is_displayed())

    def test_login_email_wrong_username(self):
        driver = self.driver
        driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        self.assertIn("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin", driver.current_url)
        
        user = driver.find_element_by_id("identifierId")
        user.click()
        user.clear()
        user.send_keys(42)
        user.send_keys(Keys.ENTER)

        with self.assertRaises(NoSuchElementException):
            print("Vsichko e ok")
            psw = driver.find_element_by_name("password")


    def test_login_email_wrong_password(self):
        driver = self.driver
        driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        self.assertIn("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin", driver.current_url)
        
        user = driver.find_element_by_id("identifierId")
        user.click()
        user.clear()
        user.send_keys(username)
        user.send_keys(Keys.ENTER)

        psw = driver.find_element_by_name("password")
        psw.clear()
        psw.send_keys(42)
        psw.send_keys(Keys.ENTER)

        with self.assertRaises(NoSuchElementException):
           logo = driver.find_element_by_id("sdgBod")

    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main(
        defaultTest="LoginEmail.test_login_email_wrong_password")
