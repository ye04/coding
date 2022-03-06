import requests
import bs4

while True:
    keyword = input("검색할 상품의 키워드를 입력하세요. (종료하려면 0 입력) ")
    if keyword == '0':
        break

    twoDList = []
    numbers= ['7', '8', '1', '2', '13', '3']

    url_list = [] # [[특정 url, 크롤링된 값]]

    arrange_list = ['<G마켓 랭크 순>', '<판매 인기 순>', '<낮은 가격 순>', '<높은 가격 순>', '<상품평 많은 순>', '<신규 상품 순>']
    for element in numbers:
        arrange = element
        url_list.append("https://browse.gmarket.co.kr/search?keyword="+keyword+"&s="+arrange)

    for pair in zip(url_list, arrange_list):
        twoDList.append(list(pair))

    print('<G마켓의', keyword, '상품 정보>')

    for item in twoDList:
        print(item[1])
        raw = requests.get(item[0])
        html = bs4.BeautifulSoup(raw.text, 'html.parser')

        box = html.find('div', {'class': 'section__module-wrap', 'module-design-id': '15'})

        items = box.find_all('div', {'class':'box__item-container'})

        for item2 in items[:3]:
            title=item2.find('span', {'class':'text__item'})
            price = item2.find('strong', {'class':'text__value'})
            print('이름: ', title.text)
            print('가격: ', price.text)
        
        print()
    break

print('이용해 주셔서 감사합니다.')



# url = "https://www.aladin.co.kr/home/welcome.aspx"
# raw = requests.get(url)
# html = bs4.BeautifulSoup(raw.text, 'html.parser')

# target = html.find('div', {'class':'rank'})
# books = target.find_all('tr')

# for book in books:
#     print(book.text)