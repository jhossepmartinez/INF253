import re

def getConfig(filename):
    with open(f"{filename}") as file:
        cE, cS, cT = file.readline().split()
        print("Config:",cE, cS, cT)
        return cE, cS, cT

def getLine(filename):
    with open(f"{filename}") as file:
        line = file.readline()
        return line

getConfig("config.txt")
linetest = getLine("codigo.txt")

pattern = re.compile("^bool")

print(pattern.search(linetest))
