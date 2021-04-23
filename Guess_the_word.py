#Guess the word
import random


def introduction():
    global letter_count
    global turns
    #introduction
    print("\nLet's play Guess the Word")
    print(f"You have {turns} turns to guess the word!")
    #to show length of the word
    print(" _ "*letter_count)

def main():
    global turns
    global guesses
    global attempts
    while turns>0:
        guess = input("\n\nGuess a letter: ") #Let the user to enter a letter
        guess = guess.lower()
        if guess in secret:
            print("Correct guess.\n")
            guesses += guess  #Save the correct guesses in guesses
        else:
            print("Try again\n")
            turns -= 1 #counting guesses
            attempts += 1
            print(f"You have {turns} turns left.\n")
        #show correct guessed letters in correct place
        missed = 0
        for letter in secret:
            if letter in guesses:
                 print(' ', letter, ' ', end = '')
            else:
                print(' _ ', end = '')
                missed = 1
        if missed == 0 :
            print("\n\nCongratulations, you have won!")
            break
    else:
        print("\n\nSorry, you have loss.")

replay = ''
while replay.lower() != 'n':
    words = ['mathematics' , 'python' , 'enormity' , 'intelligence' , 'handkerchief' ]
    secret = random.choice(words)
    letter_count = len(secret)
    turns = letter_count
    guesses = ""
    attempts = 1
    introduction()
    main()
    print("You have tried {} attempts.".format(attempts))
    print(f"The secret word is {secret}")
    replay = input("\nDo you want to play again? (y/n)")
            
print("\nEnd of Game.")
