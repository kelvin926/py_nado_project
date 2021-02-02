class sinjo:
    def __init__ (self, word, ex1, ex2, answer):
        self.word = word
        self.ex1 = ex1
        self.ex2 = ex2
        self.answer = answer
    
    def show_question(self):
        print(f"이건 무슨 뜻 일까요?: {self.word}")
        print(f"1. {self.ex1}")
        print(f"2. {self.ex2}")
    
    def check_answer(self):
        while True:
            try:
                user_answer = int(input("답: "))
                if user_answer == self.answer:
                    print("정답입니다!")
                    break
                else:
                    print("오답입니다!")
            except(ValueError):
                print("숫자만 입력하세요!")
                pass

#main
word = sinjo("별다줄", "별결 다 줄이네", "별같이 다 줄이자:", 1)
word.show_question()
word.check_answer()