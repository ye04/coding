from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome('C:\\Users\\delig\\Desktop\\coding\\python_practice\\mogakco_webscraping\\chromedriver.exe', options=options)
url = "https://papago.naver.com/"
driver.get(url)
time.sleep(3)

dictionary = {}

while True:
    question = input("번역할 영단어 입력 (0을 입력하면 종료됩니다.) : ")

    if question == '0':
        break
    else:
        form = driver.find_element_by_css_selector('textarea#txtSource')
        form.send_keys(question)

        button = driver.find_element_by_css_selector("button#btnTranslate")
        button.click()
        time.sleep(2)

        result = driver.find_element_by_css_selector("div#txtTarget")
        dictionary[question] = result.text
        
        form.clear()

driver.close()
print(dictionary)