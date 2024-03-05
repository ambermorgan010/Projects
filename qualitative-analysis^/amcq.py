# Function 1
def ask_multiple_choice_question(question, options):
    print(question)
    i = input(options).upper()
    while i not in ('A', 'B', 'C', 'D'):
        i = input('Invalid answer, try again: ')
        i = i.upper()
    return i


# Function 2
def ask_multiple_choice_question(question, options):
    print(question)
    for option in options:
        print(option, '-', options[option])

    while True:
        answer = input().lower()
        if answer not in options:
            print('Please answer with a, b or c!')
        else:
            break
    return answer


# Function 3
def ask_multiple_choice_question(question, options):
    print(question)
    print(options)
    response = input().lower()
    while response != 'a' and response != 'b' and response != 'c' and response != 'd':
        response = input('Please enter a, b, c, or d as it is written here.').lower()
    if response == 'a' or response == 'b' or response == 'c' or response == 'd':
        return response
    else:
        return question

# Function 4
def ask_multiple_choice_question(question, options):
    print(question)
    for i in options:
        print(i, ':', options.get(i))
    response = input("Enter either A, B, C, D: ").lower()
    while not (response == 'a' or response == 'b' or response == 'c' or response == 'd'):
        print("Not a valid response")
        response = input("Enter either A, B, C, D: ").lower()
    return response


# Function 5
def ask_multiple_choice_question(question, options):
    """
    Ask the user a multiple choice question. The question is given as a string.
    The options are given as a dictionary with the keys being strings that the
    user can type and the values being what the user is choosing. The question
    is shown to the user along with the choices (with the options put in front
    of them such as A., B., and so forth). The user enters an appropriate letter
    (a, b, c, ... (ignoring case)), validation is performed, and then the typed
    option is returned.
    """
    print(question)
    for letter in options:
        print(letter.upper(), options[letter])
    answer = input('Answer: ')
    answer = answer.lower()
    while answer not in options:
        answer = input('Invalid answer!\nTry Again: ')
        answer = answer.lower()
    return answer


# Function 6
def ask_multiple_choice_question(question, options):
    print(question)
    for letter in options: print(letter.lower(), options[letter])







    response = input('Enter your letter response: ').lower()
    while response not in options: response = input('Sorry, invalid response. Please try again. Enter your letter response: ').lower()
    return response


# Function 7
def ask_multiple_choice_question(question, choices):
    print(question)
    print('\n'.join('%s: %s' % (c.upper(), choices[c]) for c in choices))
    answer = input('Your answer is: ')
    while answer.lower() not in choices:
        print("Error: Please pick one of the multiple choice options.")
        print(question)
        print('\n'.join('%s: %s' % (c.upper(), choices[c]) for c in choices))
        answer = input('Your answer is: ')
    return answer.lower()


# Function 8
def ask_multiple_choice_question(question, options):
    print("")
    print(question)
    for letter in options:
        print("    " + letter.upper() + ". " + options[letter])
    answer = input("What is your choice? ")
    answer = answer.lower()
    while answer not in options:
        answer = input("Not a valid response, please enter one of the shown letters: ")
        answer = answer.lower()
    return answer


# Function 9
def ask_multiple_choice_question(mc_question, options):
    # Validates user input multiple choice answer and returns it for scoring
    print('\n' + mc_question)
    for choice in options:
        # Shows user options from which to choose for multiple choice questions
        print('%s: %s' % (choice.upper(), options[choice]))
    answer = input('Your answer: ').strip()
    while answer.lower() not in options:
        # Asks user to enter proper value for multiple choice answer
        print('\nPlease choose one of the multiple choice options.')
        return ask_multiple_choice_question(mc_question, options)
    return answer.lower()


# Function 10
def ask_multiple_choice_question(question, options):
    print()
    user_input = input(question).upper().strip()
    for letter in options:
        print(letter, options[letter])

    while user_input not in ("A", "B", "C", "D"):
        user_input = input("Please enter A, B, C, or D:  ").upper().strip()
        user_input = user_input.upper().strip()
    return user_input
