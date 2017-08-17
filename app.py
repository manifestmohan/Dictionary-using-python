import json
import difflib

from difflib import get_close_matches

data=json.load(open("data.json"))

def meaning(word):
    word=word.lower()
    suggest=get_close_matches(word,data.keys(),n=1,cutoff=0.8)[0]
    if word in data:
        return data[word]
    elif len(suggest)>0:
        choice=input("Did you mean %s ! Type 'Y' for YES and 'N' for NO : " %suggest)
        choice=choice.lower()
        if choice=="y":
            return data[suggest]
        elif choice == "n":
            return "Try Again"
        else:
            return "Wrong Input"
    else:
        return "Word does not exist"

text = input("Enter the word : ")

output=(meaning(text))

if type(output) == list :
    for i in output:
        print(i)
else:
    print(output)
