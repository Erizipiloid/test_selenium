import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestMeLesson(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1024, 768)

    def test_first(self):
        self.driver.get("https://www.selenium.dev/about/")
        doc_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/documentation']")
        self.assertEqual(doc_link.text, 'Documentation')
        doc_link.click()
        self.assertEqual(self.driver.title, 'The Selenium Browser Automation Project | Selenium')
        self.assertEqual(self.driver.current_url, 'https://www.selenium.dev/documentation/')

    def test_second(self):
        self.driver.get("https://www.selenium.dev/documentation/")
        self.driver.execute_script("window.scrollTo(0,2500);")

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()



