
def play():
    points = 0
    a1 = raw_input("What is the smallest country in the world? ").lower()
    if a1 == "vatican City":
        points += 1
        print("Correct. You've got " + str(points) + " points")
    elif a1 == "vatican":
        points += 1
        print("Correct. You've got " + str(points) + " points")
    else:
        print("Incorrect. You've got " + str(points) + " points")
    a2 = raw_input("What is the capital of New Zealand? ").lower()
    if a2 == "wellington":
        points += 1
        print("Correct. You've got " + str(points) + " points")
    else:
        print("Incorrect. You've got " + str(points) + " points")
    a3 = raw_input("Which desert is the largest in the world? ").lower()
    if a3 == "the sahara desert":
        points += 1
        print("Correct. You've got " + str(points) + " points")
    elif a3 == "sahara":
        points += 1
        print("Correct. You've got " + str(points) + " points")
    else:
        print("Incorrect. You've got " + str(points) + " points")
    a4 = raw_input("What is the name of the worlds longest river? ").lower()
    if a4 == "the nile":
        points += 1
        print("Correct. You've got " + str(points) + " points")
    elif a4 == "nile":
        points += 1
        print("Correct. You've got " + str(points) + " points")
    else:
        print("Incorrect. You've got " + str(points) + " points")
    a5 = int(raw_input("In which year World War I begin? "))
    if a5 == 1914:
        points += 1
        print("Correct. You've got " + str(points) + " points")
    else:
        print("Incorrect. You've got " + str(points) + " points")

    print("Percentage of correct answers: " + str(points / 5 * 100) + "%.")


while True:
    ans = raw_input("Do you wanna play? ")
    if ans.lower() == "yes":
        play()
    else:
        break
