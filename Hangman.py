import json
import random
import hgDrawings as draw
import sys

x = json.load(open('german-cities.json'))  #extract the city names from the database
cityDatabase = x['data']
cities = []  #here are our cities stored
for i in cityDatabase:
    cities.append(i['name'])

for i in cities:  #fix broken german letters in the database
    if "Ã¶" in i:
        fixedWord = i.replace('Ã¶', 'ö')
        cities.append(fixedWord)
        cities.remove(i)
    if "Ã¼" in i:
        fixedWord = i.replace('Ã¼', 'ü')
        cities.append(fixedWord)
        cities.remove(i)

losingLine = ['You are gravely mistaken! Choose another!', 'Oops! One step closer to death!',
              'Another mistake! You can already feel the shivering gaze of the abyss!', 'Wrong!',
              'Incorrect!', 'Bad choice!', 'Unlucky!']
winningLine = ['And this is correct! Once more!', 'Correct! Pick again!', "You're right! Try again!", "Good job!",
               'Way to go!', 'Phenomenal!']

wordChosen = random.choice(cities)
wordChosen = wordChosen.upper()
wordLetters = set(wordChosen)
mistakeCounter = 0
answer = set()

print("Welcome to Galgenmännchen! This is a Hangman game, but using German cities. You have 6 tries. \n"
      "Umlauts are allowed. \n"
      "Type anything to start.")

input()

draw.hangman_lvl(mistakeCounter)

print("The word is:")
for i in wordChosen:
    print('_', end='')
print(" ")
print("Guess one letter!")


while mistakeCounter < 6:
    guess = input().upper()
    if not len(guess) == 1:
        print("You have to type ONE letter! Try again!")
        continue
    if not guess.isalpha():
        print("You have to type a letter! Try again!")
        continue
    if guess in answer:
        print("You have already picked this letter! Pick another one!")
        continue
    if guess not in wordChosen:
        mistakeCounter += 1
        if mistakeCounter == 6:
            draw.hangman_lvl(mistakeCounter)
            break
        draw.hangman_lvl(mistakeCounter)
        print(random.choice(losingLine))
    if guess in wordChosen:
        print(random.choice(winningLine))
        print(" ")
        answer.add(guess)
        for i in wordChosen:
            if i in answer:
                print(i, end='')
            else:
                print('_', end='')
        print('')
    if answer == wordLetters:
        print('')
        print("Congratulations! You have escaped the cold fingers of death. But for long?")
        sys.exit()

print("You lost. Your body is hanging helplessly on the rope. For mere seconds convulsions "
      "still pulsate through your body, \neerily jerking your limbs in a weird and uncanny dance. "
      "But soon even it comes to an end, this last movement of yours. \nYour face is blue, your tongue, swollen "
      "and thick, sticks out like an undercooked Bratwurst. Had you been \nstill be able of feeling, "
      "you'd feel a nasty cold trickle of feces down your left thigh. But \nthis is not the case. Alas! Your knowledge "
      "of German cities was insufficient to save you. \nNow there is nothing. Now you are dead.")
