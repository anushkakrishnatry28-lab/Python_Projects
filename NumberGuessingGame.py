#Number Guessing Game
number=int(input("Enter the number to be guessed:- "))
user=int(input("Enter the number:- "))

while number!=user:
    print("Try again!!!")
    user=int(input("Enter the number:- "))
    
print("You guessed the correct number.....Congratulations.....")
    