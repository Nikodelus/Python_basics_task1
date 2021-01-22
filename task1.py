import random
draw = random.randint(1, 100)

def guessing(num):
    guess = int(0)
    while guess != num:
        try:
            guess = int(input('Guess the number: '))
            if guess > num:
                print('Too big, try again')
            elif guess < num:
                print('Too small, try again')
            else:
                print('Tou win!')
        except ValueError:
            print("It's not a number, try again.")
    return

guessing(draw)

