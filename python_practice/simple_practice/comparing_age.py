#사용자와 내가 동갑인지 아닌지를 확인하는 프로그램
myAge = 13
userAge = int(input("당신은 몇 살 인가요? "))
if myAge == userAge :
    print("저와 동갑이시네요!")
elif myAge > userAge :
    print("제가 ", (myAge - userAge), " 살 더 많네요.")
elif myAge < userAge :
    print("저보다 ", (userAge - myAge), " 살 많으시네요.")
else:
    print("에러 발생, 확인이 불가능합니다.")







