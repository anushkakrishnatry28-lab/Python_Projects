#Random Number Generator Game
import random
random_number=random.randint(1,100)
max_attempts=5
attempts=0
while attempts<max_attempts:
    user=int(input("Enter the random number:- "))
    attempts+=1
    if user==random_number:
        print("Well done...you guessed the right number")
    elif user < random_number:
        print("Too low...Try again")
    else:
        print("Too high...Try again")
if  attempts == max_attempts and user!=random_number:
    print("Game over...") 
    print("The random number is:- ",random_number)            
    
