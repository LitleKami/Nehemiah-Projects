from Question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for dat in question_data:
    text = dat["question"]
    answer = dat["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()
print("You have completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
