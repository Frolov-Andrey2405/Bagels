import random

# Configuration
NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print_intro()

    while True:
        secret_num = generate_secret_number()
        print('I have thought up a number.')
        print(f' You have {MAX_GUESSES} guesses to get it.')

        for num_guesses in range(1, MAX_GUESSES + 1):
            guess = get_valid_guess(num_guesses)
            clues = get_clues(guess, secret_num)
            print(clues)

            if guess == secret_num:
                print('You got it!')
                break

            if num_guesses == MAX_GUESSES:
                print(f'You ran out of guesses. The answer was {secret_num}.')

        play_again = input('Do you want to play again? (yes or no) ').lower()
        if not play_again.startswith('y'):
            break

    print('Thanks for playing!')


def print_intro():
    print(f'''The deductive logic game "Bagels"
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.''')


def generate_secret_number():
    numbers = random.sample('0123456789', NUM_DIGITS)
    return ''.join(numbers)


def get_valid_guess(num_guesses):
    while True:
        guess = input(f'Guess #{num_guesses}: ')
        if len(guess) != NUM_DIGITS or not guess.isdecimal():
            print('Invalid input. Please enter a valid guess.')
        else:
            return guess


def get_clues(guess, secret_num):
    if guess == secret_num:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if not clues:
        return 'Bagels'
    clues.sort()
    return ' '.join(clues)


if __name__ == '__main__':
    main()
