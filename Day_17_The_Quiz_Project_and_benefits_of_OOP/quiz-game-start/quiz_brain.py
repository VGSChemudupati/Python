
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.quit_command = 0
        

    def still_has_questions(self):
        if self.quit_command == 0: 
            return self.question_number< len(self.question_list)
        else:
            return False
         
    def check_answers(self, text1, text2):
        user_answer = text1
        correct_answer = text2
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            print(f"correct")
            print(f"score - {self.score}/{self.question_number}")
        elif user_answer.lower() == "quit":
            self.quit_command = 1
            self.still_has_questions()
        else:
            print(f"worng")
            print(f"score - {self.score}/{self.question_number}")
            print(f"This is correct answer : {correct_answer}")



    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}? (True/False)")
        self.check_answers(user_answer, current_question.answer)
       

        


