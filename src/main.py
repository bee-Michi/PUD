#We import the required modules
import time, random
#Non standard module
import names
from password_generator import PasswordGenerator
#Title, for flex and beauty
print("------------------------------------------------------------PUB----------------------------------------------------------------------------")
#Version, with a reminder to update
version = "0.2.0 This version is beta. Make sure you are on the latest version by using the github command ang going to the latest relese"
#Creator, which tells the creator of this project
creator = "bee-Michi"
#Contributors of this project
contributors = {"Currently nobody :( You can be the first one :)"}
#Tells you copyright and license
copyright = "Copyright© bee-Michi 2022. This project is distributed under the MIT license. Learn more info at the license file :)"
#Github command, that tells you the github page
github = "https://github.com/bee-Michi/PUD"

#This part is where the main functions are held. These contain all commands and utilities. If you want modify code, here the code is contained
#Function to print the help command
def printhelp():
    #This is the help command. It hosts all the available utilities and commands
    helptoprint = ["Time", "Random number generator", "Countdown", "Password generator"]
    #Sort the list alphabetically
    helptoprint.sort()
    # For loop to print all the help commands up here
    for hel in helptoprint:
        print(hel)
#Function to print all the available commands
def printcommands():
    # This is the command command, here all the available commands are available.
    commands = ["Help", "Version", "Creator", "Contributors", "Copyright", "Github",]
    #Sort the list alphabetically
    commands.sort()
    # For loop to print all the commands up here
    for everycommand in commands:
        print(everycommand)
#Function to print the contributors
def printcontributor():
    # For loop to print all contributors    
    for contribute in contributors:
        print(contribute)
#Function to print the current time
def getcurrenttime():
    #We get the current time and store it on a variable 
    t = time.localtime()
    #Variable to print, using time and formatting it in a way
    current_time = time.strftime("%H:%M:%S", t)
    #Print th variable
    print(current_time)
#Function for the random number generator
def randomnumbergeneretor():
    #Function to generate a random number
    def generate():
        #Get a random number
        number = random.randint(0, 100000000)
        #Print it
        print(number)
    #Call the function
    generate()
    #Ask if the user wants to repeat 
    repeat = input("Want to repeat? (input y or n): ")
    #Check if the user says y
    if repeat == "y":
        #Call the function again
        generate()
        
#Function to print a countdown
def countdown():
    #Makecountdown to create the countdown. This function creates, calculates and simulates a timer.
    def makecountdown(timeselect):
        #Main while loop that does all the calculation
        while timeselect:
            #Format minutes and seconds using our input and calculating kepping in mind minuts
            mins, secs = divmod(timeselect, 60)
            #Get mins and secs and format it
            timer = '{:02d}:{:02d}'.format(mins,secs)
            #print the timer, and using the end function
            print(timer, end="\r")
            #Make it sleep so that it's a real timer and functions like the law of time
            time.sleep(1)
            #Then detract a second to make the actual computer time go down
            timeselect -= 1
        #And repeat until the time ends
        #Print "Timer compleated!" after the timer is finished.
        print("Timer completed!")
    #Welcome and ask for the time in seconds
    timeselect = input("Welcome to countdown! Enter the time in seconds: ")
    #And then we call the function inserting the input as data inside the function. 
    makecountdown(int(timeselect))
#Function to create an mit license
def licensecreator():
    def licensemaker(license):
        #Ask for the current year
        year = input("Welcome to MIT license compiler! Please insert the year: ")
        #Ask for the copyright owner
        copyOwner = input("OK! Input the copyright owner: ")
        #Transform into str the year
        str(year)
        license = {f"""
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
        file = open("license.txt", "wt")#Open in override and text mode
        #Write the license in the file
        file.writelines(license)
        #Close the file
        file.close()
    licensemaker()
def passwordgeneretor():
    #Function for mode 1
    def mode1():
        #Generate the password
        pwo = PasswordGenerator()
        password = pwo.generate()
        #Print the passoword
        print(f"Here's your password: {password}")
    #Function for mode 2
    def mode2():
        #Set password generator to pwo
        pwo = PasswordGenerator()
        #Ask for length
        length = int(input("Specify length: "))
        #Set min and max length so length is equal to the length that the user asked
        pwo.minlen = length
        pwo.maxlen = length
        #Generate the password
        password = pwo.generate()
        #Print it
        print(f"Here's your password: {password} ")
    #Function to print all modes
    def helpmodes():
        modes = ["Mode 1: Random password", "Mode 2: Random password with specified length"]
        #For loops
        for mode in modes:
            print(mode)
    while True:
        #Check what mode does the user want to use
        modeselect = input("Hi! Type the number to access the corresponding mode. Don't know what are modes? Type help: ")
        #If the input is equal to 1 activate mode 1
        if modeselect == "1":
            mode1()
        #Else if the input is equal to 2 activate mode 2
        elif modeselect == "2":
            mode2()
        #Else if the input is equal to help use the function to print all modes
        elif modeselect == "help":
            helpmodes()
        elif modeselect == "exit":
            break
        #Final else to check if the input is not equal to 1 or 2, and print an error
        else:
            print("Not an accepted mode!")
#Main while true loop
while True:
    #The central input, to check what tool does the user want to do
    select = input("Welcome! Use help to get all tools and commands for some useful commands: ")
    #If and elif commands, to check what to use
    #Help
    if select == "help":
        printhelp()
    #Commands
    elif select == "commands":
        printcommands()
    #Version
    elif select == "version":
        print(version)
    #Creator
    elif select == "creator":
        print(creator)
    #Contributors
    elif select == "contributors":
        printcontributor()
    #Copyright
    elif select == "copyright":
        print(copyright)
    #Github
    elif select == "github":
        print(github)
    #Two versions to exit the program, quit and exit
    elif select == "quit":
        break
    elif select == "exit":
        break
    #Access time
    elif select == "time":
        getcurrenttime()
    #Access random number generator
    elif select == "random number generator":
        randomnumbergeneretor()
    #Access the countdown.
    elif select == "countdown":
        countdown()
    #Access the license compiler
    elif select == "license creator":
        licensecreator()
    #Access the password generator
    elif select == "password generator":
        passwordgeneretor()
