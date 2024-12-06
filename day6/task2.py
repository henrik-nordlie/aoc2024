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


def simulate(lines, visited_positions):
    guard = find_start_pos(lines) # Guard = [y_pos, x_pos, direction]
    old_pos = [0,0,0] 
    while (guard[0]<len(lines) and guard[1]<len(lines[0]) and guard[0]>=0 and guard[1]>=0):
        if lines[guard[0]][guard[1]] == "#":
            guard = [old_pos[0], old_pos[1], old_pos[2]]
            guard[2] += 1
            if guard[2] == 4:
                guard[2] = 0
        if (guard[0], guard[1], guard[2]) in visited_positions:
            return True
        visited_positions.add((guard[0], guard[1], guard[2]))
        old_pos = [guard[0], guard[1], guard[2]]
        move(guard)

    return False

visited_positions = set()
tested_blocks = set()
trapped = simulate(lines, visited_positions)
copy_visited_positions = visited_positions.copy()
ans = 0
for i in copy_visited_positions:
    if (i[0],i[1]) in tested_blocks:
        continue
    else:
        tested_blocks.add((i[0],i[1]))
    start_pos = find_start_pos(lines) # Guard = [y_pos, x_pos, direction]
    if not [start_pos[0],start_pos[1]] == [i[0],i[1]]:
        lines[i[0]] = lines[i[0]][:i[1]] + "#" + lines[i[0]][i[1]+1:]
        new_visited_positions = set()
        trapped = simulate(lines, new_visited_positions)
        if trapped:
            ans += 1
            print("trapped on", i[0],i[1])
        lines[i[0]] = lines[i[0]][:i[1]] + "." + lines[i[0]][i[1]+1:]

print(ans)


    





