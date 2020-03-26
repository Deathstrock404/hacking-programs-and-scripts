 
#!/bin/python3

#Variables and Methods

quote = "belive you can and you are halfway there"

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #no of alphabets in the string


name = "kamaljot" #string
age = 20 # int int(20)
cgpa = 7.8 #float float(7.8)

print(int(age))


print('\n')


print(int(20.2))

print("My name is " + str(name) + " and I am " + str(age) + " years old.")

age += 1
print(age)

print('\n')
#Functions

print("Here is an example function:")

def who_am_i(): #this is a function def mean defing a function
	name = "kamaljot" #these are local variables
	age = 20
	print("My name is " + str(name) + " and I am " + str(age) + " years old.")

who_am_i()


#adding parameters in a functions

def add_one_hundred(num):
	print(num+100)
	
add_one_hundred(100)


#multiple parameter
def add(x,y):
	print(x + y)
	
add(7,5)


def multiply(x,y):
	return x * y #return the output but does not print anything
	
print(multiply(5,5))



def square_root(x):
	print(x ** .5) #this mean power of 1/2
	
square_root(81)

def nl():
	print('\n')
	
nl()



#Boolean Expressions

print("Boolean expressions:")


bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

nl()
#Relational and Boolean operators

greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False

nl()

#Conditional Statement

def coke(money):
	if money >= 35:
		return "You've got yourself a coke!\n"
	else:
		return "NO coke for you sucker!\n"
		
print(coke(50))
print(coke(20))

def alcohol(age,money):
	if (age >= 21) and (money >= 400):
		return "We're getting a drink!\n"
	elif (age >= 21 ) and (money < 400):
		return "Come back with more money.\n"
	elif (age < 21) and (money >= 400):
		return "Nice try kid!\n"
	else:
		"You are too poor and too youngn\n"


print(alcohol(21,500))
print(alcohol(21,300))
print(alcohol(20,500))
print(alcohol(20,300))
