chances = 0
number = random.randomint(round(1,9))
introString = input("Enter a number between 1-9: ")
guess = (introString,'r')
while chances < 5:

    if guess > number:
        print("Your guess was too high: Guess a number lower than ", guess)
        break

    if guess < number:
        print("Your guess was too low: Guess a number higher than", number)
        break
    
    if guess == number:
        print("Congratulation YOU WON!!!")
        break

if not chances < 5:
    print("YOU LOSE!!! The number is", number)