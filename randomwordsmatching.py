import random
stages=["you lost your health 6","you lost your health 5","you lost your health 4","you lost your health 3","you lost your health 2","you lost your health 1"]
words=["ant","ball","cat"]
lives=6
choose_word=random.choice(words)
print(choose_word)
place_holder=""
word_length=len(choose_word)
for position in range(word_length):
    place_holder +="_ "
print(place_holder)
game_over=False
correct_letters=[]
while not game_over:
    guess=input("Guess the letter: ").lower()
    print(guess)
    if guess in correct_letters:
        print(f"You already guessed the letter")
    display=""
    for letter in choose_word:
        if letter==guess:
            display+=(letter)
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=(letter)
        else:
            display+=("_ ")
    print(display)
    if guess not in choose_word:
        lives-=1
        if lives==0:
            game_over=True
            print(f"It is the correct word is {choose_word} You lose")
    if "_" not in display:
        game_over=True
        print("You win")
    if lives > 0 and lives <= 6:
        print(stages[6-lives])
