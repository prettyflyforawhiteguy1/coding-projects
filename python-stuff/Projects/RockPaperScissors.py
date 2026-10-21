import random
while True:
    rpsc = ["Rock", "Paper", "Scissors"]
    uc = input("Rock, Paper, or Scissors: ")
    cpuc = random.choice(rpsc)
    if cpuc == "Rock" and uc == "Rock":
     print("Rock vs Rock. It's a tie!")
    if cpuc == "Rock" and uc == "Paper":
     print("Rock vs Paper. Paper wins!")
    if cpuc == "Rock" and uc == "Scissors":
     print("Rock vs Scissors. Rock wins!")
    if cpuc == "Paper" and uc == "Paper":
       print("Paper vs Paper. It's a tie!")
    if cpuc == "Paper" and uc == "Rock":
       print("Paper vs Rock. Paper wins!")
    if cpuc == "Paper" and uc == "Scissors":
       print("Paper vs Scissors. Scissors wins!")
    if cpuc == "Scissors" and uc == "Scissors":
       print("Scissors vs Scissors. It's a tie!")
    if cpuc == "Scissors" and uc == "Paper":
       print("Scissors vs Paper. It's a tie!")
    if cpuc == "Scissors" and uc == "Rock":
     print("Scissors vs Rock. It's a tie!")
     continue