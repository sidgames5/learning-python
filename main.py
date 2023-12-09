# https://www.youtube.com/watch?v=rfscVS0vtbw
# left off at 4:08:28

from Question import Question


question_prompts = [
    "What color are apples?\n(a) Red\n(b) Green\n(c) Blue\n\n",
    "What color are bananas?\n(a) Black\n(b) Yellow\n(c) Orange\n\n",
    "What color are strawberries?\n(a) Red\n(b) Yellow\n(c) White\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
]


def run_test(questions: list[Question]):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"Score: {str(score)} / {str(len(questions))}")
    percentage = (score / len(questions)) * 100
    if percentage >= 90:
        print("A")
    elif percentage >= 80:
        print("B")
    elif percentage >= 70:
        print("C")
    elif percentage >= 65:
        print("D")
    else:
        print("F")


run_test(questions)
