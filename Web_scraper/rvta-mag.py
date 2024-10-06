from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import calendar
import requests
import time
import os


def setter():
    global url,curr_month,clas,curr_year,save_path
    curr_month = calendar.month_name[datetime.datetime.now().month]
    url = 'https://www.rvta.in/monthly-magazine/'
    clas = 'vc_btn3-container vc_btn3-center'
    curr_year= str(datetime.datetime.now().year-1)
    save_path = '/home/ma1581/Documents/placement/current-affairs/'+curr_year+'-'+curr_month+'.pdf'

def check_if_file_already_downloaded():
    if  os.path.exists(save_path):
        exit()


def set_webdriver_config():
    global get_url,driver
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Add this line to run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(driver, 2)
    driver.get(url)
    get_url = driver.current_url
    wait.until(EC.url_to_be(url))

def check_if_page_loaded():
    global page_source
    if get_url == url:
        page_source = driver.page_source


def srch_key_class():
    global matches
    soup = BeautifulSoup(page_source, features='html.parser')
    matches = soup.find_all(class_=clas)  # Search for elements with the specified class

def match_pattern():
    for match in matches:
        a_tag = match.find('a')  # Find the first <a> tag within the match
        if a_tag and 'href' in a_tag.attrs:
            href = a_tag['href']  # Get the 'href' attribute
            if curr_year in href and curr_month in href:  # Check if '2022' is present in the href
                download(href)

def download(file_url):
      # Replace with the desired path to save the downloaded file
    while True:
        try:
            response = requests.get('http://www.google.com')  # Checking connectivity with Google
            if response.status_code == 200:
                download_response = requests.get(file_url)
                if download_response.status_code == 200:
                    with open(save_path, 'wb') as file:
                        file.write(download_response.content)
                break  # Break out of the loop once the file is downloaded
        except requests.ConnectionError:
            print("No internet connection. Retrying in 5 seconds...")
            time.sleep(5)  # Wait for 5 seconds before retrying


setter()
check_if_file_already_downloaded()
set_webdriver_config()
check_if_page_loaded()
srch_key_class()

match_pattern()

driver.quit()
