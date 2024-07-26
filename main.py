
import random
from questanswers import *

overall_result = 0
questions_to_answer = 10

while questions_to_answer > 0:
    questions_to_answer -= 1
    random_question = random.choice(question_list)
    question_index = question_list.index(random_question)
    answer_quest = answer_list[question_index]


    def count_words(sentence1, sentence2):
        words1 = set(sentence1.split())
        words2 = set(sentence2.split())
        common_words = words1 & words2

        return len(common_words)

    answer_input = input(random_question)
    count_result = count_words(answer_input.lower(), answer_quest.lower())
    overall_result += count_result
    question_list.pop(question_index)
    answer_list.pop(question_index)

if overall_result < 20:
    print("Your answers are very weak and you are rejected")
elif overall_result < 35:
    print("judging by your answer you need more practice")
elif overall_result < 50:
    print("You knowledge is good, but still need some practice to gain and you proposed to work as intern")
elif overall_result > 50:
    print("You answers were good enough on some questions and you are hired")




