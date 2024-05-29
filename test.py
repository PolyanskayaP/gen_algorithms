import functions as fun

import random
'''
kolvo = 100
n_group = 5
idxs = set(range(kolvo))

list_groups = []

for i in range(5):
    team = set(random.sample(idxs, 20))
    list_groups.append(team)
    idxs = idxs - team

print(list_groups)
'''
print(fun.razb_group_idx(100, 5))