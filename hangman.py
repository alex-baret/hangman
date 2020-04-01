# Problem Set 2, hangman.py
# Name: Alex Baret
# Collaborators: None
# Time spent: 15 hours as of 3/24

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words7.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    checkGuess = [] #initializing empty list to collect letters that match
    list(secret_word) #setting secret word to string to compare elements(letters)
    for e in letters_guessed: #iterates through letters guessed
        if e in secret_word and secret_word.count(e) > checkGuess.count(e): #checking if the letter is in secret word and if it's occured less than the number of times in secret word
            checkGuess.append(e) #if the above is true, add to collection list, else don't add it 
    if len(checkGuess) == len(secret_word): #if the collection list equals the length of secret word, the word's been guessed, so return True, else False
        return True
    else: 
        return False



def get_guessed_word(secret_word, letters_guessed): #currently works but if there's a multiple in the list it doesn't record it, implement function above
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    checkGuess = []
    x = len(secret_word)
    for l in range(x):
        checkGuess.append("_")
    for char in letters_guessed:
        if char in secret_word:
            index = secret_word.find(char)
            if secret_word.count(char) > 1: #case if there's a duplicate letter
                # ----- first instance ---- #
                index = secret_word.find(char) #find the index of the letter in secret word
                checkGuess[index] = char #place the matched letter at the index of where it was found in the checking list
                # ------ 1+ instances ---- #
                secret_list = list(secret_word) #change secret word to list bc strings are immutable 
                while secret_list.count(char) != 1:
                    ind = secret_list.index(char) #find the first instance of the letter in the new mutable list
                    secret_list.remove(char) #take it out 
                    secret_list.insert(ind, "*") #replace at the index it used to be a placeholder
                    # print(secret_list) #check if everything above worked
                    secret_list2 = ''.join(secret_list) #put the list back into a string to find the 
                    index = secret_list2.find(char) #finds the second instance of the letter
                    checkGuess[index] = char #put the second instance of the letter into checking list
            else: #case if there isn't a duplicate letter
                checkGuess[index] = char 
    return(checkGuess)
            



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    string_guessed = ''.join(letters_guessed)
    letters = "abcdefghijklmnopqrstuvwxyz"
    for char1 in letters:
        for char2 in string_guessed:
            if char1 == char2:
                list_letters = list(letters)
                list_letters.remove(char1)
                letters = ''.join(list_letters)
                break
    return letters
                
    
