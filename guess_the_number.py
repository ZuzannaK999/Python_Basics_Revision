import random
mini = raw_input("Choose the min number: ")
top = raw_input("Choose the max number: ")
if mini.isdigit():
    mini = int(mini)
else:
    print("You haven't entered a number")
    quit()
if top.isdigit():
    top = int(top)
else:
    print("You haven't entered a number")
    quit()
num = random.randint(mini, top)
guess_limit = 5
guess_num = 0
while guess_num < guess_limit:
    ans = raw_input("Please guess a number: ")
    if ans.isdigit():
        ans = int(ans)
    else:
        print("You haven't entered a number")
        continue
    if ans != num:
        guess_num += 1
        print("Incorrect. This is your " + str(guess_num) + " try")
        if ans < num:
            print("Choose sth bigger")
        elif ans > num:
            print("Choose sth smaller")
    elif ans == num:
        print ("Correct")
        break
if guess_num == guess_limit:
    print("You've lost")

