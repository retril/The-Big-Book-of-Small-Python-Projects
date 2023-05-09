import random

# number of digits to guess
num_digits = 3

max_guesses = 10

print("Bagels is a logic game for deduction")
print('''
I mean a {}-digit number in which none of the digits are repeated. 
Try to guess it. Here are the clues: 
When I say -> it means: 
Pico -> One digit is correct, but it is in the wrong position. 
Fermi -> One digit is correct and is in the right position. 
Bagels -> No digit is correct.
For example, if the secret number is 248 and you enter the number 843, 
the clue will be Fermi Piko.'''.format(num_digits))


def getSecretNum():
    numbers = list('0123456789')  # List of digits from 0 to 9.
    random.shuffle(numbers)

    # Add first three digits from numbers list to secretNum
    secret_num = ''
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num

def IsNumberEQ(secretnum, number):
    if number == secretnum:
        return 'You find the right answer'

    clues = []
    for i in range(3):
        if secretnum[i] == number[i]:
            clues.append('Fermi')
        elif secretnum[i] in number:
            clues.append('Piko')
    if len(clues) == 0:
        clues.append('Bajgle')

    clues.sort()
    return clues


while True:
    secret_num = getSecretNum()
    print("Let's start!")
    print("You have {} attempts ".format(max_guesses))
    attepts = 1
    while attepts <= max_guesses:
        guess = ''
        while len(guess) != num_digits or not guess.isdecimal():
            print('Attempt #{}: '.format(attepts))
            guess = input('> ')

        clues = IsNumberEQ(secret_num, guess)
        print(clues)
        attepts += 1

        if guess == secret_num:
            break
        if attepts > max_guesses:
            print('You have used all attempts.')
            print('The correct answer is: {}.'.format(secret_num))

    print('Do you wanna play one more time? (yes or no)')
    if not input('> ').lower().startswith('y'):
        break
    print('Thanks for game!')