"""
FUNCTION: Student database program.

AUTHOR NAME: Amber Morgan
"""

import matplotlib.pyplot as plt


def read_students(filename):
    """
    Reads the student records from the given CSV file.
    Returns four dictionaries:
        1. The key is the ID and the values are individual student records.
        2. The key is the major (lowercase), and the values are lists of student records.
        3. The key is the year (lowercase) and, the values are lists of student records.
        4. The key is the advisor (lowercase) and, the values are lists of student records.

    Each student record is a list with all of the following:
        student ID (int)
        name
        major
        year
        advisor
    None of these values have been changed except ID is converted to an int.
    """
    file = open(filename)
    key_ID = {}  # ID: individual student record
    key_major = {}  # major (lower): student records
    key_year = {}  # year (lower): student records
    key_advisor = {}  # advisor (lower): student records
    for line in file:
        ID, name, major, year, advisor = line.strip().split(",")
        ID = int(ID)
        key_ID[ID] = [ID, name, major, year, advisor]
        if major.lower() not in key_major:
            key_major[major.lower()] = []
        key_major[major.lower()].append([ID, name, major, year, advisor])
        if year.lower() not in key_year:
            key_year[year.lower()] = []
        key_year[year.lower()].append([ID, name, major, year, advisor])
        if advisor.lower() not in key_advisor:
            key_advisor[advisor.lower()] = []
        key_advisor[advisor.lower()].append([ID, name, major, year, advisor])
    file.close()
    return key_ID, key_major, key_year, key_advisor


def get_valid_id_from_user(ids):
    """
    Gets a valid ID from the user. A valid ID is a bunch of digits and, once converted to an int,
    is one of the elements in the given set of IDs. This function returns an integer.
    """
    input_ID = input("Enter a student ID: ")
    while not input_ID.isdigit() or int(input_ID) not in ids:
        input_ID = input("Not a valid ID, try again: ")
    return int(input_ID)


def get_valid_value_from_user(allowed, name):
    """
    Gets a valid value from the user. The input must be in the set of allowed values given as an
    argument. All of the allowed options have already been converted to lowercase, and the user's
    input should be as well. The prompt to the user includes the given name argument.
    """
    input_value = input("Enter a {}: ".format(name))
    while input_value.lower() not in allowed:
        input_value = input("Not a valid {}, try again: ".format(name))
    return input_value.lower()


def print_information_for_student(student_record):
    """
    Prints out the information from a student record. A student record is a list of a single
    student's ID, name, major, year, and advisor.
    """
    ID, name, major, year, advisor = student_record
    print("Student #{}: {} in major {} in {} year with advisor {}".format(ID, name, major, year, advisor))


def print_list_of_students(student_records):
    """
    Prints out the ID and name of the students in the list. The student records contain a lot of
    information, but the first two values in each record are the ID and the name.
    """
    for student in student_records:
        print(student[0], student[1])


def get_lengths(collection):
    """
    Returns a list of the lengths of each of the values of the elements in the given collection.
    """
    lengths = []
    for element in collection:
        lengths.append(len(element))
    return lengths


def convert_all_to_title_case(collection):
    """
    Returns a list containing all of the elements in the given collection but after calling the
    title() method for each of them.
    """
    elements = []
    for element in collection:
        elements.append(element.title())
    return elements


def bar_plot_len_of_values(dictionary):
    """
    Makes a bar plot with the keys of the dictionary as the x-ticks and the Y values are the
    lengths of each of the values of the items in the dictionary.
    """
    # Gets the X ticks values and the Y values
    X = convert_all_to_title_case(dictionary.keys())
    Y = get_lengths(dictionary.values())

    plt.bar(X, Y, tick_label=X)

    plt.xticks(rotation=90)  # Rotates the x-ticks by 90 degrees
    plt.subplots_adjust(bottom=0.35)  # Makes room for the x-ticks
    plt.show()


def main():
    # Load the data
    students_by_id, students_by_major, students_by_year, students_by_advisor = read_students('students.csv')

    # Continue until the user chooses to quit
    quitting = False
    while not quitting:
        # Show the menu
        print('---------------------------------------')
        print('MENU')
        print('1. List of Grades for Student Given ID')
        print('2. List Students for Major')
        print('3. List Students for Class Year')
        print('4. List Students with Advisor')
        print('5. Plot Number of Students per Major')
        print('6. Plot Number of Students per Class Year')
        print('7. Plot Number of Students per Advisor')
        print('8. Quit')
        print('---------------------------------------')

        # Get the user's choice; then do the appropriate action.
        choice = input('Enter your menu choice: ')
        if choice == '1':
            student_id = get_valid_id_from_user(students_by_id.keys())
            print_information_for_student(students_by_id[student_id])
        elif choice == '2':
            major = get_valid_value_from_user(students_by_major.keys(), 'major')
            print_list_of_students(students_by_major[major])
        elif choice == '3':
            year = get_valid_value_from_user(students_by_year.keys(), 'class year')
            print_list_of_students(students_by_year[year])
        elif choice == '4':
            advisor = get_valid_value_from_user(students_by_advisor.keys(), 'advisor')
            print_list_of_students(students_by_advisor[advisor])
        elif choice == '5':
            bar_plot_len_of_values(students_by_major)
        elif choice == '6':
            bar_plot_len_of_values(students_by_year)
        elif choice == '7':
            bar_plot_len_of_values(students_by_advisor)
        elif choice == '8':
            quitting = True
        else:
            print('Invalid choice, please try again')
    print('Bye!')


if __name__ == "__main__":
    main()
