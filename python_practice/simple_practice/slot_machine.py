import random
code = "PLAY"
userCode = input("Enter " + code + " to play ")
result = 0
if userCode == "PLAY":
    random1 = random.randint(1,7)
    random2 = random.randint(1,7)
    random3 = random.randint(1,7)
    print(random1, random2, random3)
    firstNumber = int(input("Pick your first number "))
    secondNumber = int(input("Pick your second number "))
    thirdNumber = int(input("Pick your last number "))
    if random1 == firstNumber:
        result = result + 1
    if random2 == secondNumber:
        result = result + 1
    if random3 == thirdNumber:
        result = result + 1
else:
    print('Play next time!')

if result == 0 or result == 1:
        print('Try again next time')
elif result == 2:
        print('You got two out of three! You win!')
elif result == 3:
        print('Congratulation! JackPot!!')
else:
    print('Invalid results')