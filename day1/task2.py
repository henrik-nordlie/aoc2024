file = "input.txt"

#Read lines of file and split them into two lists on space
def read_file(file):
    with open(file) as f:
        lines = f.readlines()
    return [line.split() for line in lines]

num_scores = []
list1 = []
list2 = []
for line in read_file(file):
    list1.append(int(line[0]))
    list2.append(int(line[1]))

list2.sort()

list2_uniqe_num_occurences = {}
for i in list2:
    if i in list2_uniqe_num_occurences:
        list2_uniqe_num_occurences[i] += 1
    else:
        list2_uniqe_num_occurences[i] = 1

#compare the lists and append the differences to a new list
for i in range(len(list1)):
    if list1[i] in list2:
        num_scores.append(list1[i]*list2_uniqe_num_occurences[list1[i]])

#sum the differences
print(sum(num_scores))

