# sys.py
import sys

args = sys.argv[1:]

for i in args:
    print(i.upper(), end=' ')

print("")

input('입력 대기')