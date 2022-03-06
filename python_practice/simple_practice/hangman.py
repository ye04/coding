def hangman(word):
    try_num = 10
    board = []
    users = []
    wrong = set({})

    for i in word:
        board.append("_ ")

    users_letters = sorted(users)
    given_letters = sorted(board)

    while users_letters != given_letters:

        users_letters = sorted(users)
        given_letters = sorted(board)
        print(''.join(board))

        user_letter = input(("Guess the word! [Wrong letters: {0}] [Remained try: {1}] ".format(''.join(wrong), try_num))).lower()

        if user_letter == "quit".lower():
            break
        
        if len(user_letter) > 1:
            print("Please type only a letter")
            break

        if user_letter not in word:
            wrong.add("{0} ".format(user_letter))
            try_num -= 1

        count = -1
        
        for j in word:
            count += 1
            if j == user_letter:
                board[count] = j
                users.append(j)
                users_letters.append(j)

            else:
                continue
        
        if len(users) == len(word):
            print(word)
            print("Yay you guessed the word correctly! [Word: {0}]" .format(word))
            break
        
        if try_num <= 0:
            print("Sorry try again")
            break



        

hangman("hello")