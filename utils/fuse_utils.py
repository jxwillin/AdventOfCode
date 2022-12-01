# Fuses util files into one super util script so it's easier to setup where I have web access but not git clone
import os
excludes = ["__init__.py", os.path.basename(__file__)]
dirs = os.listdir(".")
def check_line(line):
    if line.startswith("import ."):
        return False
    return True
with open("util.py","w") as output:
    for file in dirs:
        if file.endswith(".py"):
            if file not in excludes:
                lines = open(file,'r').readlines()
                for line in lines:
                    if check_line(line):
                        output.write(line)

