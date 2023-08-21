from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

q_list = []

for question in question_data:
    q_list.append(Question(question["text"], question["answer"]))

qb = QuizBrain(q_list)

while qb.has_more_questions():
    qb.next_question()

print(f"Quiz completed!\nFinal Score: {round(qb.score/qb.q_number*100,1)}% ({qb.score}/{qb.q_number})")
