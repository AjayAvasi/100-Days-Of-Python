def check_answer(question, input_answer):
    return question.answer == input_answer


class QuizBrain:

    def __init__(self, q_list):
        self.q_list = q_list
        self.score = 0
        self.q_number = 0

    def next_question(self):
        question = self.q_list[self.q_number]
        self.q_number += 1
        answer = input(f"{self.q_number}) {question.question} (True/False): ")
        if check_answer(question, answer):
            print("You got it right! ")
            self.score += 1
        else:
            print("You got it wrong :(")

        print(f"The correct answer is {question.answer}.\nCurrent Score: {self.score}/{self.q_number}\n")

    def has_more_questions(self):
        return self.q_number < len(self.q_list)
