import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#THIS APP CAN BE TWEAKED TO SEND JOB APPLICATIONS.. BUT FOR NOW IT SAVES THE JOB APPLICATIONS POSTINGS AND IT FOLLOWS THE COMPANIES

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3746510231&f_AL=true&geoId=106670623&keywords=Python%20Developer&location=Rom%C3%A2nia&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true&sortBy=R"
EMAIL = os.environ["mail"]
PASSWORD = os.environ["password"]


chrome_settings = webdriver.ChromeOptions()
chrome_settings.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_settings)
driver.get(url=URL)

sign_in_btn = driver.find_element(By.CSS_SELECTOR, "body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis")
sign_in_btn.click()

time.sleep(2)
username_login = driver.find_element(By.CSS_SELECTOR, "#username")
username_login.send_keys(EMAIL)
password_login = driver.find_element(By.CSS_SELECTOR, "#password")
password_login.send_keys(PASSWORD)
password_login.send_keys(Keys.ENTER)

#find all the job applications on the page
wait = WebDriverWait(driver, 10)
driver.maximize_window()
job_applications_count = len(wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#main > div > div.scaffold-layout__list > div > ul > li'))))
time.sleep(2)

for i in range(job_applications_count):
    job_application = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'#main > div > div.scaffold-layout__list > div > ul > li:nth-child({i+1})')))
    job_application.location_once_scrolled_into_view
    job_application.click()
    time.sleep(3)
    save_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".jobs-save-button")))
    save_btn.click()
    time.sleep(3)
    follow_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".follow")))
    follow_btn.location_once_scrolled_into_view
    follow_btn.click()
    time.sleep(3)

