"""
FUNCTION: This file contains all of the questions that make up the quiz and their answer parameters.
AUTHOR: Amber Morgan
"""

import question_types


def question_1():
    response = question_types.ask_yes_no_question("Do you like thunderstorms?")
    if response:
        print("Interesting...")
        return 4
    else:
        print("Coward.")
        return 1


def question_2():
    response = question_types.ask_multiple_choice_question("Which horror movie character trope are you?",
                                                           {"a": "The Jock", "b": "The Blonde", "c": "The Innocent",
                                                            "d": "The Scholar", "e": "The Idiot"})
    if response == "a":  # The Jock
        print("At least you're more tolerable than The Blonde trope.")
        return 2
    elif response == "b":  # The Blonde
        print("This is the most annoying trope. Bad vibes.")
        return 1
    elif response == "c":  # The Innocent
        print("At least you're the most likely to survive, I guess.")
        return 3
    elif response == "d":  # The Scholar
        print("You're probably the reason The Innocent survives. Your sacrifice is worthwhile.")
        return 4
    else:  # The Idiot
        print("You are the best trope. You are the redeeming quality of bad movies.")
        return 5


def question_3():
    response = question_types.ask_yes_no_question("Do you enjoy stargazing?")
    if response:  # yes
        print("Good... good.")
        return 4
    else:  # no
        print("But why?")
        return 1


def question_4():
    response = question_types.ask_multiple_choice_question("What's your favorite season?",
                                                           {"a": "Spring", "b": "Summer", "c": "Fall", "d": "Winter"})
    if response == "a":  # Spring
        print("You're probably a happy person.")
        return 2
    elif response == "b":  # Summer
        print("You're basic. I mean that as an insult.")
        return 1
    elif response == "c":  # Fall
        print("You're the best. Carry on.")
        return 4
    else:  # Winter
        print("You're valid.")
        return 3


def question_5():
    response = question_types.ask_multiple_choice_question("Are you an early bird or night owl?",
                                                           {"a": "early bird", "b": "night owl", "c": "neither"})
    if response == "a":  # early bird
        print("You probably have a superiority complex because of it.")
        return 1
    elif response == "b":  # night owl
        print("I appreciate you. Carry on.")
        return 3
    else:  # neither
        print("This is understandable... I feel ya.")
        return 2


def question_6():
    response = question_types.ask_multiple_choice_question("Do you prefer tea or coffee?", {"a": "tea", "b": "coffee",
                                                                                            "c": "neither", "d": "both"})
    if response == "a":  # tea
        print("You have taste.")
        return 3
    elif response == "b":  # coffee
        print("You probably have a caffeine addiction.")
        return 2
    elif response == "c":  # neither
        print("Huh, okay. You better not be drinking energy drinks instead then.")
        return 1
    else:  # both
        print("Indecisive. Me too.")
        return 4


def question_7():
    response = question_types.ask_multiple_choice_question("If I hand you the aux cord, what will you play?",
                                                           {"a": "rock", "b": "country", "c": "pop", "d": "metal",
                                                            "e": "classical", "f": "rap"})
    if response == "a":  # rock
        print("Okay, that's a good choice.")
        return 5
    elif response == "b":  # country
        print("I will kick you out of my car while it's moving. Don't try it.")
        return 1
    elif response == "c":  # pop
        print("Meh, that's a mediocre choice... unless it's 2000s pop music.")
        return 4
    elif response == "d":  # metal
        print("You're either the coolest person ever or you're an elitist. I'll give you the benefit of the doubt.")
        return 6
    elif response == "e":  # classical
        print("Is this actually your favorite or does everyone just say it should be?")
        return 2
    else:  # rap
        print("You're on thin ice, but not as thin as country music.")
        return 3


def question_8():
    response = question_types.ask_numerical_question("What month were you born in (use corresponding number)?", 1, 12)
    if response == 3 or response == 4 or response == 11:
        print("Ooh!")
        return 4
    elif response == 1 or response == 2 or response == 8:
        print("Alright.")
        return 3
    elif response == 5 or response == 9 or response == 10:
        print("Oof.")
        return 2
    else:
        print("Noted.")
        return 1


def question_9():
    response = question_types.ask_numerical_question("What's your favorite number?", None, None)
    if response < 0:  # negatives
        print("Ah, a negative number. That's pretty cool.")
        return 5
    elif 0 < response < 10:  # 1-9
        print("You're boring. Should've picked a cooler number.")
        return 1
    elif response == 69 or response == 420:  # silly goose
        print("Silly goose. But unoriginal.")
        return 3
    elif 9 < response < 100:  # 10-99
        print("You're cool. Not the coolest, but cool.")
        return 4
    else:  # >100
        print("Eh, that's an okay choice.")
        return 2


def question_10():
    response = question_types.ask_numerical_question("How would you rate your own vibes?", 1, None)
    if response < 3:  # 1-2
        print("You're probably right.")
        return 1
    elif 2 < response < 5:  # 3-4
        print("Well, at least you're honest.")
        return 2
    elif 4 < response < 7:  # 5-6
        print("Okay, that's alright.")
        return 4
    elif 7 < response < 9:  # 7-8
        print("I believe you.")
        return 5
    else:  # 9-...
        print("You're full of yourself. Get your vibes checked.")
        return 3
