import keyboard as kb
import random
global points
global streak
global coinside
points = 0
streak = 0
coinside = ['Heads', 'Tails']
def game():
    streak = 0
    points = 0
    print("Press SPACE to start.")
    kb.wait(' ')
    while True:
        cl = random.choice(coinside)
        pc = input("Choose a side. Heads or Tails: ")
        if cl == pc:
            print(f'The coin landed on {cl}! +1 point')
            streak = streak + 1
            points = points + 1
            print(f'Streak: {streak}')
            print(f'Current points: {points}')
        else:
            print(f'The coin landed on {cl}. -1 point')
            points = points - 1
            streak = 0
            print(f'Streak: {streak}')
            print(f'Current points: {points}')
game()
    

