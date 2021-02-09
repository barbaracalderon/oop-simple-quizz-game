from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    pair = Question(q_text, q_answer)
    question_bank.append(pair)
    # We created a list of questions (question_bank) where
    # we're adding each question/answer pair to.

game_quiz = QuizBrain(question_bank)
while game_quiz.still_has_questions():
    game_quiz.next_question()
print('You reached the end of the Quiz!')
print(f'Your total score was {game_quiz.score}/{len(question_bank)}')
# TODO: asking the questions
# TODO: check if answers are correct
# TODO: check if we reached the end of the quizz

# class Quizzbrain with 2 attributes: question_numer = 0 and question_list
# and 1 method: next_question()

# We must create all our questions. So, create a question bank
# It should look something like:
# question_bank = [
#   Question(q1, a1),
#   Question(q2, a2),
#   Question(q3, a3)
#   ...
# ]
