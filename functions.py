import random, time, warnings

answers = ['spear', 'alone', 'broke', 'forge', 'gripe', 'phone', 'yodle', 'peach', 'sport', 'mural', 'cloud', 'flake', 'would', 'brute', 'grind', 'alike', 'cream', 'viral', 'joint', 'quack', 'boxer', 'juice', 'merit', 'alien', 'sugar', 'equal', 'prism', 'crank', 'young', 'mount', 'flick', 'plant', 'cloth']

def directions_screen():
    directions = input('See directions? (type y or n)\n')
    if directions == 'y':
        print(
            '- : that letter is not in the answer\n! : that letter is in the word, but a different location\nthe letter : it is in the correct place.'
        )
    return

def answer():
    #answer = answers[random.randint(0, len(answers)-1)]
    answer = random.choice(answers)
    la = list(answer)
    return la

def guess_fix(word: str):
    warnings.warn("Guess must be 5 letters")
    if len(word) > 5:  # first 5 characters only
        fixed_word = word[:5]
    elif len(word) < 5:  # add - up to 5 characters
        fixed_word = word + (5 - len(word)) * "-"
    return fixed_word

def run_game():
    list_answer = answer()
    guess = str(input('\nGuess a 5 letter word: '))
    if len(guess) != 5:
        guess = guess_fix(guess)
    guess_list = list(guess.lower())

    #result = 5*['-']
    correctGuess = False
    guessCount = 1
    allGuesses, allResults = [], []
    while correctGuess == False:
        result = 5*['-']
        for i in range(len(list_answer)):
            if guess_list[i] not in list_answer:
                result[i] = "-" # or use " " ??
            elif guess_list[i] == list_answer[i]:
                #result[i] ="o"
                result[i] = guess_list[i]
            elif guess_list[i] in list_answer and result[i] == "-":
                result[i] = "!"

        allGuesses.append(guess_list)
        allResults.append(str(result))
        print('Your Guess #' + str(guessCount))
        print(guess_list)
        print('Result: ')
        print(result)
        if guess_list == list_answer:
            correctGuess = True
            print('\nYou win! (' + str(guessCount) + r'/6)')
            for i in range(len(allGuesses)):
                time.sleep(0.6)
                print(allResults[i])
        elif guessCount == 6:
            print('6 guesses reached!')
            print('the word was ' + ''.join(list_answer))
            for i in range(len(allGuesses)):
                print(allResults[i])
            break
        else:
            guessCount+=1
            guess = str(input('\nGuess a 5 letter word: '))
            if len(guess) != 5:
                guess = guess_fix(guess)
            guess_list = list(guess.lower())

    playAgain = input('\nplay again? (y or n)\n')
    if playAgain != 'y': playAgain='n'
    return playAgain

# not in use - get words from text file
def get_words():
    words_file = open('words.txt', 'r')
    words = words_file.read()
    word_list = words.split('\n')
    for i in range(len(word_list)):
        word_list[i] = word_list[i].lower()
    return word_list
