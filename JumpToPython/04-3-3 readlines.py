# readline.py
f = open("C:\PythonStudy\JumpToPython\writedata.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line, end='')
f.close()