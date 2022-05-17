""" Scrape all inflation rates in BG since tracking by NSI
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("--incognito")  #It loads the chrome driver in incognito mode
options.add_argument("--disable-infobars")
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
  })

driver = webdriver.Chrome('C:\Chromedriver1\chromedriver.exe',options=options )
driver.maximize_window()
driver.get("https://nsi.bg/bg/content/2539/%D0%BA%D0%B0%D0%BB%D0%BA%D1%83%D0%BB%D0%B0%D1%82%D0%BE%D1%80-%D0%BD%D0%B0-%D0%B8%D0%BD%D1%84%D0%BB%D0%B0%D1%86%D0%B8%D1%8F%D1%82%D0%B0")

table = driver.find_element_by_xpath('//*[@id="cpi_calc"]')
all_start_options = []
select = Select(driver.find_element_by_id('start'))
for opt in select.options:
    all_start_options.append(opt.get_attribute("value"))

del all_start_options[0]

for index, elem in enumerate(all_start_options):
    if (index+1 < len(all_start_options) and index - 1 >= 0):

        prev_el = str(all_start_options[index-1])
        curr_el = str(elem)
        next_el = str(all_start_options[index+1])

        select1 = Select(driver.find_element_by_id('start'))
        select1.select_by_value(curr_el)

        select2 = Select(driver.find_element_by_id('end'))
        select2.select_by_value(next_el)

        select3 = Select(driver.find_element_by_id('start'))
        select3.select_by_value(prev_el)

        WebDriverWait(driver, 220).until(
                        EC.visibility_of_element_located((By.XPATH, '//*[@id="result"]/b[2]')))

        inflation = driver.find_element_by_xpath('//*[@id="result"]/b[2]')
        card_log = open('inflation.log', 'a+')
        card_log.write(f"{curr_el} - {next_el} inflation is {inflation.text}\n")
        card_log.close()
