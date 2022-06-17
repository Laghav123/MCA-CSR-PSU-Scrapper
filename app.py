# doing the needful imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time 

# setting the driver as chromedriver
driver = webdriver.Chrome("/Users/laghavmohan/csr scrapping/pandas trial/chromedriver")

# initilazation website
driver.get("https://csr.gov.in/content/csr/global/master/home/home/csr-spent--psu-vs-non-psu/companies.html?=PSU=4055=FY%202020-21")

# changing the FY
#--------Use this code snippet to change the FY----------#

element = WebDriverWait(driver, 6000).until(
    EC.presence_of_element_located((By.CLASS_NAME, "companyName"))
)

dd = Select(driver.find_element(By.ID, "dropdownFilter"))
dd.select_by_value("FY 2016-17")

# changing the items per page
#--------Use this code snippet to change number of companies shown per page----------#

element = WebDriverWait(driver, 6000).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "companyName"))
)
element = WebDriverWait(driver, 6000).until(
    EC.presence_of_element_located((By.ID, "paginaitonDD"))
)

pp = Select(driver.find_element(By.ID, "paginaitonDD"))
pp.select_by_value("20")


# pressing next button several times
#--------this code snippet is used to press next button several times----------#
#--------it takes you to the page number <last number of the range, 11 in this case>-------#
#--------use this code only when necessary, exp: you won't need it while scraping pages in begining--------#

for i in range(1,11):

    element = WebDriverWait(driver, 6000).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "companyName"))
    )
    
    next_button = WebDriverWait(driver, 6000).until(
        EC.presence_of_element_located((By.CLASS_NAME, "paginationjs-next.J-paginationjs-next"))
    )  
    next_button.click()

# navigating all webpages
#--------this code snippet click to open every companies indivudial page----------#

for i in range(1,5):

    element = WebDriverWait(driver, 6000).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "companyName"))
    )

    companies = driver.find_elements(by = By.CLASS_NAME, value="companyName")


    for company in companies:
        try:
            company.click()
        except:
            pass
  
    next_button = WebDriverWait(driver, 6000).until(
        EC.presence_of_element_located((By.CLASS_NAME, "paginationjs-next.J-paginationjs-next"))
    )  
    next_button.click()

# navigating the last page companies
#--------This code snippet click to open every companies on the page opened after clicking next button last time----------#

element = WebDriverWait(driver, 6000).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "companyName"))
)

companies = driver.find_elements(by = By.CLASS_NAME, value="companyName")


for company in companies:
    try:
        company.click()
    except:
        pass

# exporting the data    
#--------This code scans and save the table on every page opened in the browser----------#

whs = driver.window_handles
for wh in whs:
    try:
        if (wh != driver.current_window_handle):
            driver.switch_to.window(wh)
                
            heading = WebDriverWait(driver, 60000).until(EC.presence_of_element_located((By.ID, "headingText")))
            name = heading.text + ".csv"
            print(name)
                
            element = WebDriverWait(driver, 60000).until(EC.presence_of_element_located((By.CLASS_NAME, "odd-theme")))
            dfs = pd.read_html(driver.page_source)

            dfs[0].to_csv(name)
    except TimeoutError:
        pass