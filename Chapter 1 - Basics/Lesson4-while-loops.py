#LESSON 4 While Loops


print("---------------------Lesson 4.1 - Print Hello 1000 times--------------------------------")

#What if I asked you to print Hello 1000 times? Or if I asked you to print every even number from 0 to 1000?

#you could do this:
print("0")
print("2")
#print("4")...


#You wouldn't want to type all of that out, humans are slow and smart, computer are dumb, but incredibly fast. So let's let the
#computer do the work

#To do something repitively, Python gives you a tool called loops, there are two types of loops, while loops, and for loops.
#this lesson will show you while loops:

#A while loop is like an if statement, except instead of only executing the code in the body one time, 
#it executes it as fast as it can repeatedly until the condition is False.

#for example:
print("begin while loop example")
counter = 0
while counter < 10:
    print(counter)
    counter = counter + 1

#What do you think this code will do?

#The word "while" makes this a while loop, the condition is "counter < 10", since counter is 0, this condition starts off true
#the body of the loop is the indented block below the while statement, 
#in this case a print statement, and then a line that adds 1 to the counter
#as the loop repeats, the counter keeps growing, from 0 to 1, to 2 and so on... when it hits 10, the loop ends, because 10 is not less than 10
#if you run this code, it should print the numbers, 0 through 9.

#You can see how you could easily modify this to print number 0 to 10,000 or even higher. With a lot less typing
#Try it out! if the program takes too long, you can always kill the process in the terminal with the keyboard shortcut "CTRL+C" in the terminal 


#TASK
#1. Make a loop that prints the numbers 5 through 15
#2. Make a loop that prints the numbers from 100 to 1, counting down
#3. Make a loop that finds the sum of the numbers 1 through 100




print("---------------------Lesson 4.2 - Infinite Loops--------------------------------")
#One thing that can start happening as you write loops is you can accidentally create an infinite loop
#When you create an infinite loop, your computer burns up and creates a singularity that has 5% of swallowing the Earth

#Just kidding, but infinite loops will stop your program from ever continuing past the loop, and can make your computer do bad things
#like run out of memory in certain circumstances

#just always make sure that the condition in your while loop is being updated inside the loop.

#Task: write an explanation for why each of these examples is an infinite loop

#EX 1:

#while True:
    #..do some code


#EX 2:

#x = 2
#while x == 2:
    #print(x)

#EX 3:
#x = 2
#while x <= 2:
    #print(x)
#x = 100



print("---------------------Lesson 4.3 User Input Loop --------------------------------")

#loops are often at the core of any video game, called the main gameplay loop

#many text based games have some loop like this:

print("Game Start: ")
isPlaying = True

while isPlaying:
    optionsMessage = "Enter your next move:\n 1. Attack\n2. Move\n3. Talk\n4. Summon\n5. Quit\nChoose a number and hit 'Enter':"
    playerInput = input(optionsMessage)
    if playerInput == "1":
        print("ATTACK")
    elif playerInput == "2":
        print("MOVE")
    elif playerInput == "3":
        print("TALK")
    elif playerInput == "4":
        print("SUMMON")
    elif playerInput == "5":
        print("QUITTING")
        isPlaying = False
    else:
        print("Not an option, try again.")

print("Game Over")

#Run the program and player around with the options, notice how I have a quit option, to prevent an infinite loop
#without the "isPlaying" condition being changed, the only way to quit this game would be to close it in the task manager or kill the process in the terminal


#TASK:
#Write your own game play loop with some different options:


print("---------------------Challenge-----------------------------")
#Challenge (ask for help if you need it): Fibonacci Sequence 

#The fibonacci sequence is a sequence of numbers that often appears in nature. More about it here: https://en.wikipedia.org/wiki/Fibonacci_number

#the fibonacci numbers go like this: 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
#The pattern is that each number is the sum of the last two numbers
#The next number in the sequence would be 13 + 21 which is 34
#The first fibonacci number is 0, and the second fibonacci number is 1

#I want you to print the first 99 fibonacci numbers: