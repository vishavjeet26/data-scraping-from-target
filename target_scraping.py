from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import re
import json

url = "https://www.target.com/p/-/A-81260450"
driver = Chrome(executable_path = 'C:\\Users\\Sara\\Downloads\\vishavjeet_doc\\certifications\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(20)
driver.get(url)

raw_data = {'url':url}


try:
    title = driver.find_element(By.XPATH, '//*[@id="pageBodyContainer"]/div[1]/div[1]/h1/span')
    raw_data['title'] = title.get_attribute('innerText')

except NoSuchElementException:
    print("There's no title available")

try:
    description = driver.find_element(By.XPATH, '//*[@id="specAndDescript"]/div[1]/div[2]/div[1]')
    raw_data['description'] = description.get_attribute('innerText')

except NoSuchElementException:
    print("There's no title available")

try:
    price_element = driver.find_element(By.XPATH, '//*[@id="pageBodyContainer"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/span')
    match = re.search(r'([\D]+)([\d,]+)', price_element.get_attribute('innerText'))
    currency, price = (match.group(1), match.group(2).replace(',',''))
    raw_data['currency'] = currency
    raw_data['price'] = int(price)

except NoSuchElementException:
    raw_data['currency'] = None
    raw_data['price'] = None
    print("There's no pricce available")

try:
    ingredients = driver.find_element(By.XPATH, '//*[@id="tabContent-tab-Labelinfo"]/div/div/div[1]/div')
    raw_data['ingredients'] = ingredients.get_attribute('innerText').split(',')

except NoSuchElementException:
    raw_data['ingredients'] = []
    print("There's no ingredients available")

try:
    specs = driver.find_element(By.XPATH, '//*[@id="specAndDescript"]/div[1]/div[1]')
    raw_data['specs'] = specs.get_attribute('innerText')


except NoSuchElementException:
    raw_data['specs'] = {}
    print("There's no specs available")


soup = BeautifulSoup(driver.page_source,'html.parser')

#gets a list of all elements under "Specifications"
div = soup.find("div", {"class":"styles__StyledCol-sc-ct8kx6-0 iKGdHS h-padding-h-tight"})
list = div.find_all("div")
for a in range(len(list)):
    list[a] = list[a].text

    

#locates the elements in the list
tcin = [v for v in list if v.startswith("TCIN")]
upc = [v for v in list if v.startswith("UPC")]

if tcin:
    raw_data['tcin'] = tcin[0].split(':')[1].strip()

if upc:
    raw_data['upc'] = upc[0].split(':')[1].strip()

json_object = json.dumps(raw_data, indent = 4)
  
# Writing to output.json
with open("output.json", "w") as outfile:
    outfile.write(json_object)

driver.quit()