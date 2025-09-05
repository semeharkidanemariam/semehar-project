secret_word = "hello"
guess = ""
guess_limit = 4
guess_count = 0
out_of_guess = False
while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("enter you guess")
        guess_count = + 1
    else:
        out_of_guess = False
if out_of_guess:
    print("you lose!")
else:
    print("you win!")            

