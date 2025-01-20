from data import question_data

class Quizbrain:
    def __init__(self, questions):
        self.questions = questions
        self.questions_number = 0
        self.score = 0

    def next_questions(self):
        for i in range(len(self.questions)):
            questions_input =  input(f"Q.{i+1 }. {self.questions[i][ "question"]} (True/False): ")
            if questions_input == self.questions[i]["correct_answer"]:
                print("Correct")
                self.score += 1
                print(f"Your current score is {self.score}")
            else:
                print("Wrong")

ask_question = Quizbrain(question_data)

ask_question.next_questions()