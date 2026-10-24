from sys import argv
from os.path import exists

if len(argv)!=2:
    print("Usage: py diary.py filename")
    exit()
    
script, file_name = argv



print("Does the file exist?", exists(file_name))

date=input("Whats today date? ")
learn=input("What have you learn today? ")
mood=input("Hows going on today? ")

with open(file_name,'a') as f:
    f.write(f"Date: {date}\nLearned: {learn}\nMood: {mood}\n\n")

print("Here's your diary:")
with open(file_name) as f:
    print(f.read())


