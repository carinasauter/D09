from random import randint
from sys import argv


def mimsmind_game():


    if len(argv) > 1:
        length = int(argv[1])
    else:
        length = 1

    random_number = randint(10**(length - 1), 10**(length) - 1)
    print("Let's play the mimsmind0 game.\nGuess a {}-digit number: ".format(length))
    guessed_number = 0
    count = 1
    while random_number != guessed_number:
        try:
            guessed_number = int(input(""))
        except:
            print("You can only enter integers. Please try again: ")
            count +=1
            continue

        if random_number > guessed_number:
            print("Try again. Guess a higher number: ")
            count += 1
        elif random_number < guessed_number:
            print("Try again. Guess a lower number: ")
            count += 1
    if count == 1:
        print("Congratulations. You guessed the correct number in {} try.".format(count))
    else:
        print("Congratulations. You guessed the correct number in {} tries.".format(count))


def main():
    mimsmind_game()

if __name__ == '__main__':
    main()
