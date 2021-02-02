from random import *
quizs = ["apple", "banana", "cherry", "orange"]
quiz_number = randint(0, (len(quizs)-1))
print(f"[Debug] quiz number = {quiz_number}, quiz_word = {quizs[quiz_number]}")
quiz = quizs[quiz_number]
input_chars = ''
print("문제: " + "_ "*len(quiz))

while True:
    succeed = True
    
    input_char = input("입력해주세요! : ")
    if input_char == '':
        print("글자를 입력해주세요!")
    
    elif len(input_char) == 1:
        if input_char not in input_chars:
            input_chars += input_char
        for w in quiz:
            if w in input_chars:
                print(w, end=" ")
            else:
                print("_", end=" ")
                succeed = False
        print("\n")
        print(f"[Debug]: input_chars = {input_chars}")
        if succeed:
            print("게임 종료!")
            break
    
    else:
        print("한 글자만 입력해주세요!")