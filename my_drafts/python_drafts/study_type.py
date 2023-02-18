user_code = input("Type START to start your test. You can stop anytime by typing STOP during the test. ").lower()
user_answers = []
visual = 0
auditory = 0
kinesthetic = 0
result = 0
result_dict = {}
result_list = []
compare_list = []
playing = False

if user_code == "start":
    playing = True
else:
    playing = False

while playing:
    answer1 = input("When learning how to use my computer, I prefer to:\n A: Read the manual first\n B: Have someone explain how to do it first\n C: Just start using the computer and get help if I need it.\nType your answer here: ").lower()
    user_answers.append(answer1)
    if "stop" in user_answers:
        break
    if len(answer1) == 1:
        if answer1 == "a":
            visual += 1
        elif answer1 == "b":
            auditory += 1
        elif answer1 == "c":
            kinesthetic += 1
        else:
            print("Invalid answer. Please type one letter from above.")
            break
    else:
        print("Invalid answer. Please type only one character from above")
        break


    answer2 = input("When getting directions to a new location, it is easier to:\n A: Look at a map\n B: Have someone tell me how to get there\n C: Follow someone or have them take me there.\nType your answer here: ").lower()
    user_answers.append(answer2)
    if "stop" in user_answers:
        break
    if len(answer2) == 1:
        if answer2 == "a":
            visual += 1
        elif answer2 == "b":
            auditory += 1
        elif answer2 == "c":
            kinesthetic += 1
        else:
            print("Invalid answer. Please type one letter from above.")
            break
    else:
        print("Invalid answer. Please type only one character from above")
        break

    answer3 = input("To remember a phone number, I:\n A: Look at the number and dial it several times\n B: Repeat it silently or out loud to myself several times\n C: Remember the number by the pattern pressed on the keypad, the tones of each number or by writing it down.\nType your answer here: ")
    user_answers.append(answer3)
    if "stop" in user_answers:
        break
    if len(answer3) == 1:
        if answer3 == "a":
            visual += 1
        elif answer3 == "b":
            auditory += 1
        elif answer3 == "c":
            kinesthetic += 1
        else:
            print("Invalid answer. Please type one letter from above.")
            break
    else:
        print("Invalid answer. Please type only one character from above")
        break
    
    result_dict.update({"Visual": visual, "Auditory": auditory, "Kinesthetic": kinesthetic})
    result_list.extend(result_dict.values())
    result_list.sort()
    large = result_list.index(result_list[0])
    print(large)
    print(result_list)
    print("Visual:", visual, "Auditory:", auditory, "Kinesthetic:", kinesthetic)

    


    print("You are {} learner" .format(result_list[2]))
    print("Thank you!")
    break

print("See you later!")











'''
if user_code == "start":
    playing = True
else:
    playing = False

def check():
    if "stop" in user_answers:
        return False

    for letter in user_answers:
        if not letter == "a" or not letter == "b" or not letter == "c":
            print("Invalid answer. Please type a letter from above.")
            return False

while playing:
    user_answers.append(input("When learning how to use my computer, I prefer to:\n A: Read the manual first\n B: Have someone explain how to do it first\n C: Just start using the computer and get help if I need it.\nType your answer here: ").lower())
    playing = check()
    user_answers.append(input("When getting directions to a new location, it is easier to:\n A: Look at a map\n B: Have someone tell me how to get there\n C: Follow someone or have them take me there.\nType your answer here: ").lower())
    playing = check()
    print(user_answers)

print("See you next time!")
'''
