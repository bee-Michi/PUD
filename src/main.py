#We import the required modules
import time, random
#Non standard module
import names
from password_generator import PasswordGenerator
#Title, for flex and beauty
print("""
------------------------------------------------------------PUB----------------------------------------------------------------------------
""")
#Version, whhith a reminder to update
version = "0.2.0 This version is beta. Make shure you are on the lates version by using the github command ang going to the latest relese"
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
    helpp = ["Time", "Random number generator", "Coundown"]
    #Sort the list alphabeticlly
    helpp.sort()
    # For loop to print all the help commands up here
    for hel in helpp:
        print(hel)
#Function to print commands
def commands():
    # This is the command command, here all the avialable commands are available.
    commad = ["Help", "Version", "Creator", "Contributors", "Copytirgth", "Github",]
    #Sort the list alphabeticlly
    commad.sort()
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
    def generate():
        def rngcnl():
            #Input to get the length
            lenchoice = int(input("Select the length of the number(max 1000000): "))
            #Number generation using randint and storing it on a variable
            randfinal = random.randint(lenchoice, 1000000)
            #Print the fianal generation
            print(randfinal)
        #else use this function 
        def rngncnl():
            #Get a random seed 
            randfinal = random.random()
            #Print it
            print(randfinal)
        #If statment whith the input to check what function to use.
        if cnl == "y":
            rngcnl()
        elif cnl == "n":
            rngncnl()
        else:
            print("not supported, try agian!")
    generate()
    repeat = input("Wanto to repet? (input y or n): ")
    if repeat == "y":
        generate()
#Function to print a countdown
def countdownI():
    #Countdown function to calculate the time
    def countdown(t):
        #Main while loop
        while t:
            #Calculate mins, secs
            mins, secs = divmod(t, 60)
            #Format the timer
            timer = '{:02d}:{:02d}'.format(mins,secs)
            #End the timer
            print(timer, end="\r")
            #Make it sleep so that it's a real timer
            time.sleep(1)
            #Then detract a second
            t -= 1
        #Print this when the timer ends
        print("Timer completed!")
    #Ask for the time in seconds
    t = input("Welcome to countdown! Enter the time in seconds: ")
    #And then we call the function we call the function
    countdown(int(t))
#Function to make an mit liscence
def liscencecompiler():
    #Ask for the year
    year = input("Welcome to MIT Liscence compiler! Please insert the year: ")
    #Ask for the copyrigth owner
    copyOwner = input("OK! Input the copyrigth owner: ")
    #Transform into str the year
    str(year)
    liscenc = {f"""
    The MIT License (MIT) Copyright © {year} <{copyOwner}>
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
    documentation files (the “Software”), to deal in the Software without restriction, including without limitation the
    rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
    persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
    Software.

    THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
    WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
    COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
    OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    """}
    #Open and write a file
    file = open("liscence.txt", "wt")#Open in ovveride mode
    file.writelines(liscenc)
    #Close the file
    file.close()
    #Print that the file has been created
    print("File liscence.txt created and liscence written")
def passgenertor():
    #Check what mode does the user want to use
    modeselect = input("Hi! Type the mode you want to use. Don't know what are modes, type help: ")
    #Function for mode 1
    def mode1():
        #Set the module we imported to the name pwo
        pwo = PasswordGenerator()
        #Generate the password
        passwrod = pwo.generate()
        #Print it!
        print(f"Herse your password: {passwrod}")
        #No black magic!
    #Function for mode 2
    def mode2():
        #Set the module we imported to the name pwo
        pwo = PasswordGenerator()
        #Ask for length
        length = int(input("Specify length: "))
        #Set min and max length so length is 1
        pwo.minlen = length
        pwo.maxlen = length
        #Generate the password
        password = pwo.generate()
        #Print it
        print(f"Herse your password: {password} ")
        #No black magic
    def helpmodes():
        modes = ["Mode 1: Random password", "Mode 2: Random password with specified length"]
        for mode in modes:
            print(mode)
    if modeselect == "1":
        mode1()
    elif modeselect == "2":
        mode2()
    elif modeselect == "help":
        helpmodes()
    else:
        print("Not an accapted mode!")
#Main while true loop
while True:
    #The central input
    PUBseleect = input("Welcome! Use help to get all utilites and commands for some useful commands: ")
    #If and elif commands, to check what to use
    #Help
    if PUBseleect == "help":
        help()
    #Commands
    elif PUBseleect == "commands":
        commands()
    #Version
    elif PUBseleect == "version":
        print(version)
    #Creator
    elif PUBseleect == "creator":
        print(creator)
    #Contributors
    elif PUBseleect == "contributors":
        contributor()
    #Copytirgth
    elif PUBseleect == "copyrigth":
        print(copyrigth)
    #Github
    elif PUBseleect == "github":
        print(github)
    #Two versions to exit the program, quit and exit
    elif PUBseleect == "quit":
        break
    elif PUBseleect == "exit":
        break
    #Access time
    elif PUBseleect == "time":
        clock()
    #Acces random number generator
    elif PUBseleect == "random number generator":
        rng()
    #Acces the countdown.
    elif PUBseleect == "countdown":
        countdownI()
    #Acces the liscence compiler
    elif PUBseleect == "liscence compiler":
        liscencecompiler()
    #Acces the password generator
    elif PUBseleect == "password generator":
        passgenertor()
