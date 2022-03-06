from selenium import webdriver
import time

driver = webdriver.Chrome('C:\\Users\\delig\\Desktop\\coding\\python_practice\\mogakco_webscraping\\chromedriver.exe')
url = "https://papago.naver.com/"
driver.get(url)
time.sleep(3)

question = input("Type here to translate. : ")

form = driver.find_element_by_css_selector("textarea#txtSource")
form.send_keys(question)

button = driver.find_element_by_css_selector("button#btnTranslate")
button.click()
time.sleep(2)

result = driver.find_element_by_css_selector("div#txtTarget")
print(question, "->", result.text)

driver.close()