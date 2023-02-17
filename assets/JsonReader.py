import json
def language_load():
    file = open("assets/languages/langue.txt", "r")
    infile = file.readlines()
    file.close()
    if "english" in infile:
        langue = "english"
    elif "frensh" in infile:
        langue = "frensh"
    else:
        langue = "error"
        print("error")
    return langue

def readJson(toread, langue):
    if langue == "english":
        filetoread = "assets/languages/english.json"
    elif langue == "frensh":
        filetoread = "assets/languages/frensh.json"
    else:
        filetoread = "assets/languages/english.json"
    with open(filetoread) as f:
        injson = json.load(f)

    toreturn = injson[toread]
    return toreturn