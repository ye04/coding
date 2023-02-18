# 문제


# 파이썬에 내장된 round() 함수를 이용하지 않고, 반올림 계산을 실행할 수 있는 코드를 작성해보세요.

# 조건 1 : 소수 첫째 자리에서 반올림이 이루어집니다. (ex. 3.14 → 3, 1.5 → 1)
# 조건 2 : 소수 첫째 자리가 0~4이면 버림, 5~9이면 올림을 합니다.

num = input("반올림할 숫자를 입력해 주세요: ")

if "." in num:
    parts = num.split(".")
    whole_num = int(parts[0])
    tenth_digit = int(parts[1][0])
    if tenth_digit <= 4:
        result = whole_num
    elif tenth_digit >= 5:
        result = whole_num + 1
    
    print(f"반올림된 숫자는 {result} 입니다.")
else:
    print("입력하신 숫자는 이미 자연수입니다.")
