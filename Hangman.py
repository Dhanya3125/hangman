import random

def choose_word():
    words = ['python', 'hangman', 'programming', 'developer', 'computer', 'keyboard', 'laptop', 'challenge']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def display_hangman(incorrect_guesses):
    hangman_stages = [
        '''
           ------
           |    |
                |
                |
                |
                |
         =========
        ''',
        '''
           ------
           |    |
           O    |
                |
                |
                |
         =========
        ''',
        '''
           ------
           |    |
           O    |
           |    |
                |
                |
         =========
        ''',
        '''
           ------
           |    |
           O    |
          /|    |
                |
                |
         =========
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
                |
                |
         =========
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
         =========
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
         =========
        '''
    ]
    print(hangman_stages[incorrect_guesses])

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord: " + display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        display_hangman(incorrect_guesses)
        
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! '{guess}' is not in the word.")
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word!")
            print(f"The word was: {word}")
            break
    else:
        print("\nSorry, you've run out of guesses.")
        print(f"The word was: {word}")

hangman()
