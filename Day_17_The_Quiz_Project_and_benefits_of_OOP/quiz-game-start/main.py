# import question_model
# import data

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# database = data.question_data
# question_bank = []


# for item in database:
#     text= item["text"]
#     answer = item["answer"]
#     question = question_model.Question(text,answer)
#     question_bank.append(question)

# #print(question_bank)

# for question in question_bank:
#     print(question.text)
#     print(question.answer)


question_bank = []

for question in question_data:
    qtext = question["question"]
    qans = question["correct_answer"]
    new_question = Question(qtext, qans)
    question_bank.append(new_question)

# for question in question_bank:
#     print(question.text)
#     print(question.answer)


quiz = QuizBrain(question_bank)

decision_to_continue = True

while quiz.still_has_questions():
    user_answer = quiz.next_question()
    print("\n")
    
print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
