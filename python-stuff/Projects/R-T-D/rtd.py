import keyboard as kb
import random as rand
#Variables
d = [1, 2, 3, 4, 5, 6]
points = 0
wins = 0
losses = 0
dv = rand.randrange(1, 7) 

while True:
   while kb.is_pressed('s') == False:
      dv = rand.randrange(1, 7)
      #prompts the player and assigns the input to the variable
      pi = (int(input("Pick a number from 1 to 6: ")))
      #checks if input is valid
      if (pi not in d):
         print("Not a valid number.\n")
         continue
      #lose
      if dv == pi:
         print(f"the dice landed on{dv}, you lose :(")
         print("Press SPACE to continue\n")
         kb.wait(' ')
         losses = (losses + 1)
      #win
      if dv != pi:
         print(f"the dice landed on {dv}, You win! :D")
         print(f"Added 1 point. Current points: {points}")
         print("Press SPACE to continue\n")
         wins = (wins + 1)
         points = (points + 1)
         kb.wait(' ')
   #shows stats W.I.P
   if kb.is_pressed('s') == True:
      print(f'Stats: Points: {points}, Wins: {wins}, Losses: {losses}\n')
   continue