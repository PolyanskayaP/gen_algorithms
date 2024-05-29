import random
from prettytable import PrettyTable
import matplotlib.pyplot as plt
'''
N = 100
#K - количество поколений
K = 4
groups_num = 5
points_num = 20

f1_list = []
f2_list = []




#print('\nПункт 3.3')
#print('Турнир:')
buf_list = []

for times in range(0, K):

    list_index = []
    for i in range(0, N):
        list_index.append(i)


    def tour():
        tournament = []

        inner_list = list_index.copy()
        while len(tournament) < groups_num:
            buf_list = []
            while len(buf_list) < points_num:
                rand_int = random.randint(0, N)

                if rand_int in inner_list:
                    buf_list.append(rand_int)
                    inner_list.remove(rand_int)

            tournament.append(buf_list)


        tournament_print = []
        for i in tournament:
            buf_list_1 = []

            for j in i:
                buf_list_1.append(j + 1)
            tournament_print.append(buf_list_1)
        print('Разделенные группы:',tournament)

        return tournament


    best_parents_list = []

    while len(best_parents_list) < N:
        tour_list = tour()

        for item in tour_list:
            inner_fi = []
            for index, point in enumerate(item):

                inner_fi.append([point, fi_list[point]])

            inner_fi = sorted(inner_fi, key=lambda x: x[1])
            print('Номер точки и значение функции Ф: ',inner_fi)
            best_parents_list.append(inner_fi[-2][0])
            best_parents_list.append(inner_fi[-1][0])

    print('\nЛучшие родители: ')

    print([i + 1 for i in best_parents_list])

    print('\n\nПары: ')  #Пункт 3.4

    part4, axes_4 = plt.subplots()
    axes_4.set_xlim(0, 4000)
    axes_4.set_ylim(0, 4000)
    parents = []

    buf_1 = None

    while len(parents) < N / 2:
        rand_int = random.randint(0, N)
        if rand_int in best_parents_list:
            if buf_1 is None:
                buf_1 = rand_int
                best_parents_list.remove(rand_int)
            else:
                parents.append([buf_1, rand_int])
                buf_1 = None
                best_parents_list.remove(rand_int)

    print([[x + 1 for x in j] for j in parents])


    def crossover(parent1, parent2):
        t2 = int(N / 2 - 1)
        t1 = random.randint(1, t2 - 2)
        t3 = random.randint(t2 + 2, N - 1)
        baby1 = bkg_list[parent1][0:t1] + bkg_list[parent2][t1:t2] + bkg_list[parent1][t2:t3] + bkg_list[parent2][t3:m * 2]
        baby2 = bkg_list[parent2][0:t1] + bkg_list[parent1][t1:t2] + bkg_list[parent2][t2:t3] + bkg_list[parent1][t3:m * 2]
        return [baby1, baby2]

    babys_bkg = []
    for item in parents:
        babys_bkg.append(crossover(item[0], item[1])[0])
        babys_bkg.append(crossover(item[0], item[1])[1])

    table_4 = PrettyTable()
    table_4.field_names = ["Номер", "БКГх1", "БКГх2", "l1", "l2", "x1", "x2", 'f1', 'f2', 'b', 'Ф']

    ls = []
    i = 0
    baby_l1_list, baby_l2_list, baby_x1_list, baby_x2_list, baby_f1_list, baby_f2_list, bkg1_list, bk2_list = [], [], [], \
                                                                                                              [], [], [], \
                                                                                                              [], []
    for item in babys_bkg:
        i += 1
        l1 = binary_to_gray(item[0:m])
        bkg1_list.append(item[0:m])
        baby_l1_list.append(l1)
        l2 = binary_to_gray(item[m:])
        bk2_list.append(item[m:])
        baby_l2_list.append(l2)
        x1 = l1 * 79 / (2 ** m - 1)
        baby_x1_list.append(x1)
        x2 = l2 * 79 / (2 ** m - 1)
        baby_x2_list.append(x2)
        ls.append([l1, l2])
        f1 = 0.2 * (x1 - 70) ** 2 + 0.8 * (x2 - 20) ** 2
        baby_f1_list.append(f1)
        f2 = 0.2 * (x1 - 10) ** 2 + 0.8 * (x2 - 70) ** 2
        baby_f2_list.append(f2)
        axes_4.scatter(x=f1, y=f2)
        # axes_4.text(f1, f2, f'{i}')

    baby_b_list, baby_fi_list = [], []
    for i in range(1, N + 1):
        b_conter = 0
        for j in range(1, N + 1):
            if (baby_f1_list[j - 1] < baby_f1_list[i - 1] and baby_f2_list[j - 1] <= baby_f2_list[i - 1]) or \
                    (baby_f1_list[j - 1] <= baby_f1_list[i - 1] and baby_f2_list[j - 1] < baby_f2_list[i - 1]):
                b_conter += 1

        fi = 1 / (1 + (b_conter / (N - 1)))
        baby_fi_list.append(fi)
        table_4.add_row(
            [i, bkg1_list[i - 1], bk2_list[i - 1], baby_l1_list[i - 1], baby_l2_list[i - 1],
             f"{baby_x1_list[i - 1]:.2f}", \
             f"{baby_x2_list[i - 1]:.2f}", f"{baby_f1_list[i - 1]:.2f}", f"{baby_f2_list[i - 1]:.2f}", \
             b_conter, f"{fi:.2f}"])
    fi_list = baby_fi_list.copy()
    f1_list = baby_f1_list.copy()
    f2_list = baby_f2_list.copy()


axes_4.set_title('Пункт 3.4')
axes_4.set_xlabel("f1")
axes_4.set_ylabel("f2")
axes_4.set_xlim(0, 4000)
axes_4.set_ylim(0, 4000)
# Отображаем график
#plt.show()
'''


