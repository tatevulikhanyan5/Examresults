"""1. Navigate to https://www.6pm.com/
2. Click on Bags part
3. Click on the Handbags
4. Assert selected tag text under "Your Selections" text
5.* From Sort By DDL select Most Popular"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

drivers = ["chrome", "edge", "firefox"]
driver = webdriver.Firefox()
driver.get("https://www.6pm.com/")
driver.maximize_window()

bag_hover = driver.find_element(By.XPATH, "//a[@href='/c/bags']")
webdriver.ActionChains(driver).move_to_element(bag_hover).perform()
time.sleep(3)

handbags_link = driver.find_element(By.CSS_SELECTOR, "[href='/handbags/COjWARCS1wHiAgIBAg.zso?s=isNew/desc/goLiveDate/desc/recentSalesStyle/desc/']")
handbags_link.click()
time.sleep(3)
element = driver.find_element(By.XPATH, "//ul[@id='searchSelectedFilters']//a[.='Handbags']")
actual_text = element.text
expected_text = "Handbags"
assert expected_text in actual_text, f"nope"
time.sleep(3)
sort_by_ddl = driver.find_element(By.ID, "searchSort")
sort_by_ddl.click()
time.sleep(3)
most_popular_option = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/div/div/div/div[3]/span/div/span/select/option[3]")
most_popular_option.click()

driver.quit()

#good job, but as not with POM, so 35 score