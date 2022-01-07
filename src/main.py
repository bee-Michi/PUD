print("""
------------------------------------------------------------PUB----------------------------------------------------------------------------
""")
version = "0.1.2 You can check versions by going on the github page or using the github command"
creator = "bee-Michi"
contributors = {
    "Currently nobady :( You can be the first one :)"
}
copyrigth = "Copytirgth© bee-Michi 2022"
liscence = "This project is distributed under the MIT liscence. Learn more info at the liscence file :)"
github = "https://github.com/bee-Michi/PUD"

def help():
    helpp = ["Help"]
    for hel in helpp:
        print(hel)
def commands():
    commad = ["Version", "Creator", "Contributors", "copytirgth", "liscence", "github"]
    for command in commad:
        print(command)
def contributor():
    for contribute in contributors:
        print(contribute)
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
