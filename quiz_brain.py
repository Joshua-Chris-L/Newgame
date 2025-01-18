from data import question_data

class Quizbrain:
    def __init__(self, questions):
        self.questions = questions
        self.questions_number = 0

    def next_questions(self):
        for i in range(len(self.questions)):
            questions =  input(f"{self.questions[i]["text"]} ")
            print(questions)


ask_question = Quizbrain(question_data)

ask_question.next_questions()