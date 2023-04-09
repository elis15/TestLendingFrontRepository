import time
import unittest

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By


class searchLendingFront(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("driver/chromedriver.exe")

    def test_consult(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.google.com")
        driver.find_element(By.NAME, "q").send_keys("lendingfront" + keys.Keys.ENTER)
        driver.find_element(By.XPATH,"//h3[contains(text(),'LendingFront | Technology for Business and Consumer Lending')]").click()
        time.sleep(2)
        textCompare = "xxLendingFront’s technology makes extending capital to businesses"
        textElement = driver.find_element(By.XPATH,"//h3[contains(text(),'LendingFront’s technology makes extending capital to businesses')]").text
        self.assertEqual(textCompare,textElement)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()