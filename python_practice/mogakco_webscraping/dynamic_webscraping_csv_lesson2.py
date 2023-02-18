from selenium import webdriver
import time
import csv

driver = webdriver.Chrome('/chromedriver')
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

#store the 'my_papago.csv' file to read in the varialble 'f'
f = open('./my_papago.csv', 'r', encoding = 'utf-8')
#store all the data in csv file in the variable 'rdr'
rdr = csv.reader(f)
#skip the very first row(column headers) of 'rdr'
next(rdr)

my_dict = {}

#store the vocabulary and the translation result in the dictionary
for row in rdr:
    keyword = row[0]
    korean = row[1]
    my_dict[keyword] = korean

f.close()

#to allow adding to the file, reopen the file with the mode 'a'
f = open('./my_papago.csv', 'a', newline='', encoding = 'utf-8')
wtr = csv.writer(f)

#tranlating
while True:
    keyword = input('번역할 영단어 입력 (0 입력하면 종료)')
    if keyword == '0':
        print('번역 종료')
        break
    
    #if the vocabulary is in the 'my_dict' dictionary keys, let the user know this, and print out the stored translation result
    if keyword in my_dict.keys():
        print('이미 번역한 영단어입니다! 뜻은',my_dict[keyword], '입니다.')
    else:
        driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
        driver.find_element_by_css_selector('button#btnTranslate').click()
        time.sleep(1)

        output = driver.find_element_by_css_selector('div#txtTarget').text

        wtr.writerow([keyword, output])

        my_dict[keyword] = output

        driver.find_element_by_css_selector('textarea#txtSource').clear()

driver.close()

f.close()
