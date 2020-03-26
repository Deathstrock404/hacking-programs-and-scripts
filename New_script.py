#!/bin/python3

import sys # shows the system functions and parameters
from datetime import datetime as dt # imports as an alias
print (sys.version)
print(dt.now())

my_name = "Kamaljot"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence"
print(sentence[:4]) #this is to print the elements in the string before the 4th element

print(sentence.split()) #this splits the sentence into multiple sub strings with each elament of a string being new string 

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split) # this is used to join the various strings togather and create a new string with a space b/w them due to the use of ' '

print(sentence_join)

quote = "He said, \"give me all your money\"" # to use " inside a string without any error
print(quote)

too_much_space = "                           hello             "
print(too_much_space.strip()) #use .strip to remove all the space in the string when nothing is specified in the bracket


print("a" in "Apple") # to check wheter an element/letter is present in a string or not this is VERY CASE SENSITIVE

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #do the same thing as check  wheter an element/letter/charachter is present in a string or not but this is NOT CASE SENSITIVE

#FORMAT

movie = "End Game"
print("My favorite movie is {}.".format(movie)) #inplace of concatination we can also use this


#DICTIONARIES - key/value pairs {}

drinks = {"Coke": 20,"Dew": 15, "limca":10} #cold drinks are keys and the price is the value
 
print(drinks)
 
employees = {"Finance":["rahul","mohit","kunal"],"IT":["ankush","dilpreet"],"HR":["manan","aryan"]}
print(employees)

employees['Legal'] = ["nikita"] #add a key:value pair
print(employees)

employees.update({"Sales":["arijit","hardik"]}) #add new key:value pair using update
print(employees)

drinks['Coke'] = 25
print(drinks)

print(drinks.get("Coke"))
