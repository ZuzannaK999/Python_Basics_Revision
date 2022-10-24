import random
round_limit = 3
round_num = 0
ur_score = 0
comp_score = 0
options = ["r", "p", "s", "q"]
random_num = random.randint(0, 2)
#0=rock, 1=paper, 2=scissors
comp_ans = options[random_num]
while round_num < round_limit:
    ur_ans = raw_input("Choose (r)rock, (p)paper or (s)scissors or (q)quit ")
    if ur_ans not in options:
        print("Invalid input. Try again")
        continue
    print("The computer chose: " + comp_ans)
    if ur_ans == "r" and comp_ans == "p":
        round_num += 1
        print("Computer scores")
        comp_score += 1
    elif ur_ans == "p" and comp_ans == "r":
        round_num += 1
        print("You score")
        ur_score += 1
    elif ur_ans == "s" and comp_ans == "r":
        round_num += 1
        print("Computer scores")
        comp_score += 1
    elif ur_ans == "p" and comp_ans == "s":
        round_num += 1
        print("Computer scores")
        comp_score += 1
    elif ur_ans == "r" and comp_ans == "s":
        round_num += 1
        print("You score")
        ur_score += 1
    elif ur_ans == "s" and comp_ans == "r":
        round_num += 1
        print("You score")
        comp_score += 1
    elif ur_ans == "s" and comp_ans == "p":
        round_num += 1
        print("You score")
        comp_score += 1
    elif ur_ans == "q":
        print("Bye")
        quit()
    else:
        print ("A tie. Try again")
        continue
if round_num == round_limit:
    print("Game over.")
    if ur_score > comp_score:
        print("You won the game")
    elif comp_score > ur_score:
        print ("You lost the game")


