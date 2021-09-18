import os
running = True

os.chdir("sys")

# const
root = os.getcwd()

# commands
def pwd(silent = False):
    dir = os.getcwd().replace(root, "")
    if dir == "":
        if silent == True:
            print("/")
        return "/"
    else:
        if silent == True:
            print(dir)
        return dir

def cd(inp):
    try:
        out = inp.replace("cd ", "")
    except:
        out = inp.replace("cd", "")
    if out.startswith("/"):
        try:
            os.chdir(root + out)
        except:
            print("directory does not exist")
    else:
        try:
            
            os.chdir(out)
        except:
            print("directory does not exist")
        dir = os.getcwd()
        if not dir.startswith(root):
            os.chdir(root)
        

# main loop
while running:
    inp = input(pwd(True) + " $ ")
    if inp.startswith("cd"):
        cd(inp)
    elif inp == "pwd":
        pwd()
    elif inp == "exit":
        running = False
    else:
        print("command does not exist")
