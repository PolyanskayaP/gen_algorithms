import math as mt
import matplotlib.pyplot as plt
 
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
   print(list_BKGx)
   return list_BKGx
    
def preobr_list_BKGx_to_binx(list_BKGx):
   list_binars = list()
   list_intx = list()
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
      #print(dvoich_list_intx)
      bin_str = ''.join(str(x) for x in dvoich_list_intx)
      list_binars.append(bin_str)
   print(list_binars)
   return list_binars

def from_list_bin_to_list_int(list_binars):
   list_int = list()
   for x in list_binars:
      list_int.append(int(x, base=2))
   print(list_int)
   return list_int

def preobr_list_intx_to_realx(list_intx, length_part_BKG, xL, xH):
   list_realx = list()
   for xi in list_intx:
      x = xL +    (xi*(xH - xL))/((2**length_part_BKG) - 1)
      list_realx.append(x)
   print(list_realx)
   return list_realx
    
def grafik_realx(realx1, realx2):
   plt.scatter(realx1, realx2, color = 'orange')
   plt.show()

length_part_BKG = 18
xL = 0 
xH = 79

list_BKGx = gener_list_BKGx(length_part_BKG)
list_binars = preobr_list_BKGx_to_binx(list_BKGx)
list_intx = from_list_bin_to_list_int(list_binars)
list_realx = preobr_list_intx_to_realx(list_intx, length_part_BKG, xL, xH)
grafik_realx(list_realx, list_realx)