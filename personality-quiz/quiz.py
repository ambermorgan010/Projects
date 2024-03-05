"""
FUNCTION: This is the quiz. It calls the question, collects the scores, and prints the result.
AUTHOR: Amber Morgan
"""


import questions
import question_types


def scoring(score):
    if score > 38:
        print("Your vibes are absolutely immaculate. Congrats.")
    elif score > 30:
        print("Your vibes are pretty good... You pass the vibe check.")
    elif score > 20:
        print("This is acceptable... your vibes are questionable, but they'll suffice.")
    elif score > 10:
        print("You're on thin ice, buddy. Mediocre vibes at best.")
    else:
        print("If your vibes were a food, they'd be expired milk or that piece of cheese on the basketball court in"
              "Diary of a Wimpy Kid. Bad vibes. Horrible.")


def main():
    scores = [questions.question_1(), questions.question_2(), questions.question_3(), questions.question_4(),
              questions.question_5(), questions.question_6(), questions.question_7(), questions.question_8(),
              questions.question_9(), questions.question_10()]
    final_score = sum(scores)
    scoring(final_score)


if __name__ == "__main__":
    main()
