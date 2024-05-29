import functions as fun
import random

n_max = 5
a = [8, 5, 2, 20, 13, 14, 17, 13, 15, 21]
list_max_n_idxs = [x[0] for x in sorted(enumerate(a), key=lambda x: x[1])[-n_max:]]
print(list_max_n_idxs)