#LESSON 2 - Variables and Operators


print("--------------------Section 2.1 - Introduction to Variables----------------------")
#A variable is a symbol that can represent any piece of data in memory, it is very similar to a variable in algebra

#For example:
x = "Hello World" #This code is declaring a variable called 'x', and setting it equal to the string "Hello World"

#x now represents the data "Hello World"

#this lets you do this:
print(x) #And if you run this program (by clicking 'F5'), you will see that print does not print the letter 'x', it prints what the variable x represents: "Hello World"



#TASKS for Lesson 2.1

#1. Write some new code that prints the numbers 1, 2, and 3, all on new lines. Only use variables, name your variables x, y, and z









print("--------------------Section 2.2 - Naming Variables ----------------------")

#Variables can have any name you want, as long they don't have spaces in them
#In theory you could use silly names like:

hamburger = "Hello World"
print(hamburger)

#but as your programs get more complicated, it becomes hard to keep track of what each variable represents
#In practice you want to name variables something that relates to what it is, for example:

helloMessage = "Hello World"
print(helloMessage)

#another convention when naming variables is called 'camel case'. Camel case is where you leave the first word
#lower case, and then every other word you capitalize the first letter

#ex: helloYouAreMyBestFriend is a little easier to read than helloyouaremyfriend

#variable names should be short but descriptive, and they are a lot of the difference between an experienced and a beginnner programmer


#TASKS for Lesson 2.2

#1.  What would be a good name for a variable that represents the result of adding two numbers?
#2.  Predict what this code will print out: 

#helloOrion = "helloLucas"
#print(helloOrion)

#3. Uncomment the code from #2 and find out.




print("--------------------Section 2.3 - Variable Types ----------------------")

#So far you have only seen variables holding strings. Strings are a sequence of characters. Characters are things like 'a', '1', '?', '.', basically
#anything you can type on your keyboard. 

#a string is just one of many "types". 
#The Python name for string is "str"

#some common types in python are:
# - bool : can only be True or False
# - int : represents an integer, which is a positive or negative number but with no decimal points, ex: 1, 0, -1, 243
# - float : a number with a decimal point, ex: 1.0, 2.0, -0.023
# - str : a string, aka a sequence of characters: "hello", "apsiuhfpasihfg19384019384 )(^&*^#$"
# - list : a list of any data type, [1, 2, 3, 4]
# - NoneType : a type that represents nothing

#some more advanced types are:
# - dict
# - set
# - tuple

#Python automatically figures out what type your variable has
#you can print what type a variable has by using the "type" function
x = "orion"
type(x) #this will return the type, in this case, "str" because the variable x is a string

x = 1
type(x)#this will return "int" because x is now an integer

#you can see the type by putting the type function inside of a print function:
intType = 12
print(type(intType)) #will print "int"

strType = "12"
print(type(strType)) # will print "string"

floatType = 12.0
print(type(floatType)) # will print "float"


#Task for Lesson 2.2
#What happens if you uncomment these two lines of code?
#x = 10
#print(x + 2)



print("--------------------Section 2.4 - Operators ----------------------")
#Depending on the type you can do different things with variables:
#To do things to variables, you use operators. An operator is a symbol that lets you manipulate variables, this will
#make more sense in a moment with some examples

#In a comment next to each line, write what you think each line of code will print

print(1 + 2)
print(2.5 - 0.5)
print(3 * 4)
print(4 / 2)
print("hello " + "world")
print("1" + "2")
#print("hello"  - "world") #uncomment this line to see what happens


#Common Operators:
#   +    -> plus sign, adds two ints or floats, or "concatenates" two strings. String concatenation means to put the two strings side by side
#   -    -> minnus sign, substracts two numbers
#   *    -> multiply sign, multiplies two numbers
#   /    -> division sign, divides two numbers

#not all operators work on all types, you can add two strings, but you cannot subtract them

#Another operator that you have already seen is called the "assignment" operator. it is the equals sign: "="
#the assignment operator is different from an equals sign in math in a subtle way. In math, an equals sign is you 
#telling someone two things are equal. The assignment operator is you assigning a value to a variable, and nothing else.

#in math, x = 2, and 2 = 2, and 2 = x
#in programming x = 2, but 2 = x does not make sense, and 2 = 2 is an error, because 2 cannot be a variable name as its already the name of a number!

#you can combine the assignment operator with the other operators:

x = 2
y = 4
sum = x + y

#For example you could approximate the circumference of a circle
radius = 2
pi = 3.14
circumference = 2 * pi * radius
print(circumference)

#Task: Complete the following code fragment:
areaOfCircle = 0 # replace 0 with the formula for area of circle, using the variables we already defined
print(areaOfCircle)


print("--------------------Section 2.5 - Boolean values ----------------------")

# "Boolean" or "bool" is a type that can be true or false, they are also called logical types

#here is how the literal values, 'True' and 'False' can be assigned to a variable
x = True
notX = False

print(x)
print(notX)

#There are special operators for boolean values

#not -> converts the boolean to be the opposite of whatever it is ex: "not True" would evaluate to "False"
# and -> return True is both values are True, or False otherwise
# or -> return True if one or the other values is True, and only returns False if both are False
# == -> comparison operator, returns True if both values are equal, it is the equivalent as asking "is equal to"
# <  -> 'less than' sign, just like in math, returns true if the left value is less than the right value
# <= -> 'less than or equal to' sign, same but also returns if they are equal
# >  -> 'greater than'
# >= -> 'greater than or equal to'

#comment next to each one of these what these print statements what you think they will show when you uncomment them

#print(not False)
#print(True and False)
#print(False and True)
#print(False or False)
#print(False or True)
#print(12 == 12)
#print(not 12 == 12)
#print(not (True or False))
#print((not True) or (not False))



#Define the following vocabulary:

# variable - 
# camel case - 
# type - 
# str - 
# bool - 
# int - 
# float - 
# assignment - 
# concatenate - 
# operator - 
# and - 
# or -
# not - 