'''
FUNCTION: Simulates infection spread.
AUTHOR: Amber Morgan
'''


import matplotlib.pyplot as plt
import random
import math


def create_person(stationary_prob, world_size):
    """
    Creates a person. A person is represented by a dictionary with 3 or 5 keys: stationary, x, y,
    and possibly dest_x and dest_y. Stationary is a bool, and the others are integers that are
    initialized to a random value from 0 to world_size.
    """
    person = {'stationary': True,
              'x':random.randint(0, world_size), 'y':random.randint(0, world_size)}
    if random.random() >= stationary_prob:
        # A mobile (non-stationary) person
        person['stationary'] = False
        person['dest_x'] = random.randint(0, world_size)
        person['dest_y'] = random.randint(0, world_size)
    return person


def move_person(person, world_size):
    """
    Move a person slightly closer to their destination. If they are stationary, then nothing
    happens. Otherwise, their location gets one step closer in each direction (if possible)
    to the destination. If, after moving, they have reached their destination, then a new
    random destination is created.
    """
    if person['stationary']:
        return # stationary people don't move

    # Update the X coordinate
    if person['x'] > person['dest_x']:
        person['x'] -= 1
    elif person['x'] < person['dest_x']:
        person['x'] += 1

    # Update the Y coordinate
    if person['y'] > person['dest_y']:
        person['y'] -= 1
    elif person['y'] < person['dest_y']:
        person['y'] += 1

    # If the person has reached their destination, update the destination
    if person['x'] == person['dest_x'] and person['y'] == person['dest_y']:
        person['dest_x'] = random.randint(0, world_size)
        person['dest_y'] = random.randint(0, world_size)


def plot(people, color):
    """
    Plots a list of people that are each represented as a dictionary with the keys x and y using
    using a scatter plot. The color of the dots is given. This is done efficiently by only calling
    plt.scatter(...) once with lists of all of the x and y values of all the people.
    """
    # Build the X and Y lists to be plotted
    X = []
    Y = []
    for person in people:
        X.append(person['x'])
        Y.append(person['y'])

    # Make the scatter plot
    plt.scatter(X, Y, color=color)


def get_pos_int_from_user(prompt):
    """
    Shows the prompt to the user and gets a positive int from the user.
    """
    num = input(prompt).strip()
    while not num.isdigit() or int(num) < 1:
        num = input("Invalid positive integer, try again: ").strip()
    return int(num)


def get_int_between_0_and_100_from_user(prompt):
    """
    Shows the prompt to the user and gets an int between 0 and 100 from the user.
    """
    num = input(prompt).strip()
    while not num.isdigit() or int(num) > 100:
        num = input("Invalid value, must be integer from 0 to 100, try again: ").strip()
    return int(num)


def distance(person1, person2):
    """
    Calculates and returns the distance between two people. Both people are dictionaries that
    have "x" and "y" keys.
    """
    x1 = person1["x"]
    x2 = person2["x"]
    y1 = person1["y"]
    y2 = person2["y"]
    total_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total_distance


def spread_infection(healthy, infected, infection_range):
    """
    Checks the distance between all infected and healthy people (pairwise). If any healthy person
    is closer to an infected person than infection_range, they become infected.
    """
    for infected_person in infected:
        for healthy_person in healthy:
            if distance(infected_person, healthy_person) <= infection_range:
                infected.append(healthy_person)
                healthy.remove(healthy_person)


def who_will_recover(steps_infected, num_steps_to_recovery):
    """
    Identifies which of the infected peoples will recover in this simulation step.
    
    steps_infected is a list of integers for how many steps each person has been infected for.
    steps_to_recovery is the number of steps required for a person to recover.

    This function returns the index of each person that has been infected for at least
    steps_to_recovery while also incrementing the number of steps for each infected person.
    """
    will_recover = []
    for i in range(len(steps_infected)):
        steps_infected[i] += 1
        if steps_infected[i] > num_steps_to_recovery:
            will_recover.append(i)
    return will_recover


