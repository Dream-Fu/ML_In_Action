import sys
from numpy import mat, mean,power


def read_input(file):
    for line in file:
        yield line.rstrip()

input = read_input(sys.stdin)
mapper_out = []
for line in input:
    line_arr = line.strip().split('\t')
    for item in line_arr:
        item = float(item.strip())
        print(item)
# mapper_out = [line.strip().split('\t') for line in input]
cum_val = 0.0
cum_sum_sq = 0.0
cum_n = 0.0
# for instance in mapper_out:
#         print(instance)
#         # nj = float(instance[0].strip())
#         # cum_n += nj
#         # cum_val += nj * float(instance[1].strip())
#         # cum_sum_sq += nj * float(instance[2].strip())
# # mean = cum_val / cum_n
# # var_sum = (cum_sum_sq - 2 * mean * cum_val + cum_n * mean * mean) /cum_n
# print("%d \t %f \t %f" %(cum_n, mean, var_sum))
print(sys.stderr, "report: still alive")
