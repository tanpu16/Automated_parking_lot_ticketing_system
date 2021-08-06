#driver.py
import sys
import fileinput
from pl_auto_ticketing import pl_auto_ticketing_process

if len(sys.argv) == 1:
    while True:
        inter_input = input()
        pl_auto_ticketing_process(inter_input)
elif len(sys.argv) > 1:
    for eachline in fileinput.input():
        pl_auto_ticketing_process(eachline)
else:
    print("Incorrect command line arguments. Expected 1 or 0")