def unique_letters(secret_word): #calculates number of unique letters in the word
    '''Checks how many unique letters are in secret_word.  
    Takes in a string as a parameter called "secret_word".'''
    num_letters = 0
    place_letters = []
    for char in secret_word: 
        num_letters += 1
        place_letters.append(char)
        if place_letters.count(char) > 1:
            num_letters -= 1
    return num_letters
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter! (I.E. check to make sure it's a letter)
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * At the start of each game the player starts with three warnings.  Each
      time they input something other than the alphabet they lose a warning. 3
      warnings gone and invalid input is entered,the player loses a guess.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    # # ---- Introduction -------- #
    # #secret_word = "apple"
    # secret_word = choose_word(wordlist)
    print(secret_word)
    letters_guessed =[]
    print("Welcome to Hangman!")
    print("I am thinking of a word that is", len(secret_word),"letters long.")
    warnings_remaining = 3 #three warnings to start
    guesses_remaining = 6
    print("You have",warnings_remaining,"warnings left.")
    print("------------------------------")
    
    while is_word_guessed(secret_word,letters_guessed) != True:
        #-----------------Round 1-----------------#
        print("You have",guesses_remaining,"guesses left.")
        print("You have",warnings_remaining,"warnings left.")
        print("Available Letters: ", get_available_letters(letters_guessed))
        single_letter = input("Please Guess a letter: ")
        print("------------------------------")
        if single_letter in secret_word:
                    letters_guessed.append(single_letter)
                    print("Good Guess: ",get_guessed_word(secret_word,letters_guessed))
        if single_letter not in secret_word and str.isalpha(single_letter) == True: #not in word and alphabetical
                if single_letter in ("aeiou"):  #not in word and it's a vowel
                    letters_guessed.append(single_letter)
                    guesses_remaining -= 2
                else:
                    letters_guessed.append(single_letter)
                    guesses_remaining -= 1
                    print("Oops! That letter is not in my word: ",get_guessed_word(secret_word,letters_guessed))
        if single_letter not in secret_word and str.isalpha(single_letter) != True: #not in word also non-alphabet
                    letters_guessed.append(single_letter)
                    if warnings_remaining > 0:
                        warnings_remaining -= 1
                        print("Not a valid letter.  You have: ",warnings_remaining,"warnings remaining")
                    else:
                        guesses_remaining -= 1
                        print("Not a valid letter and you lost a guess: ",get_guessed_word(secret_word,letters_guessed))
        if letters_guessed.count(single_letter) > 1: 
                if warnings_remaining > 0:
                    warnings_remaining -= 1          
                    print("Oops! You've already guessed that letter. You now have",warnings_remaining,"warnings:",get_guessed_word(secret_word,letters_guessed))
                if warnings_remaining <= 0:
                    guesses_remaining -= 1
                    print("Sorry you're out of warnings, therefore you lost a guess")
        #--------------Rounds 2-6------------------- #
        while guesses_remaining > 0:
            print("You have",guesses_remaining,"guesses left.")
            print("You have",warnings_remaining,"warnings left.")
            print("Available Letters: ", get_available_letters(letters_guessed))
            single_letter = input("Please Guess a letter: ")
            print("------------------------------")
            # if single_letter.isalpha == True: #checking if the input is part of the alphabet
            if single_letter in secret_word:
                    letters_guessed.append(single_letter)
                    print("Good Guess: ",get_guessed_word(secret_word,letters_guessed))
            
            if single_letter not in secret_word and str.isalpha(single_letter) == True: #not in word and alphabetical
                if single_letter in ("aeiou"):  #not in word and it's a vowel
                    letters_guessed.append(single_letter)
                    guesses_remaining -= 2
                else:
                    letters_guessed.append(single_letter)
                    guesses_remaining -= 1
                    print("Oops! That letter is not in my word: ",get_guessed_word(secret_word,letters_guessed))
            if single_letter not in secret_word and str.isalpha(single_letter) != True: #not in word also non-alphabet
                    letters_guessed.append(single_letter)
                    if warnings_remaining > 0:
                        warnings_remaining -= 1
                        print("Not a valid letter.  You have: ",warnings_remaining,"warnings remaining")
                    else:
                        guesses_remaining -= 1
                        print("Not a valid letter and you lost a guess: ",get_guessed_word(secret_word,letters_guessed))
            if letters_guessed.count(single_letter) > 1: 
                if warnings_remaining > 0:
                    warnings_remaining -= 1          
                    print("Oops! You've already guessed that letter. You now have",warnings_remaining,"warnings:",get_guessed_word(secret_word,letters_guessed))
                else:
                    guesses_remaining -= 1
                    print("Sorry you're out of warnings, therefore you lost a guess.")
            # if is_word_guessed(secret_word, letters_guessed) == True:
            #         break
    # ------------- End of Game Check for Victory/Loss -------- #
    if is_word_guessed(secret_word,letters_guessed) != True:
            print("You ran out of guesses :/ Game Over. The word is: ",secret_word)
    else: 
        print("Congrats!  You got it. The word is: ", secret_word)
        total_score = (guesses_remaining * unique_letters(secret_word))
        print("Your score for this game is: ", total_score )

    
    
    
    
    
    
#    pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(letters_guessed, secret_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    word = get_guessed_word(secret_word,letters_guessed)
    joined_guess = ''.join(word)
    if len(joined_guess) == len(secret_word):
        for char1 in joined_guess: 
            for char2 in secret_word:
                if char1 == char2: 
                    return True
                else: 
                    return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
            Keep in mind that in hangman when a letter is guessed, all the positions
            at which that letter occurs in the secret word are revealed.
            Therefore, the hidden letter(_ ) cannot be one of the letters in the word
            that has already been revealed.

    '''
    joined_guess = ''.join(get_guessed_word)
    # stripped_guess = joined_guess.strip(" ")
    for i in wordlist: 
        if len(i) == len(joined_guess):
            for char1 in joined_guess: 
                for char2 in i:
                    if char1 == char2: 
                        print(i)
                    else: 
                        print("No Possible Matches.")

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # # ---- Introduction -------- #
    # #secret_word = "apple"
    # secret_word = choose_word(wordlist)
    print(secret_word)
    letters_guessed =[]
    print("Welcome to Hangman!")
    print("I am thinking of a word that is", len(secret_word),"letters long.")
    warnings_remaining = 3 #three warnings to start
    guesses_remaining = 6
    print("You have",warnings_remaining,"warnings left.")
    print("------------------------------")
    
    while is_word_guessed(secret_word,letters_guessed) != True:
        #-----------------Round 1-----------------#
        print("You have",guesses_remaining,"guesses left.")
        print("You have",warnings_remaining,"warnings left.")
        print("Available Letters: ", get_available_letters(letters_guessed))
        single_letter = input("Please Guess a letter: ")
        print("------------------------------")
        if single_letter in secret_word:
                    letters_guessed.append(single_letter)
                    print("Good Guess: ",get_guessed_word(secret_word,letters_guessed))
        if single_letter not in secret_word and str.isalpha(single_letter) == True: #not in word and alphabetical
                if single_letter in ("aeiou"):  #not in word and it's a vowel
                    letters_guessed.append(single_letter)
                    guesses_remaining -= 2
                else:
                    letters_guessed.append(single_letter)
                    guesses_remaining -= 1
                    print("Oops! That letter is not in my word: ",get_guessed_word(secret_word,letters_guessed))
        if single_letter not in secret_word and str.isalpha(single_letter) != True: #not in word also non-alphabet
                    letters_guessed.append(single_letter)
                    if warnings_remaining > 0:
                        warnings_remaining -= 1
                        print("Not a valid letter.  You have: ",warnings_remaining,"warnings remaining")
                    else:
                        guesses_remaining -= 1
                        print("Not a valid letter and you lost a guess: ",get_guessed_word(secret_word,letters_guessed))
        if letters_guessed.count(single_letter) > 1: 
                if warnings_remaining > 0:
                    warnings_remaining -= 1          
                    print("Oops! You've already guessed that letter. You now have",warnings_remaining,"warnings:",get_guessed_word(secret_word,letters_guessed))
                if warnings_remaining <= 0:
                    guesses_remaining -= 1
                    print("Sorry you're out of warnings, therefore you lost a guess")
        #--------------Rounds 2-6------------------- #
        while guesses_remaining > 0:
            print("You have",guesses_remaining,"guesses left.")
            print("You have",warnings_remaining,"warnings left.")
            print("Available Letters: ", get_available_letters(letters_guessed))
            single_letter = input("Please Guess a letter: ")
            print("------------------------------")            
            
            if single_letter not in secret_word and str.isalpha(single_letter) != True and single_letter == '$':
                letters_guessed.append(single_letter)
                if match_with_gaps(letters_guessed, secret_word) == True:
                    print(show_possible_matches(letters_guessed))
            
            if single_letter in secret_word:
                    letters_guessed.append(single_letter)
                    print("Good Guess: ",get_guessed_word(secret_word,letters_guessed))
            
            if single_letter not in secret_word and str.isalpha(single_letter) == True: #not in word and alphabetical
                if single_letter in ("aeiou"):  #not in word and it's a vowel
                    letters_guessed.append(single_letter)
                    guesses_remaining -= 2
                else:
                    letters_guessed.append(single_letter)
                    guesses_remaining -= 1
                    print("Oops! That letter is not in my word: ",get_guessed_word(secret_word,letters_guessed))
            if single_letter not in secret_word and str.isalpha(single_letter) != True: #not in word also non-alphabet
                    letters_guessed.append(single_letter)
                    if warnings_remaining > 0:
                        warnings_remaining -= 1
                        print("Not a valid letter.  You have: ",warnings_remaining,"warnings remaining")
                    else:
                        guesses_remaining -= 1
                        print("Not a valid letter and you lost a guess: ",get_guessed_word(secret_word,letters_guessed))
            if letters_guessed.count(single_letter) > 1: 
                if warnings_remaining > 0:
                    warnings_remaining -= 1          
                    print("Oops! You've already guessed that letter. You now have",warnings_remaining,"warnings:",get_guessed_word(secret_word,letters_guessed))
                else:
                    guesses_remaining -= 1
                    print("Sorry you're out of warnings, therefore you lost a guess.")
            # if is_word_guessed(secret_word, letters_guessed) == True:
            #         break
        # ------------- End of Game Check for Victory/Loss -------- #
        if is_word_guessed(secret_word,letters_guessed) != True:
            print("You ran out of guesses :/ Game Over. The word is: ",secret_word)
        else: 
            print("Congrats!  You got it. The word is: ", secret_word)
            total_score = (guesses_remaining * unique_letters(secret_word))
            print("Your score for this game is: ", total_score )



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
    # pass

#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
