import os
running = True

os.chdir("sys")

# const
root = os.getcwd()

# commands
def pwd():
    dir = os.getcwd().replace(root, "")
    if dir == "":
        print("/")
    else:
        print(dir)

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
    inp = input(os.getcwd() + "$ ")
    if inp.startswith("cd"):
        cd(inp)
    elif inp == "pwd":
        pwd()
    elif inp == "exit":
        running = False
    else:
        print("command does not exist")
