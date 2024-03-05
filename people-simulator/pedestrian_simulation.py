'''
FUNCTION: Simulates pedestrians
AUTHOR: Amber Morgan
'''

import random
import matplotlib.pyplot as plt


def create_person(stationary_prob, world_size):
    """
    Creates a person. A person is represented by a dictionary with 3 or 5 keys: stationary, x, y,
    and possibly dest_x and dest_y. Stationary is a bool, and the others are integers that are
    initialized to a random value from 0 to world_size.
    """
    person = {}
    rand_float = random.random()
    person["x"] = random.randint(0, world_size)
    person["y"] = random.randint(0, world_size)
    if rand_float < stationary_prob:
        person["stationary"] = True
    else:
        person["stationary"] = False
        person["dest_x"] = random.randint(0, world_size)
        person["dest_y"] = random.randint(0, world_size)
    return person


def move_person(person, world_size):
    """
    Move a person slightly closer to their destination. If they are stationary, then nothing
    happens. Otherwise, their location gets one step closer in each direction (if possible)
    to the destination. If, after moving, they have reached their destination, then a new
    random destination is created.
    """
    if not person["stationary"]:
        if person["x"] < person["dest_x"]:
            person["x"] += 1
        if person["y"] < person["dest_y"]:
            person["y"] += 1
        if person["x"] > person["dest_x"]:
            person["x"] -= 1
        if person["y"] > person["dest_y"]:
            person["y"] -= 1
        if person["x"] == person["dest_x"] and person["y"] == person["dest_y"]:
            person["dest_x"] = random.randint(0, world_size)
            person["dest_y"] = random.randint(0, world_size)
    return person


def plot(people, color):
    """
    Plots a list of people that are each represented as a dictionary with the keys x and y using
    using a scatter plot. The color of the dots is given. This is done efficiently by only calling
    plt.scatter(...) once with lists of all of the x and y values of all the people.
    """
    X = []
    Y = []
    for person in people:
        X.append(person["x"])
        Y.append(person["y"])
    plt.scatter(X, Y, color=color)


def get_pos_int_from_user(prompt):
    """
    Shows the prompt to the user and get a positive int from the user.
    """
    pos_int = input(prompt)
    while not pos_int.isdigit() or int(pos_int) < 1:
        pos_int = input(prompt)
    return int(pos_int)


def main():
    # Get information from the user
    world_size = get_pos_int_from_user("How large is the world? ")
    population = get_pos_int_from_user("How many people? ")
    percentage_stationary = get_pos_int_from_user("Percentage of people that are stationary (0-100)? ") / 100
    sim_steps = get_pos_int_from_user("How many simulation steps? ")

    # In order to keep updating matplotlib in the same window, turns on
    # interactive mode with plt.ion()
    plt.ion()

    # plt.show() only needs to be called once, after this call plt.draw() to
    # update the plot
    plt.show()

    # Each has a percentage_stationary chance of being stationary
    people = []
    for i in range(population):
        person = create_person(percentage_stationary, world_size)
        people.append(person)

    # Run the simulation for 'sim_steps' iterations
    for step_num in range(sim_steps):
        # plt.clf() will clear the current figure so we can re-draw it
        plt.clf()

        # Set the axes of our plot to the appropriate values
        plt.axis([0, world_size, 0, world_size])

        for person in people:
            move_person(person, world_size)

        # Plot the people
        plot(people, 'b')

        plt.title('Simulation Step #' + str(step_num))

        # To update the plot we call plt.draw() instead of plt.show()
        plt.draw()

        # A small pause is needed for pyplot to be able to draw the plot
        plt.pause(0.0001)


if __name__ == "__main__":
    main()
