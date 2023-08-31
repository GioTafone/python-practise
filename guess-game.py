num_to_guess = 9
guess_count = 0
guess_limit = 3

print('Welcome! try to guess a number between 0 and 9. You only have 3 try :)')
while guess_count < guess_limit:
    guess = int(input('Guess the number: '))
    guess_count += 1
    if guess == num_to_guess:
        print('Correct!!')
        break
else:
    print('You ran out of try')
