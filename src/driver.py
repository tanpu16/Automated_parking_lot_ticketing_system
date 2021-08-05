#driver.py
import sys
import fileinput
if len(sys.argv) == 1:
    while True:
        inter_input = input()
        parking_lot_ticketing_process(inter_input)
elif len(sys.argv) == 0:
    for eachline in fileinput.input():
        parking_lot_ticketing_process(eachline)
else:
    print("Incorrect command line arguments. Expected 1 or 0")