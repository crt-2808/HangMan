import random
import WordList #Import list of words from WordList file
import States #Import live from States

#Step 1: Select a random from the list and global definition
selected_word=random.choice(WordList.words).lower()
end_game=False
live=6
#Step 2: Create blank spaces for the word
word_display=[]
word_len=len(selected_word)
for symbol in range(word_len):
    word_display+="_"
    
#Step 2.1: Print the logo of the game
print(States.logo)
#Step 3: Show the spaces of the word
print(word_display)

#Step 4: While cicle so the user can guess
while not end_game:    
    guess=input("Give me a letter that can be on the word: ").lower()
     #Step 4.1 If the letter is already guessed, let the user know
    if guess in word_display:
      print(f"You already guessed {guess}")
    #Step 5: Check if the letter is on the word
    for position in range(word_len):
        letter=selected_word[position]
        if letter==guess:
            word_display[position]=letter
        
    #Step 5.1: If the letter is not on the word, the player looses one live
    if guess not in selected_word:
        print(f"You guessed {guess} that is not in the word, you lose a live")
        live-=1
        #Step 5.1.1: Show the user they lost
        if live==0:
            end_game=True
            print(f"You lose. The word was {selected_word}")
  
    #Step 5.2:Print the word 
    print(f"{' '.join(word_display)}")    
    
    #Step 6: Show the user they have won
    if "_" not in word_display:
        end_game=True
        print("You win!")
    print(States.stages[live])