from selenium import webdriver
import time
import csv

driver = webdriver.Chrome('chromedriver')
url = 'https://papago.naver.com/'
driver.get(url)
time.sleep(3)
switch_button = driver.find_element_by_css_selector('button.btn_switch___x4Tcl')
switch_button.click()

f = open("./my_papago.csv", "r", newline = '', encoding = 'utf-8')
korean = []
rdr = csv.reader(f)
my_dict = {}
next(rdr)

for row in rdr:
    korean.append(row[1])



for i in range(len(korean)):
        driver.find_element_by_css_selector('textarea#txtSource').send_keys(korean[i])
        driver.find_element_by_css_selector('button#btnTranslate').click()
        time.sleep(1)

        output = driver.find_element_by_css_selector('div#txtTarget').text

        my_dict[korean[i]] = output

        driver.find_element_by_css_selector('textarea#txtSource').clear()

f.close()
driver.close()

for item in my_dict.items():
    print(item[0],":",item[1])
        
    