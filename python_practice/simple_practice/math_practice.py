#function 1 by me
def factorial(x) :
    n = 0
    result = []
    final = 1
    while n < x :
        fac_x = x - n
        result.append(fac_x)
        n += 1
    for element in result:
        final = final * element
    print(final)

factorial(5)

#function 1 answer
def factorial(number):
    factorialOfNum = 1
    while(number > 1):
        factorialOfNum *= number   #number 자체가 줄어드는 방식
        number -= 1                # 처음 facOfNum = 1(facOfNum) * 5 (number)
    if number == 0:                # next facOfNum = 5(facOfNum) * 4 (number-1)
        print("0")
    else: print(factorialOfNum)

#function 2 by me
def mean(numbers):
    final = 0
    for element in numbers:
        final = final + element
    print(final / len(numbers))
mean([2, 4, 6])

#function 2 answer
def meanArray(numArray):
    sumOfArray = 0
    for num in numArray:          # sumOfArray = 0(sumOfArray) + 2(첫 번째 넘버)
        sumOfArray += num         # sumOfArray = 2(sumOfArray) + 4(두 번째 넘버)
    print(str(sumOfArray / len(numArray)))

