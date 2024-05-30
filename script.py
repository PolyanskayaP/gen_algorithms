import functions as fun

length_part_BKG = 18 #24
xL = 0 
xH = 79
kolvo = 100
n_group = 5
n_max = 5
n_cycles_for_parents = 4

list_BKGx = fun.gener_list_BKGx(length_part_BKG)

list_randoms_1 = fun.choose_random_from_list(list_BKGx, kolvo)
list_binars_1 = fun.preobr_list_BKGx_to_binx(list_randoms_1)
list_intx_1 = fun.from_list_bin_to_list_int(list_binars_1)
list_realx_1 = fun.preobr_list_intx_to_realx(list_intx_1, length_part_BKG, xL, xH)

list_randoms_2 = fun.choose_random_from_list(list_BKGx, kolvo)
list_binars_2 = fun.preobr_list_BKGx_to_binx(list_randoms_2)
list_intx_2 = fun.from_list_bin_to_list_int(list_binars_2)
list_realx_2 = fun.preobr_list_intx_to_realx(list_intx_2, length_part_BKG, xL, xH)

fun.grafik_realx(list_realx_1, list_realx_2)



J1_list, J2_list = fun.J1_function(list_realx_1, list_realx_2, kolvo)
print("J1", J1_list)
print("J2", J2_list)
b_list_1, f_list_1 = fun.fun_prig(J1_list, kolvo)
b_list_2, f_list_2 = fun.fun_prig(J2_list, kolvo)
print("b_list_1, f_list_1: ", b_list_1, f_list_1)
print("b_list_2, f_list_2: ", b_list_2, f_list_2)
fun.grafik_f(f_list_1, f_list_2)

fun_prig_fin = fun.fun_prig_fin(f_list_1, f_list_2, kolvo)
print("Функция пригодности: ", fun_prig_fin)

mnogo_roditeley = []
for i in range(n_cycles_for_parents):
    list_of_set = fun.razb_group_idx(kolvo, n_group)
    print("list_of_set: ",i,": ", list_of_set)

    group_i_list, group_f_list = fun.f_for_groups(list_of_set, fun_prig_fin, kolvo, n_group=5)
    print("group_i_list: ",i,": ", group_i_list)
    print("group_f_list: ",i,": ", group_f_list)

    roditeli = fun.find_max_from_groups(group_f_list, group_i_list, n_max)
    print("roditeli ",i,": ", roditeli)
    mnogo_roditeley.append(roditeli)
print("Roditeli: ", mnogo_roditeley)
roditeli_edin_spiskom = fun.priglad_mass(mnogo_roditeley)
print("Roditeli: ", roditeli_edin_spiskom)

roditeli_po_param = [[i, j] for i, j in zip(roditeli_edin_spiskom[0::2], roditeli_edin_spiskom[1::2])]
print("\nПары родителей: ", roditeli_po_param)

crossover_deti = []
for parents in roditeli_po_param:
    crossover_deti.append(fun.crossover(length_part_BKG, parents[0], parents[1], list_randoms_1, list_randoms_2))
print("\nДети (кроссовер): ", crossover_deti)

bkg_det_part_1, bkg_det_part_2 = fun.split_chrom_det(crossover_deti)
print("\nbkg_det_part_1: ", bkg_det_part_1)
print("\nbkg_det_part_2: ", bkg_det_part_2)

