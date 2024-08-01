import random
from words import wordbank
import string

def get_valid_word(wordbank):
    word = random.choice(wordbank) #choose a random word
    while '-' in word or ' ' in word:
        word = random.choice(wordbank)

    return word.upper()

def hangman():
    word = get_valid_word(wordbank)
    word_letters = set(word)
    alphabet = set(string.ascii_letters)
    used_letters = set()

    while len(word_letters)>0:

        print('you have used this characters: ',' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))

        user_letter = input('guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('you have already use that character. Please try again')
    
        else:
            print('invalid character. Please try again')

    print('yay you guess the word. '+ word)


if __name__ == '__main__':
    hangman()