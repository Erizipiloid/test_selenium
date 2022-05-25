import time
import unittest
from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()
driver.set_window_size(1024, 768)

driver.get("https://techstepacademy.com/trial-of-the-stones")
"""
find input_1
"""
driver.execute_script("window.scrollTo(0,500);")
input_1 = driver.find_element(By.ID, "r1Input")
input_1.send_keys('rock')
buttom_1 = driver.find_element(By.ID, "r1Btn")
buttom_1.click()
password_1 = driver.find_element(By.CSS_SELECTOR, '#passwordBanner > h4')
print(password_1.text)

input_2 = driver.find_element(By.ID, "r2Input")
input_2.send_keys(password_1.text)
button_2 = driver.find_element(By.ID, "r2Butn")
button_2.click()
password_2 = driver.find_element(By.CSS_SELECTOR, '#successBanner1 > h4')
print(password_2.text)

driver.execute_script("window.scrollTo(0,1000);")
name_1 = driver.find_element(By.XPATH, '//*/div/div[3]/span/b')
wealth_1 = driver.find_element(By.XPATH, '//*/div/div[3]/span/b/../../p')
name_2 = driver.find_element(By.XPATH, '//*/div/div[4]/span/b')
wealth_2 = driver.find_element(By.XPATH, '//*/div/div[4]/span/b/../../p')
input_3 = driver.find_element(By.ID, 'r3Input')
print(f' name_1 = {name_1.text} name_2 = {name_2.text}')
print(f'wealth_1 = {wealth_1.text} wealth_2 = {wealth_2.text}')

if int(wealth_2.text) > int(wealth_1.text):
    pass
else:
    input_3.send_keys(name_1.text)
    button_3 = driver.find_element(By.ID, 'r3Butn')
    button_3.click()
    answer_2 = driver.find_element(By.CSS_SELECTOR, '#successBanner2 > h4')

    print(answer_2.text)

    driver.execute_script("window.scrollTo(0,1200);")
    driver.find_element(By.ID, 'checkButn').click()
    check_answer = driver.find_element(By.CSS_SELECTOR, '#trialCompleteBanner > h4')
    print(check_answer.text)


