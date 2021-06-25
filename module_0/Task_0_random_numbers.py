import numpy as np


def comp_guess(num_min, num_max, num_random):
    count = 1  # define initial number of attempts
    guess = (num_min + num_max) // 2  # first guess is given by division of the main interval in two halves
    while guess != num_random:  # do until correct
        count += 1  # increase number of attempts
        guess = (num_min + num_max) // 2  # update guess after each attempt
        if guess > num_random:
            num_max = guess  # update upper limit of the interval
        elif guess < num_random:
            num_min = guess + 1  # update lower limit of the interval
    return count  # end if guess is correct and return number of attempts


def ask_for_interval():  # ask to define the interval and check for basic self-consistency
    while True:
        a = input("Enter lower bound of the interval: ")
        b = input("Enter upper bound of the interval: ")

        if not(a.lstrip('-').isdigit()) or not(b.lstrip('-').isdigit()):
            print("Enter digits! ")
            continue

        a, b = int(a), int(b)

        if a > b:
            print("The lower bound must be smaller than upper. Try again ")
            continue

        return a, b


lower, upper = ask_for_interval()  # define interval [lower, upper]. Although, can be defined without asking
number = np.random.randint(lower, upper + 1)  # generate random number in the interval [lower, upper]

print(f"Computer used {comp_guess(lower, upper, number)} attempts to "
      f"find the integer {number} in interval {lower, upper}")
