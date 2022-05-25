import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class TestMeLesson2(unittest.TestCase):

    def setUp(self) -> None:
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.set_window_size(1024, 768)

    def test_stones(self):
        self.driver.get("https://techstepacademy.com/trial-of-the-stones")

        """
        find input_1 - rock pass bamboo
        """
        self.driver.execute_script("window.scrollTo(0,500);")
        self.driver.find_element(By.ID, "r1Input").send_keys('rock')
        self.driver.find_element(By.ID, "r1Btn").click()
        password_1 = self.driver.find_element(By.CSS_SELECTOR, '#passwordBanner > h4')

        """
        find input_2 - bamboo pass Sucsess!
        """
        self.driver.find_element(By.ID, "r2Input").send_keys(password_1.text)
        self.driver.find_element(By.ID, "r2Butn").click()
        answer_1 = self.driver.find_element(By.CSS_SELECTOR, '#successBanner1 > h4')

        self.assertEqual(answer_1.text, 'Success!')

        """
        Two Merchants find 
        """
        self.driver.execute_script("window.scrollTo(0,1000);")
        name_1 = self.driver.find_element(By.XPATH, '//*/div/div[3]/span/b')
        wealth_1 = self.driver.find_element(By.XPATH, '//*/div/div[3]/span/b/../../p')
        name_2 = self.driver.find_element(By.XPATH, '//*/div/div[4]/span/b')
        wealth_2 = self.driver.find_element(By.XPATH, '//*/div/div[4]/span/b/../../p')
        input_3 = self.driver.find_element(By.ID, 'r3Input')
        button_3 = self.driver.find_element(By.ID, 'r3Butn')

        if int(wealth_2.text) > int(wealth_1.text):
            input_3.send_keys(name_2.text)
        else:
            input_3.send_keys(name_1.text)
            button_3.click()
            answer_2 = self.driver.find_element(By.CSS_SELECTOR, '#successBanner2 > h4')

        self.assertEqual(answer_2.text, 'Success!')

        self.driver.find_element(By.ID, 'checkButn').click()
        check_answer = self.driver.find_element(By.CSS_SELECTOR, '#trialCompleteBanner > h4')

        self.assertEqual(check_answer.text, 'Trial Complete')


    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

