import random
import hangman_art
import hangman_words
from replit import clear

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
print(f"your word {chosen_word}")
print(hangman_art.logo)
#display
display=[]
for letter in chosen_word:
  display +="_"
#set lives
lives = 6


end = False
while not end:
  #guess
  guess = input("guess a letter : ").lower()
  clear()
  if guess in display:
    print(f"letter is alreay exist {guess}")
  #check for letter = guess
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  print(" ".join(display))

  # reduce lives for a wrong guess
  if guess not in chosen_word:
    print(f"the letter {guess} is not in the word")
    lives -= 1
    if lives == 0:
      end = True
      print("you lose")

#make a end true if every letter are found
  if "_" not in display:
    end = True
    print("you won")

  print(hangman_art.stages[lives])

    
