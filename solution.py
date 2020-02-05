# permutations
#python3
#jupyter notebook
import csv
import numpy as np
with open('input.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    input_ = []
    for row in csv_reader:
        input_.append(row)
output = []
l = input_

for i in range(len(l[0])):
    for j in range(len(l[1])):
        for k in range(len(l[2])):
            s = l[0][i] + l[1][j] + l[2][k]
            output.append(s)
print(*(output))
