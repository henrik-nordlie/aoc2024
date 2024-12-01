
file = "input.txt"

#Read lines of file and split them into two lists on space
def read_file(file):
    with open(file) as f:
        lines = f.readlines()
    return [line.split() for line in lines]

distances = []
list1 = []
list2 = []
for line in read_file(file):
    list1.append(line[0])
    list2.append(line[1])

#sort the lists
list1.sort()
list2.sort()

#compare the lists and append the differences to a new list
for i in range(len(list1)):
    distances.append(abs(int(list1[i]) - int(list2[i])))


print(sum(distances))

