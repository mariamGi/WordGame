# with this code user will guess the random word
import random

word_range = ['pen', 'pencil', 'notebook', 'Royal', 'piano', 'Mellotron']
guess_word = random.choice(word_range)
word = '-' * len(guess_word)  # quantity of the letter in word
chance = (len(guess_word))
# definition of the word_range's words
if guess_word == word_range[0] or guess_word == word_range[1] or guess_word == word_range[2]:
    print('it is most usable school subject')
elif guess_word == word_range[3] or guess_word == word_range[4] or guess_word == word_range[5]:
    print('it is musical Keyboard instrument')

game_over = False
while not game_over:
    print(f'you have {chance} tries.  ')
    print(word)
    guess = input('enter one letter')
    i = 0
    chance -= 1
    if guess in guess_word:
        while guess_word.find(guess, i) != -1:
            i = guess_word.find(guess, i)
            word = word[:i] + guess + word[i + 1:]
            i += 1
            print(word)
    else:
        print('sorry wrong letter')
    if guess == guess_word:
        print('congratulation, you Won')
        game_over = True
    if chance == 0:
        print('no more chances, Game Over')
        game_over = True
