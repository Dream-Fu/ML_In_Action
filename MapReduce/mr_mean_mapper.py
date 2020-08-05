import sys
from numpy import mat, mean, power


def read_input(file):
    for line in file:
        yield line.rstrip()


input = read_input(sys.stdin)
input = [float(line) for line in input]
num_input = len(input)
input = mat(input)
sq_input = power(input, 2)

print("%d \t %f \t %f" %(num_input, mean(input), mean(sq_input)))
print(sys.stderr, "report: still alive")

