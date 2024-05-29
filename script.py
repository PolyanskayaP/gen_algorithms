import functions as fun

length_part_BKG = 18 #24
xL = 0 
xH = 79
kolvo = 10

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


