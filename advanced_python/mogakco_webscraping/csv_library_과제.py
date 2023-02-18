import csv

file = open('C:\\Users\\delig\\Desktop\\coding\\python_practice\\mogakco_webscraping\\covid19_articles.csv', 'r', newline="", encoding='utf-8')

rdr = csv.reader(file)

news = 0

for row in rdr:
    if '[속보]' in row[2]:
        print(row)
        news += 1

print(news)
