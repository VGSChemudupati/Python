import data

question_bank = data.question_data
score = 0
i = 1
for item in question_bank:
    user_answer = input(item["question"])
    if user_answer == item["correct_answer"]:
        score +=0
        print(f"right// score is {score}/{i} ")

    elif user_answer == "quit":
        break
    else:
        print(f"wrong// score is {score}/{i} ")
    i+=1

print("You've completed the quiz")
print(f"Your final score is {score}/{len(question_bank)}")