def main():
    # Gets information from the user
    world_size = get_pos_int_from_user("How large is the world? ")
    population = get_pos_int_from_user("How many people? ")
    perc_stationary = get_int_between_0_and_100_from_user("Percentage of people that are stationary (0-100)? ") / 100
    infection_range = get_pos_int_from_user("How far away can a person get to an infected person and become infected? ")
    steps_to_recovery = get_pos_int_from_user("How many steps does it take for a person to recover? ")
    sim_steps = get_pos_int_from_user("How many simulation steps? ")

    # In order to keep updating matplotlib in the same window, turn on
    # interactive mode with plt.ion()
    plt.ion()

    # plt.show() only needs to be called once, after this call plt.draw() to
    # update the plot
    plt.show()

    # Create a list containing 'population' different people
    people = []
    for _ in range(population):
        people.append(create_person(perc_stationary, world_size))

    # Make lists of healthy, infected, and recovered people
    # The first person in the 'people' list is the only initially infected person
    # All other people are healthy. The recovered list starts out empty
    healthy = people[1:]
    infected = [people[0]]
    steps_infected = [0] # the first infected person just became infected
    recovered = []

    # Lists to record the Y values of the number of healthy, infected, and recovered people during
    # each simulation step. They start out with the initial population setup.
    Y_healthy = [len(healthy)]
    Y_infected = [len(infected)]
    Y_recovered = [len(recovered)]

    # Run the simulation for 'sim_steps' iterations
    for step_num in range(sim_steps):
        # Check if the disease is eradicated
        if len(infected) == 0:
            break

        # plt.clf() will clear the current figure so we can re-draw it
        plt.clf()

        # Set the axes of our plot to the appropriate values
        plt.axis([0, world_size, 0, world_size])

        # Move all people
        for person in people:
            move_person(person, world_size)

        # Spread the infection among the populace
        spread_infection(healthy, infected, infection_range)
        for i in range(len(steps_infected), len(infected)):
            steps_infected.append(0)

        # Find the individuals who have recovered (and move the to the recovered list)
        will_recover = who_will_recover(steps_infected, steps_to_recovery)
        for i in reversed(will_recover):
            recovered.append(infected.pop(i))
            steps_infected.pop(i)

        plot(healthy, "green")
        plot(infected, "red")
        plot(recovered, "blue")

        Y_healthy.append(len(healthy))
        Y_infected.append(len(infected))
        Y_recovered.append(len(recovered))

        # Set plot title to include the current number of healthy, infected, & recovered people
        plt.title("Healthy: {}, Infected: {}, Recovered: {}".format(len(healthy), len(infected), len(recovered)))

        # To update the plot we call plt.draw() instead of plt.show()
        plt.draw()

        # A small pause is needed for pyplot to be able to draw the plot
        plt.pause(0.00001)
    
    # Display some useful information
    if step_num == sim_steps - 1:
        print("Disease not eradicated after %d steps" % sim_steps)
        print("There are %d healthy people, %d infected people, and %d recovered people" %
            (len(healthy), len(infected), len(recovered)))
    else:
        print("Disease eradicated after %d steps" % step_num)
        print("There are %d healthy people and %d recovered people" %
            (len(healthy), len(recovered)))
    print("The peak number of infected people was %d" % max(Y_infected))

    # Close the current figure and turn off interactive mode before the final plot
    plt.close()
    plt.ioff()

    #plt.plot(range(len(Y_healthy)), Y_healthy, color="green", label="Healthy")
    #plt.plot(range(len(Y_infected)), Y_infected, color="red", label="Infected")
    #plt.plot(range(len(Y_recovered)), Y_recovered, color="blue", label="Recovered")
    plt.stackplot(range(len(Y_healthy)), Y_healthy, Y_infected, Y_recovered, colors=["green", "red", "blue"])
    plt.ylabel("Number of People")
    plt.xlabel("Time")
    plt.title("Infection/Recovery Rate")
    plt.legend(["Healthy", "Infected", "Recovered"])
    plt.show()
    # The three lines should be the same colors as their respective dots earlier


# least 4 different sets of starting values and 5 trials), then collect your data, average your
# results and the summarize them here.
#
# Control Group
# Trial 1: 500, 1000, 50, 10, 100, 1000; eradicated after 585 steps, 150 healthy, 850 recovered, 426 peak
# Trial 2: 500, 1000, 50, 10, 100, 1000; eradicated after 534 steps, 153 healthy, 847 recovered, 466 peak
# Trial 3: 500, 1000, 50, 10, 100, 1000; eradicated after 491 steps, 156 healthy, 844 recovered, 531 peak infected
# Average: 327 steps, 153 healthy, 847 recovered, 474 peak infected
#
# Hypotheses:
# 1. As size of world increases, rate of infection will decrease because there will be more distance between people.
# Trial 1: 2500, 1000, 50, 10, 100, 1000; eradicated after 189, 996 healthy, 4 recovered, 4 peak infected
# Trial 2: 2500, 1000, 50, 10, 100, 1000; eradicated after 100, 999 healthy, 1 recovered, 1 peak infected
# Trial 3: 2500, 1000, 50, 10, 100, 1000; eradicated after 100, 999 healthy, 1 recovered, 1 peak infected
# Average: 130 steps, 998 healthy, 2 recovered, 2 peak infected
# This supports the hypothesis. The peak infection and number recovered were significantly lower the the control.
#
# 2. As the percent of stationary people increases, the rate of infection will decrease.
# Trial 1: 500, 1000, 95, 10, 100, 1000; eradicated after 100 steps, 998 healthy, 2 recovered, 2 peak
# Trial 2: 500, 1000, 50, 10, 100, 1000; eradicated after 100 steps, 995 healthy, 5 recovered, 5 peak
# Trial 3: 500, 1000, 70, 10, 100, 1000; eradicated after 100 steps, 998 healthy, 2 recovered, 2 peak
# Average: 100 steps, 997 healthy, 3 recovered, 3 peak infected
# This supports the hypothesis. The peak infection and number recovered are significantly lower than the control.
#
# 3. As the number of steps that people take to recover decreases, it will increase the rate of recovery, and people
# won't be infectious as long.
# Trial 1: 500, 1000, 50, 10, 25, 1000; eradicated after 56 steps, 990 healthy, 10 recovered, 9 peak
# Trial 2: 500, 1000, 50, 10, 25, 1000; eradicated after 372 steps, 643 healthy, 357 recovered, 70 peak
# Trial 3: 500, 1000, 50, 10, 25, 1000; eradicated after 82 steps, 993 healthy, 7 recovered, 4 peak
# Average: 170 steps, 875 healthy, 125 recovered, 28 peak
# This supports the hypothesis. The peak was lower than the control, and less steps were taken.

if __name__ == "__main__":
    main()
