from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pytest
import pytest_html
''''
Test case is step by step instructions for a tester to verify a software or web appliccation

step-01: Open chrome browser
step-02: Navigate to https://passport.alibaba.com/icbu_login.htm?tracelog=hd_signinhttps://passport.alibaba.com/icbu_login.htm?tracelog=hd_signinhttps://passport.alibaba.com/icbu_login.htm?tracelog=hd_signin
step-03: Enter incorrect user name/online id
step-04: Enter incorrect password
step-05: Click on sign in button
step-06: print title
step-07: print current URL
step-08: close the browser

Test result: pass

'''

class Test_Alibaba:
    @pytest.fixture()
    @pytest.mark.regression
    def test_setup(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://passport.alibaba.com/icbu_login.htm?tracelog=hd_signinhttps://passport.alibaba.com/icbu_login.htm?tracelog=hd_signinhttps://passport.alibaba.com/icbu_login.htm?tracelog=hd_signin")
        self.driver.maximize_window()
        time.sleep(10)

        yield

        self.driver.close()
        self.driver.quit()
        print("Test Successful")

    @pytest.mark.regression
    def test_alibabaLogin(self, test_setup):
        self.driver.find_element(By.NAME, "loginId").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(10)
        self.driver.find_element(By.ID,"fm-login-submit").click()
        time.sleep(50)
        print("The title is: ", self.driver.title)



    @pytest.mark.smoke
    def test_alibabaLogin02(self, test_setup):
        self.driver.find_element(By.NAME, "loginId").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "fm-login-submit").click()
        time.sleep(10)
        print("The title is: ", self.driver.title)


    @pytest.mark.skip(reason="All smoke test under skip")
    @pytest.mark.smoke
    def test_alibabaoginFunction03(self, test_setup):
        self.driver.find_element(By.NAME, "loginId").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "fm-login-submit").click()
        time.sleep(10)
        print("Mahi")
        print("The title is: ", self.driver.title)

    @pytest.mark.skip(reason="All smoke test under skip")
    @pytest.mark.smoke
    def test_alibabaLoginFunction04(self, test_setup):
        self.driver.find_element(By.NAME, "loginId").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "fm-login-submit").click()
        time.sleep(10)
        print("The title is: ", self.driver.title)

    #@pytest.mark.skip(reason="All smoke test under skip")
    @pytest.mark.smoke
    def test_AlibabaLoginFunction05(self, test_setup):
        self.driver.find_element(By.NAME, "loginId").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "fm-login-submit").click()
        time.sleep(10)
        print("Mahi")
        print("The title is: ", self.driver.title)
        print("Current URL: ", self.driver.current_url)


    @pytest.mark.regression
    def test_AlibabaLoginFunction06(self, test_setup):
        self.driver.find_element(By.NAME, "loginId").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "fm-login-submit").click()
        time.sleep(10)
        print("The title is: ", self.driver.title)
        print("Current URL: ", self.driver.current_url)

    @pytest.mark.regression
    def test_alibabaLoginFunction07(self, test_setup):
        self.driver.find_element(By.NAME, "loginId").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "fm-login-submit").click()
        time.sleep(10)

        print("The title is: ", self.driver.title)
        print("Current URL: ", self.driver.current_url)

    @pytest.mark.skip(reason="All smoke test under skip")
    @pytest.mark.smoke
    def test_alibabaLoginFunction08(self, test_setup):
        self.driver.find_element(By.NAME, "loginId").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "fm-login-submit").click()
        time.sleep(10)
        print("Mahi")
        print("The title is: ", self.driver.title)
