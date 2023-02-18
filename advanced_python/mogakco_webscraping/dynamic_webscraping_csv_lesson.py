from selenium import webdriver
import time
import csv

#open the automated chrome browser
driver = webdriver.Chrome('chromedriver')

#papago webpage
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
#time delay
time.sleep(3)

#create a 'my_papago.csv' file to write and store it in the variable 'f'
f = open('./my_papago.csv', 'w', newline='',  encoding='utf-8')
#create a 'wtr' object that writes the csv file
wtr = csv.writer(f)
#write a column header
wtr.writerow(['영단어', '번역결과'])

#무한 루프 (번역 작업을 원하는 만큼 실행할 수 있도록)
while True:
    keyword = input('번역할 영단어 입력 (0 입력하면 종료) ')
    if keyword == '0':
        print('번역 종료')
        break
    
    #input the english vocab and click the translate button
    form = driver.find_element_by_css_selector('textarea#txtSource')
    form.send_keys(keyword)

    button = driver.find_element_by_css_selector('button#btnTranslate')
    button.click()
    time.sleep(1)

    #store the translation result
    output = driver.find_element_by_css_selector('div#txtTarget').text

    #write the [영단어, 번역결과] to the my_papago.csv file
    wtr.writerow([keyword, output])

    #clear the textarea to repeat the same process for different vocabulary
    driver.find_element_by_css_selector('textarea#txtSource').clear()

#close the chrome browser
driver.close()
#close the file
f.close()