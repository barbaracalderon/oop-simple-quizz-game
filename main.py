from question_model import Question
from data import question_data

# We must create all our questions. So, create a question bank
# It should look something like:
# question_bank = [
#   Question(q1, a1),
#   Question(q2, a2),
#   Question(q3, a3)
#   ...
# ]
question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    pair = Question(q_text, q_answer)
    question_bank.append(pair)

for pair in question_bank:
    print(pair)
