import os
running = True

# const
root = os.getcwd()

# commands
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
    inp = input()
    if inp.startswith("cd"):
        cd(inp)
    elif inp == "exit":
        running = False
    else:
        print("command does not exist")
