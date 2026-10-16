import random 

random_number = random.randint(1,10)

is_right = False

previous_guesses =[]

def guesses(random_number, previous_guesses):

    guess = int(input("enter a number 1-10: "))
    while guess > 10 or guess < 1:
         print("invalid input")
         guess = int(input("enter a number 1-10: "))

    while guess in previous_guesses:
        print("you guessed ", guess,)
        print("guess another number.")
        print(previous_guesses)
        guess = int(input("enter a number 1-10: "))
    while guess > 10 or guess < 1:
                print("invalid input!")
                guess = int(input("enter a number 1-10: "))

    if guess == random_number:
         print("you guessed right!")
         print("the number was:", random_number)
         previous_guesses.append(guess)
         print("you guessed:", previous_guesses)
         return True 

    elif guess > random_number:
         print("wrong! the number is lower! ")
         print("already guessed:", previous_guesses)
         previous_guesses.append(guess)

         return False
    else:
         print("wrong! the number is higher! ")
         print("already guessed:", previous_guesses)
         previous_guesses.append(guess)

         return False 

    
    
while not is_right:
     is_right = guesses(random_number,previous_guesses )

         
    



