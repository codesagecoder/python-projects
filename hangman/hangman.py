import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    #avoiding words with dash or space
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 6

    # we remove a correctly guessed letter from word_letters which further decreases word_letters
    # eventually arriving at 0
    # while ends when len(word_letters) == 0 OR when lives ==0
    while len(word_letters) > 0 and lives > 0:

        # SHOW LETTERS USED
        # ' '.join(['a','b','c']) --> 'a b c'
        # the list of used words will be seperated by a space since before
        # .join we specify using ' '(space)
        # a coma concatinates
        print('You have ',lives,'lives left and You have used these letters: ',' '.join(used_letters))

        # SHOW WHAT CURRENT WORD IS (e.g W - R D)
        # the for seperates this satement into two, not seperated at else.
        # if a letter in used_letters is found in word display it, if not (else) display a -(dash)
        # do this check for each letter in word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # getting user input from
        user_letter = input('Guess a letter: ').upper()

        # if user input is valid(only english alphabets) and also not icluded in
        # previously guessed letters(we minus used letter(used_letters) from alphabet set() ),
        # we add to used_letters
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # if the user input is in the word letters, we remove the user input letter from word_letters,
            # in order to avoid guesssing already guessed letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives-=1 # takes away a life if wrong
                print('letter is not in word.')
                
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')
    
    # once loop has ended we get here
    if lives == 0:
        print('You died. The word was',word)
    else:
        print('You guessed the word ',word, '!!')

hangman()