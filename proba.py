from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.set_window_size(1024, 768)


# driver.get("https://www.selenium.dev/about/")
# # doc_link = driver.find_element(By.CSS_SELECTOR, '#main_navbar > ul > li:nth-child(4) > a > span')
# doc_link = driver.find_element(By.CSS_SELECTOR, "a[href='/documentation']")
# print(doc_link.text)
#
# doc_link.click()
# print(driver.title)
# print(driver.current_url)

driver.get("https://www.selenium.dev/documentation/")
driver.execute_script("window.scrollTo(0,3000);")

driver.find_element(By.CSS_SELECTOR, 'i[class="fab fa-facebook"]').click()


# driver.close()