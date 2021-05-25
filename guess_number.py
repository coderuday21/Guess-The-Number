num=18
no_of_guess_left=5
while no_of_guess_left!=0:
    print("Guess Left:",no_of_guess_left)
    guess=int(input("Guess the no"))
    if guess==num:
        print("You have guessed the number")
        if input('Do you want to continue: Yes or No') in ('y','yes'):
            no_of_guess_left=5
        else:
            break
    elif guess<num:
        print("The no guessed is less than number")
        no_of_guess_left-=1
    else:
        print("The no guessed is more than number")
        no_of_guess_left-=1
else:
    print("you haven't guessed the right number")
