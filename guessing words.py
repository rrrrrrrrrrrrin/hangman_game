from random import choice
from body import body
from words import words

guessed_words = []

print("Let's play the hangman game!")


def get_word():
    return choice(words)


def display_hangman(attempts):
    return body[attempts]


def play(guessed_words, word):
    attempts = 6
    word_completion = ['_'] * len(word)
    inserted_letters, guessed_letters = [], []

    if input('Show first and last letters? (y/n): ') == 'y':
        guessed_letters.append([word[0], word[-1]])
        word_completion = list(word[0] + '_' * (len(word) - 2) + word[-1])

    print(display_hangman(attempts), *word_completion, sep='')

    while True:
        letter = input('Enter a letter: ').lower()
        if letter in [chr(i) for i in range(97, 123)]:
            if letter in word and letter not in guessed_letters:

                for count in range(len(word)):
                    if word[count] == letter:
                        word_completion[count] = letter

                inserted_letters.append(letter)
                guessed_letters.append(letter)
                print(*word_completion)

            elif letter in inserted_letters and '_' in word_completion:
                print('You have already inserted this letter. Repeat your attempt')
                continue

            else:
                attempts -= 1
                inserted_letters.append(letter)
                print(display_hangman(attempts), *word_completion, sep='')

        if '_' not in word_completion:
            guessed_words.append(word)
            print('Congrats, you guessed a word!')
            break

        if attempts == 0:
            print(f'Game over. The estimated word is {word}')
            break

        else:
            continue


while True:
    play(guessed_words, get_word())
    if input('Start a new game? (y/n): ') != 'y':
        print('Guessed words of yours:', end=' ')
        print(*guessed_words, sep=', ')
        break
