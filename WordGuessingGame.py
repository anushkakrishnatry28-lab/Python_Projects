#Word Guessing Game
import random
word=["apple","guava","litchi","pineapple","mango","pomegranate"]
words=random.choice(word)
max_attempts=5
attempts=0
while attempts < max_attempts:
    user=input("Enter the word:- ")
    attempts+=1
    if user==words:
        print("Congratulations....")
        break
    else:
        print("Try again....")
if(attempts==max_attempts and user!=words):
    print("Game is over")
    print("The random word generated is:- ",words)            