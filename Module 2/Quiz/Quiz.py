from data import QData
from QuestionModel import Question
from QuizBrain import QuizBrain

Qbank = [Question(item['text'], item['answer']) for item in QData]

quiz = QuizBrain(Qbank)
quiz.nextQ()