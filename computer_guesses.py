#computer guesses a number
import random
mini = 0;
top = 8;
guess_limit = 5
guess_num = 0
while True:
    the_num = raw_input("Enter a number you want the computer to guess: ")
    if the_num.isdigit():
        the_num = int(the_num)
        break
    else:
        print("You haven't enter a number. Try again")
        continue
while guess_num < guess_limit:
    ans = random.randint(mini, top)
    if ans != the_num:
        guess_num += 1
        feedback = raw_input("Is " + str(ans) + " too (h)high or too (l)low? ")
        if feedback == "h":
            top = ans - 1
            ans = random.randint(mini, top)
        elif feedback == "l":
            mini = ans + 1
            ans = random.randint(mini, top)
    elif ans == the_num:
        print("Computer's answer: " + str(ans))
        print("Computer guessed the number " + str(the_num) + " correctly")
        break
if guess_num == guess_limit:
    print("Computer lost ")
