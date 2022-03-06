def solution(participated, qualified):
    unqualified = []
    for person in participated:
        if person in qualified:
            qualified.remove(person)
        else:
            unqualified.append(person)
    return unqualified
solution(['곰', '곰', '망고', '김변수', '곰'], ['김변수', '망고', '곰', '곰'])