"""First day lecture cpu file."""
import sys
import random

# create memory array
memory = [
    1, # PRINT DO A THING
    3, # SAVE TO REGISTER / R[N] / VALUE
    4,
    37,
    2  # HALT
]

registers = [0] * 8

pc = 0 # Keep track of memory location
running = True
while running:
    ir = memory[pc]

    if ir == 1:
        print("Do a thing.")
        pc += 1

    elif ir == 2:
        running = False
        pc += 1
    
    elif ir == 3:
        registers[memory[pc+1]] = memory[pc+2]
        pc += 3

