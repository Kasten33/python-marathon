class QuizBrain:
    def __init__(self, QList):
        self.QNumber = 0
        self.QList = QList
        self.Score = 0

    def nextQ(self):
        if self.QNumber < len(self.QList):
            CurrentQ = self.QList[self.QNumber]
            self.QNumber += 1
            userA = input(f"Q{self.QNumber}: {CurrentQ.text} (True/False): ")
            self.checkA(userA, CurrentQ.answer)
        else:
            print(f"You've completed the quiz. Your final score is: {self.Score}/{len(self.QList)}")

    def checkA(self, userA, answer):
        if userA.lower() == answer.lower():
            self.Score += 1
            print("You got it right!")
            print(f"New Score: {self.Score}")
            self.nextQ()
        else:
            print("That's wrong. You lose.")
            exit() 



