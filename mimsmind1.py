from random import randint
from sys import argv


def mimsmimd_game():
    if len(argv) > 1:
        length = int(argv[1])
    else:
        length = 3
    random_number = randint(10**(length - 1), 10**(length) - 1)
    random_number = make_number_right(random_number, length)
    guessed_number = 0
    count = 1
    maxrounds = (2**length) + length
    guessed_correctly = False
    prompt = "Let's play the mimsmind1 game. You have {} guesses.\nGuess a {}-digit number: ".format(
        maxrounds, length)
    while random_number != guessed_number and count <= maxrounds:
        user_input = input(prompt)
        if len(user_input) != length:
            user_input = input("Invalid input. Try again: ")
        try:
            int(user_input)
        except:
            user_input = input("Invalid input. Try again: ")
        count += 1
        bulls = 0
        cows = 0
        if user_input == random_number:
            guessed_correctly = True
            print(("Congratulations! You guessed the correct number in {} tries!".format(
                count)))
            break

        lst_random = list(random_number)
        lst_input = list(user_input)
        cow_lst = list()
        for c, d in zip(lst_random, lst_input):
            if c == d:
                bulls += 1
            else:
                if d in lst_random and d not in cow_lst:
                    cows += 1
                    cow_lst.append(d)
        prompt = ("bull(s): {}, cow(s): {}. {}".format(
            bulls, cows, "" if count == maxrounds else "Try again: "))
    if not guessed_correctly:
        print("Sorry, you are out of tries. The correct number was {}.".format(
            random_number))


def make_number_right(number, length):
    if int(number) < (10**(length - 1)):
        number = str(number)
        number = "0" * (length - len(number)) + number
        return number
    return str(number)

mimsmimd_game()
