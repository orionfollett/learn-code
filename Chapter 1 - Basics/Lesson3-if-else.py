#LESSON 3 - if else statements

print("--------------------Section 3.1 - Introduction to If Else Statements----------------------")
#Up until now, you have been working with a glorified calculator that can do some calculations and print them to the screen
#But oftentimes, you need your computer to make decisions, this is where if else statements come in

#if else statements are structured like this:
isValueTrue = True

print("BEGINNING OF IF STATEMENT")

if isValueTrue:
    print("1. this line of code will run")
    print("2. then this line of code")
    print("3. then this one")
else:
    print("this line of code will not run")
    print("and neither will this one")

print("END IF STATEMENT")

#if you had to guess, what do you think will print to the screen when you run this code?
#Run it to find out. 

#Try changing the variable "isValueTrue" to equal False

#The code before the if statement runs just like normal, the block of code that is one indent
#in from the if statement only runs if the condition after the if statement is True, 
#if the condition is False, then the code block that is indented after the else statement runs instead.

#when the if statement wraps up, the code that is after the if statement continues running 



#A more real world example could look like this:

enemyDistanceFromPlayer = 32
attackRange = 10

if enemyDistanceFromPlayer < attackRange: # if the enemy is within range, it will attack, otherwise it will move towards the player
    print("enemy attack code would go here")
else:
    print("enemy  would move towards the player")


#the if statement has two parts, the word "if", and then the "condition" which comes after the word 
#the "body" of the if statement is the code that executes if the condition is True


#TASK:

#write a mock if else statement for a video game, where if the player hits the space bar, they jump
playerInput = "SPACEBAR" #use this variable in your mock if else statement, you can just print something like "player jumps", to pretend make the player jump






print("--------------------Section 3.2 - Tangent into Input----------------------")

#Oftentimes the computer needs to make a decision based on user input.

#almost every computer program can be boiled down the a human inputs something, the computer does something with the input, then it ouputs a result
# 'IO' stands for input/output

#in a game, you press buttons, the computer does stuff with that input, and display pictures to your screen very quickly to simulate motion
#in a web browser, you enter text or whatever else, the computer talks to the internet, and then displays things

#so far you know one way of doing output, the print statement, and no ways of doing input. 

#the 'input' function, takes one argument, a message
#it will block the execution of your program until something is entered, and then it will return 
#whatever the user enters as a string

#run this code,  enter your name into the prompt, and hit 'enter':
userInputVariable = input("Please enter your name: ") #the input function displays the message that you supply, and waits for your input
print("Your name is: " + userInputVariable)

#TASK:
#now rewrite the last code example, to jump when the user enters the word "SPACEBAR"



print("--------------------Section 3.3 - More If Else Statements----------------------")

#If statements do not have to have else statements attached,

#for example you can do:

playerInput = input("Please select one option (1: compliment, 2: insult, 3: back-handed complement): ")

if playerInput == "1":
    print("You are looking very nice today.")

if playerInput == "2":
    print("Damn you uglay")

if playerInput == "3":
    print("You FINALLY look somewhat nice...for once")


#Task: Think of a reason you could combine input, if-else statements, and output (print statements) to make the computer make a decision based on the user input
#Implement you idea below:





print("--------------------Section 3.4 - elif Statements----------------------")

#sometimes you want to go through options, but only one of them can be true
#for example the complement or insult example above:

#this is where you can use the "elif" statement, which is short hand for "else if"

#the program will try the first if statement, then the next, then the next, until
#one is true, then it will only execute that block of code

#I could've done:
if playerInput == "1":
    print("You are looking very nice today.")

elif playerInput == "2":
    print("Damn you uglay")

elif playerInput == "3":
    print("You FINALLY look somewhat nice...for once")

else:
    print("Invalid option")


#If your example had more than two options from the last section, use elif options if appropriate
#If it doesnt, create a new example that does use elif statements


#Vocabulary:

# elif - 
# input (what is the input function?) - 
# IO - 