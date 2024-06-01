import math as mt
import matplotlib.pyplot as plt
import random
import itertools
import pandas as pd
 
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
    
def grafik_realx(realx1, realx2, title):
   fig = plt.figure()
   ax = fig.add_subplot(111)
   ax.scatter(realx1, realx2, color = 'green')
   ax.set_xlabel('x1')
   ax.set_ylabel('x2')
   ax.set_title(title)
   plt.show()
   
def J1_function(list_realx_1, list_realx_2, kolvo):
   f1_list = []
   f2_list = []
   for i in range(kolvo):
      f1 = 0.2 * ((list_realx_1[i] - 70)**2) + 0.8 * ((list_realx_2[i] - 20)**2)
      f2 = 0.8 * ((list_realx_1[i] - 10)**2) + 0.2 * ((list_realx_2[i] - 70)**2)
      f1_list.append(f1)
      f2_list.append(f2) 
   return f1_list, f2_list

def fun_prig(f1_list, kolvo):
   b_list = []
   fi_list = []
   for i in range(1, kolvo + 1):
      b_conter = 0
      for j in range(1, kolvo + 1):
         if (f1_list[j - 1] < f1_list[i - 1]):
               b_conter += 1
      b_list.append(b_conter)
      fi = 1 / (1 + (b_conter / (kolvo - 1)))#степень?
      fi_list.append(fi)
   return b_list, fi_list

def grafik_f(realx1, realx2, title):
   fig = plt.figure()
   ax = fig.add_subplot(111)
   ax.scatter(realx1, realx2, color = 'blue')
   ax.set_xlabel('f1')
   ax.set_ylabel('f2')
   ax.set_title(title)
   plt.show()
   
def fun_prig_fin(f1_list, f2_list, kolvo):
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
   return fi_list
   
def razb_group_idx(kolvo, n_group=5):   #, f_list
   idxs = set(range(kolvo))
   list_of_set = []
   for i in range(n_group):
      team = set(random.sample(idxs, int(kolvo/n_group)))  #следить за целочисленным делением
      list_of_set.append(team)
      idxs = idxs - team
   return list_of_set

'''
def choose_best_from_groups(list_groups, f_list, kolvo, n_group=5):
   list_max_i = []
   for sett in list_groups:
      max_i = random.sample(sett, 1)
      max_f = f_list[max_i]
      for i in sett:
         f = f_list[i]
         if f > max_f:
            max_f = f
            max_i = i 
      list_max_i.append(max_i)
'''

def f_for_groups(list_of_set, fun_prig_fin, kolvo, n_group=5):
   list_of_list_i = [list(sett) for sett in list_of_set]
   
   group_f_list = []
   for listt in list_of_list_i:
      f_listt = []
      for i in listt:
         f_listt.append(fun_prig_fin[i])
      group_f_list.append(f_listt)
   
   return list_of_list_i, group_f_list 

def find_max_from_groups(group_f_list, group_i_list, n_max=5):
   list_max_i_list = []
   list_max_i_list_new = []
   ii = 0
   for kucuk_list in group_f_list:
      kucuk_list_idxs = [x[0] for x in sorted(enumerate(kucuk_list), key=lambda x: x[1])[-n_max:]]
      list_max_i_list.append(kucuk_list_idxs)
      list_max_i_list_new.append( [group_i_list[ii][i] for i in kucuk_list_idxs] )
      ii = ii + 1
   return list_max_i_list_new

def oneDArray(x):
    return list(itertools.chain(*x))

def priglad_mass(a):
    a = oneDArray(a)
    a = oneDArray(a)
    return a
 
def crossover(length_part_BKG, parent1, parent2, list_randoms_1, list_randoms_2): #length_part_BKG = 18 #возвращает хромосому не разделенную на 2 части, как до этого
   bkg_par_1 = list_randoms_1[parent1] + list_randoms_2[parent1]
   bkg_par_2 = list_randoms_1[parent2] + list_randoms_2[parent2]
   length_part_BKG = length_part_BKG * 2 #36
   t2 = int(length_part_BKG / 2 - 1)  #17
   t1 = random.randint(1, t2 - 2)  #1..15
   t3 = random.randint(t2 + 2, length_part_BKG - 1)  #19..35
   baby1 = bkg_par_1[0:t1] + bkg_par_2[t1:t2] + bkg_par_1[t2:t3] + bkg_par_2[t3:length_part_BKG]
   baby2 = bkg_par_2[0:t1] + bkg_par_1[t1:t2] + bkg_par_2[t2:t3] + bkg_par_1[t3:length_part_BKG]
   return [baby1, baby2]

def split_chrom_det(listt):
   bkg_det_part_1 = []
   bkg_det_part_2 = []
   for deti in listt:
      for d in deti:
         d1 = d[: len(d) // 2]
         d2 = d[len(d) // 2 :]
         bkg_det_part_1.append(d1)
         bkg_det_part_2.append(d2)
   return bkg_det_part_1, bkg_det_part_2

def choose_from_df_elit_dots(df):
   df_elit = pd.DataFrame(columns=['ТТО 1', 'ТТО 2', 'x1 вещ.', 'x2 вещ.', 'f1', 'f2', 'Фун.приг.'])
   for i, row in df.iterrows():
      if row['Фун.приг.'] == 1 :
         df_elit.loc[len(df_elit.index )] = df.loc[i]
   return df_elit