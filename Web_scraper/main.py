from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager

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

len_match = len(matches)

title = soup.title.text

file = codecs.open('article_scraping.txt', 'a+')
file.write(title + "\n")
file.write("The following are all instances of your keyword:\n")
count = 1

for i in matches:
    file.write(str(count) + "." + i.get_text() + "\n")
    count += 1

file.write("There were " + str(len_match) + " matches found for the keyword.")
file.close()

driver.quit()
