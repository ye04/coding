import requests
import bs4

url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
raw = requests.get(url) #데이터가 아니라 요청이 성공했는지 여부를 돌려줌
target = '<div class="nums">'
#if target in raw.text:
    #index = raw.text.index(target)
    #print(raw.text[index:index + 578])

html = bs4.BeautifulSoup(raw.text, 'html.parser')
#html 데이터 == raw.text 이고 문자열을 html로 바꿔야 하기 때문에 'html.parser'
#html 문자열을 html로 변환해서 bs4 객체로 만듦

#find 함수 --> argument로 받은 것과 일치하는 태그들 중에서 가장 첫번째 태그만 반환
# 1. 태그만 사용 하는 경우
#html.find('div')

# 2. 선택자만 사용하는 경우
#html.find(id = 'example1')
#html.find(attrs = {'id':'example1'})

# 3. 태그 이름과 선택자 정보 모두 사용하는 경우
#html.find('div', {'id' : 'example1'})

#find_all 함수 --> 일치하는 모든 태그 반환 (사용법은 동일)

target = html.find('div', {'class':'nums'})
balls = target.find_all('span', {'class':'ball_645'})


for ball in balls[:-1]: #마지막 하나 전 element까지만
    print('당첨번호: ', ball.text) #ball은 태그를 포함한 html 코드, ball.text는 contents만 들어있는 strig

print('보너스 번호: ', balls[-1].text) #이건 반복하지 않아도 됨