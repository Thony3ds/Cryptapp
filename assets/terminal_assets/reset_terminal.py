def start():
    theinput = input("Do you want to reset terminal autorun Y/n: ")
    if theinput != "Y" and theinput != "n":
        print("error")
        start()
    else:
        if theinput == "Y":
            print("reseting....")
            file = open("autostart.txt", "w")
            file.write("False")
            file.close()
            print("reseting succeful !!")
        elif theinput == "n":
            print("canceling reset")

if __name__ == "__main__":
    start()