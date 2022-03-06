# 문제

# 메뉴에 있는 도형을 선택하고 길이를 입력받아 넓이를 구할 수 있는 코드를 작성해보세요.

# 조건 1 : 도형은 원, 삼각형, 직사각형, 정사각형이 존재합니다.
# 조건 2 : 도형의 넓이 계산은 무조건 함수로 정의되어야 합니다.
# 조건 3 : 도형 별로 필요한 길이를 입력받아야 합니다.
# 원 → 반지름
# 삼각형 → 밑변 , 높이
# 직사각형 → 가로, 세로
# 정사각형 → 한 변의 길이

# [참고] 도형 넓이 계산 공식

# (원 넓이 공식) : 반지름 * 반지름 * 원주율(3.1415)
# (삼각형 넓이 공식) : 밑변 * 높이 / 2
# (직사각형 넓이 공식) : 가로 * 세로
# (정사각형 넓이 공식) : (한 변 길이) * (한 변 길이)
import math

def circle(radius):
    area = round(radius * radius * 3.1415, 2)
    return area
def triangle(base, height):
    area = round((base * height)/2, 2)
    return area
def rectangle(width, length):
    area = round((width * length)/2 , 2)
    return area
def square(side):
    area = round(side**2, 2)
    return area


print("""==========도형 목록==========
1. 원
2. 삼각형
3. 직사각형
4. 정사각형
============================""")
shape = int(input("도형 목록에서 넓이를 계산할 도형의 번호를 입력해주세요: "))

if shape == 1:
    radius = int(input("원의 반지름 길이를 입력해주세요: "))
    area = circle(radius)
    print(f"반지름 길이가 {radius}인 원의 넓이는 {area}입니다.")
elif shape == 2:
    base = int(input("삼각형 밑변의 길이를 입력해주세요: "))
    height = int(input("삼각형 높이의 길이를 입력해주세요: "))
    area = triangle(base, height)
    print(f"밑변이 {base}이고 높이가 {height}인 삼각형의 넓이는 {area}입니다.")
elif shape == 3:
    width = int(input("직사각형 가로의 길이를 입력해주세요: "))
    length = int(input("직사각형 세로의 길이를 입력해주세요: "))
    area = rectangle(width, length)
    print(f"가로가 {width}이고 높이가 {length}인 삼각형의 넓이는 {area}입니다.")
elif shape == 4:
    side = int(input("정사각형 한 변의 길이를 입력해주세요: "))
    area = square(side)
    print(f"한 변의 길이가 {side}인 정사각형의 넓이는 {area}입니다.")
else:
    print("위 항목 중에서 골라주세요.")

