from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager

import datetime

import calendar


curr_month= calendar.month_name[datetime.datetime.now().month]
url = 'https://www.rvta.in/monthly-magazine/'
clas = 'vc_btn3-container vc_btn3-center'  # Use '.' to represent multiple classes


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
driver.get(url)
get_url = driver.current_url
wait.until(EC.url_to_be(url))

if get_url == url:
    page_source = driver.page_source

soup = BeautifulSoup(page_source, features='html.parser')
matches = soup.find_all(class_=clas)  # Search for elements with the specified class

title = soup.title.text

file = codecs.open('article_scraping.txt', 'w')
file.write(title + "\n")
file.write("The following are all instances of your keyword:\n")
count = 1

# Initialize a list to store href attributes
href_list = []

for match in matches:
    a_tag = match.find('a')  # Find the first <a> tag within the match
    if a_tag and 'href' in a_tag.attrs:
        href = a_tag['href']  # Get the 'href' attribute
        if '2022' in href and curr_month in href:  # Check if '2022' is present in the href
            file.write(str(count) + "." + a_tag.get_text() + "\n")
            href_list.append(href)
            count += 1

file.write("Href attributes with '2022':\n")
for href in href_list:
    file.write(href + "\n")
file.close()

driver.quit()
