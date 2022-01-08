#We import the required modules
import time, random
#Title
print("""
------------------------------------------------------------PUB----------------------------------------------------------------------------
""")
#Version, whhith a reminder to update
version = "0.1.3 This version is beta. Make shure you are on the lates version by using the github command ang going to the lates relese"
#Creator, whitch tells the cretor of this project
creator = "bee-Michi"
#Contributors of this project
contributors = {
    "Currently nobady :( You can be the first one :)"
}
#Tells you copyrigth and liscence
copyrigth = "Copytirgth© bee-Michi 2022. This project is distributed under the MIT liscence. Learn more info at the liscence file :)"
#Github command, that tells you the github page
github = "https://github.com/bee-Michi/PUD"

#This part is where the main functions are held. These contain all commands and utilities. If you want modify code, here the code is contained
#Function to print the help command
def help():
    #This is the help command. It hosts all the available utilities and commands
    helpp = ["Help", "Time", "Random number generator"]
    # For loop to print all the help commands up here
    for hel in helpp:
        print(hel)
#Function to print commands
def commands():
    # This is the command command, here all the avialable commands are available.
    commad = ["Version", "Creator", "Contributors", "copytirgth", "liscence", "github", "help"]
    # For loop to print all the commands up here
    for command in commad:
        print(command)
#Function to print the contributors
def contributor():
    # For loop to print all contributors    
    for contribute in contributors:
        print(contribute)
#Function to print the current time
def clock():
    #We get the current time and store it on a variable 
    t = time.localtime()
    #Variable to print, using time and formatting it in a way
    current_time = time.strftime("%H:%M:%S", t)
    #Print th variable
    print(current_time)
#Function for the random number generator
def rng():
    #Input to check if it wnats to the length of the number
    cnl = input("Welcome! Want to select how long the number will be? (input y or n): ")
    #if the number should be a determined lengthe use this function 
    def rngcnl():
        #Input to get the length
        lenchoice = int(input("Select the length of the number(max 1000000): "))
        #Number generation using randint and storing it on a variable
        randfinal = random.randint(lenchoice, 1000000)
        #Print the fianal generation
        print(randfinal)
    #else use this function 
    def rngncnl():
        randfinal = random.random()
        print(randfinal)
    if cnl == "y":
        rngcnl()
    elif cnl == "n":
        rngncnl()
    else:
        print("not supported, try agian!")
while True:
    PUBseleect = input("Welcome! Use help to get all utilites and commands for some useful commands: ")

    if PUBseleect == "help":
        help()
    elif PUBseleect == "commands":
        commands()
    elif PUBseleect == "version":
        print(version)
    elif PUBseleect == "creator":
        print(creator)
    elif PUBseleect == "contributors":
        contributor()
    elif PUBseleect == "copyrigth":
        print(copyrigth)
    elif PUBseleect == "liscence":
        print(liscence)
    elif PUBseleect == "github":
        print(github)
    elif PUBseleect == "quit":
        break
    elif PUBseleect == "exit":
        break
    elif PUBseleect == "time":
        clock()
    elif PUBseleect == "random number generator":
        rng()
