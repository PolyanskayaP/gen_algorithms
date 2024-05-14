import math as mt
import matplotlib.pyplot as plt
import random
 
def gener_list_BKGx(length_part_BKG):
   if (length_part_BKG <= 0):
      return
   list_BKGx = list()
   list_BKGx.append("0")
   list_BKGx.append("1")
   i = 2
   j = 0
   while(True):
      if i >= 1 << length_part_BKG:
         break
      for j in range(i - 1, -1, -1):
         list_BKGx.append(list_BKGx[j])
      for j in range(i):
         list_BKGx[j] = "0" + list_BKGx[j]
      for j in range(i, 2 * i):
         list_BKGx[j] = "1" + list_BKGx[j]
      i = i << 1
   #print("Список всех БКГ данной длины\n", list_BKGx)
   return list_BKGx
    
def choose_random_from_list(our_list, kolvo):
   list_randoms = list()
   for i in range(kolvo):
      list_randoms.append(random.choice(our_list))
   print("БКГ\n", list_randoms)
   return list_randoms
    
def preobr_list_BKGx_to_binx(list_BKGx):
   list_binars = list()
   for BKGx in list_BKGx:
      dvoich_list_intx = list()
      BKGx_po_sim = list(BKGx) 
      BKGx_po_cif = [int(x) for x in BKGx_po_sim]
      for i in range(len(BKGx_po_cif)):
         if i == 0:
            dvoich_list_intx.append(BKGx_po_cif[i])
         else:
            bj = 0
            for j in range(i+1):
               bj = bj ^ BKGx_po_cif[j]
            dvoich_list_intx.append(bj)
      bin_str = ''.join(str(x) for x in dvoich_list_intx)
      list_binars.append(bin_str)
   print("Двоичная СС\n", list_binars)
   return list_binars

def from_list_bin_to_list_int(list_binars):
   list_int = list()
   for x in list_binars:
      list_int.append(int(x, base=2))
   print("Целые значения\n", list_int)
   return list_int

def preobr_list_intx_to_realx(list_intx, length_part_BKG, xL, xH):
   list_realx = list()
   for xi in list_intx:
      x = xL +    (xi*(xH - xL))/((2**length_part_BKG) - 1)
      list_realx.append(x)
   print("Вещественные значения\n", list_realx)
   print("\n")
   return list_realx
    
def grafik_realx(realx1, realx2):
   fig = plt.figure()
   ax = fig.add_subplot(111)
   ax.scatter(realx1, realx2, color = 'green')
   ax.set_xlabel('x1')
   ax.set_ylabel('x2')
   plt.show()
   
def f1_function(list_realx_1, list_realx_2, kolvo):
   f1_list = []
   f2_list = []
   for i in range(kolvo):
      f1 = 0.2 * ((list_realx_1[i] - 70)**2) + 0.8 * ((list_realx_2[i] - 20)**2)
      f2 = 0.8 * ((list_realx_1[i] - 10)**2) + 0.2 * ((list_realx_2[i] - 70)**2)
      f1_list.append(f1)
      f2_list.append(f2) 
   return f1_list, f2_list

def fun_prig(f1_list, f2_list, kolvo):
   b_list = []
   fi_list = []
   for i in range(1, kolvo + 1):
      b_conter = 0
      for j in range(1, kolvo + 1):
         if (f1_list[j - 1] < f1_list[i - 1] and f2_list[j - 1] <= f2_list[i - 1]) or \
                  (f1_list[j - 1] <= f1_list[i - 1] and f2_list[j - 1] < f2_list[i - 1]):
               b_conter += 1
      b_list.append(b_conter)
      fi = 1 / (1 + (b_conter / (kolvo - 1)))
      fi_list.append(fi)
   return b_list, fi_list