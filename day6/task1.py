import numpy

file = "input.txt"

def read_file(file):
    with open(file) as f:
        lines = f.readlines()
    return [line.strip("\n") for line in lines]

lines = read_file(file)
print(lines)

directions = ["^", ">", "v", "<"]

def find_start_pos(lines):
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != "." and char != "#":
                for k, dir in enumerate(directions):
                    if char == dir:
                        return [i, j, k]
    print("didn't find guard")

def move(guard):
    if guard[2] == 0: #move up
        guard[0] -= 1
    if guard[2] == 1: #move right
        guard[1] += 1
    if guard[2] == 2: #move down
        guard[0] += 1
    if guard[2] == 3: #move left
        guard[1] -= 1


guard = find_start_pos(lines) # Guard = [y_pos, x_pos, direction]
old_pos = [0,0,0] 

visited_positions = numpy.zeros((len(lines), len(lines[0])))

while (guard[0]<len(lines) and guard[1]<len(lines[0]) and guard[0]>=0 and guard[1]>=0):
    print(lines[guard[0]][guard[1]])
    if lines[guard[0]][guard[1]] == "#":
        print("\nhit ", old_pos, guard)
        guard[0] = old_pos[0]
        guard[1] = old_pos[1]
        guard[2] = old_pos[2]
        guard[2] += 1
        if guard[2] == 4:
            guard[2] = 0
            print("wrap")
    visited_positions[guard[0],guard[1]] = 1
    print(visited_positions)
    print("\n")
    old_pos[0] = guard[0]
    old_pos[1] = guard[1]
    old_pos[2] = guard[2]
    move(guard)

print(sum(sum(visited_positions)))

    





