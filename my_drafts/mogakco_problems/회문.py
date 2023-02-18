word = list(input("단어를 입력해주세요.: "))
for i in range(len(word)//2):
    if word[0] == word[-1]:
         word.pop(0)
         word.pop()
         if len(word)==1:
             print("회문입니다.")
             break
    else:
        print("회문이 아닙니다.")
        break