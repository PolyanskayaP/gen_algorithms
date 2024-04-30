import functions as fun

length_part_BKG = 12
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