import tkinter as tk
from tkinter import font
from assets import CryptApp, TerminalCommand, JsonReader
from time import sleep

appli = tk.Tk()
Ubuntu = font.Font(family='Ubuntu', size=18, weight='bold')

class data():
    thextention = ""
    color_button = "gray"
    color_written = "white"
    color_bg = "black"
    json_readfile = JsonReader.language_load()

def entryFile4():
    global input_value3
    input_value3 = inputer3.get()
    inputer3.destroy()
    label4.destroy()
    button4.destroy()
    global label5
    label5 = tk.Label(appli, text=JsonReader.readJson(toread="Cryptage in progress please wait", langue=data.json_readfile), font=Ubuntu, bg="black", fg=data.color_written)
    label5.pack(pady=20)
    exit = input_value2 + data.thextention
    cryptapp = CryptApp.crypt_decrypt(entry_file=input_value1, exit_file=exit, key=input_value3)
    print(f"CryptApp return: {cryptapp}")
    label6 = tk.Label(appli, text=JsonReader.readJson(toread="The process have finish", langue=data.json_readfile), font=Ubuntu, bg="black", fg=data.color_written)
    label6.pack()
    label7 = tk.Label(appli, text=JsonReader.readJson(toread="The app will be autostop", langue=data.json_readfile), font=Ubuntu, bg="black", fg=data.color_written)
    label7.pack()
    sleep(3)
    appli.destroy()

def entryFile3():
    global input_value2
    input_value2 = inputer2.get()
    inputer2.destroy()
    label3.destroy()
    button3.destroy()
    global label4
    label4 = tk.Label(appli, text=JsonReader.readJson(toread="Entry your crypt key", langue=data.json_readfile), font=Ubuntu, bg="black", fg=data.color_written)
    label4.pack(pady=20)
    global inputer3
    inputer3 = tk.Entry(appli)
    inputer3.pack(pady=20)
    global button4
    button4 = tk.Button(appli, text=JsonReader.readJson(toread="Send and start", langue=data.json_readfile), command=entryFile4)
    button4.pack()

def entryFile2():
    global input_value1
    input_value1 = inputer.get()
    inputer.destroy()
    label2.destroy()
    button2.destroy()
    global label3
    label3 = tk.Label(appli, text=JsonReader.readJson(toread="Entry your exit file", langue=data.json_readfile), font=Ubuntu, bg="black", fg=data.color_written)
    label3.pack(pady=20)
    global inputer2
    inputer2 = tk.Entry(appli)
    inputer2.pack(pady=20)
    global button3
    button3 = tk.Button(appli, text=JsonReader.readJson(toread="Send", langue=data.json_readfile), command=entryFile3)
    button3.pack()

def entryFile1():
    label1.destroy()
    button.destroy()
    button1.destroy()
    global label2
    label2 = tk.Label(appli, text=JsonReader.readJson(toread="Entry your entry file", langue=data.json_readfile), font=Ubuntu, bg="black", fg=data.color_written)
    label2.pack(pady=20)
    global inputer
    inputer = tk.Entry(appli, textvariable="input1")
    inputer.pack(pady=20)
    global button2
    button2 = tk.Button(appli, text=JsonReader.readJson(toread="Send", langue=data.json_readfile), command=entryFile2)
    button2.pack()

def button_click1():
    data.thextention = ".crypt"
    label2 = tk.Label(appli, text=JsonReader.readJson(toread="Crypt", langue=data.json_readfile), font=Ubuntu, bg="black", fg=data.color_written)
    print(".crypt")
    label2.pack(pady=20)
    entryFile1()
def button_click2():
    data.thextention = ".decrypt"
    label3 = tk.Label(appli, text=JsonReader.readJson(toread="Decrypt", langue=data.json_readfile), font=Ubuntu, bg="black", fg=data.color_written)
    print(".decrypt")
    label3.pack(pady=20)
    entryFile1()

def app():
    appli.title("Crypt_App")
    appli.geometry("800x600")
    appli.minsize(width="500", height="350")
    appli.config(bg=data.color_bg)

    label = tk.Label(appli, text=JsonReader.readJson(toread="Welcome", langue=data.json_readfile), font=Ubuntu, bg='black', fg=data.color_written)
    label.pack(pady=20)
    global label1
    label1 = tk.Label(appli, text=JsonReader.readJson(toread="Chose your option", langue=data.json_readfile), font=Ubuntu, bg="black", fg=data.color_written)
    label1.pack(pady=20)

    global button
    button = tk.Button(appli, text=JsonReader.readJson(toread="Crypt", langue=data.json_readfile), command=button_click1)
    button.pack(pady=20)
    global button1
    button1 = tk.Button(appli, text=JsonReader.readJson(toread="Decrypt", langue=data.json_readfile), command=button_click2)
    button1.pack(pady=20)

    appli.mainloop()

if __name__ == '__main__':
    TerminalCommand.startSession()
    app()