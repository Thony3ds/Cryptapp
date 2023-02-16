import os, run_app

def whileSession():
    running = True
    while running:
        command = input("CryptApp/terminal: ")
        if command == "help":
            print("please see: 'assets/other/help_terminal.txt' for all commands")
        elif command == "run":
            running = False
            print("Start CryptApp....")
        elif command == "autorun":
            autorun = input("please chose your autorun mod True/False: ")
            if autorun != "True" and autorun != "False":
                print(f"error on the answer: {autorun}")
            else:
                file = open("assets/terminal_assets/autostart.txt", "w")
                file.write(autorun)
                file.close()
                print(f"finish to change the autorun's mod with {autorun} mod")
                if autorun == "True":
                    print("for start use 'run' command :)")
        else:
            print(f"error we can read the command {command} please write 'help' to receved some help")
def startSession():
    print("initalisation....")
    print("Welcome !!")
    if os.path.exists(path="assets/terminal_assets/autostart.txt") == True:
        file = open("assets/terminal_assets/autostart.txt", "r")
        infile = file.readlines()
        file.close()
        if infile == ['True']:
            return True
        elif infile == ['False']:
            print("starting terminal....")
            whileSession()
        else:
            print("Error on file system")
            print(f"the system return: {infile}")
    else:
        file = open("assets/terminal_assets/autostart.txt", "w+")
        file.write("False")
        file.close()
        startSession()