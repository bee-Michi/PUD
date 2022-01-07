print("""
------------------------------------------------------------PUB----------------------------------------------------------------------------
""")
version = "0.1.1"
creator = "bee-Michi"
contributors = {
    "Currently nobady :( You can be the first one :)"
}
copytirgth = "Copytirgth© bee-Michi 2022"
liscence = "This project is distributed under the MIT liscence. Learn more info at the liscence file :)"
github = ""

def help():
    helpp = ["Help: This command!"]
    for hel in helpp:
        print(hel)

while True:
    PUBseleect = input("Welcome! Use help to get all utilites and commands for some useful commands: ")

    if PUBseleect == "help":
        help()
