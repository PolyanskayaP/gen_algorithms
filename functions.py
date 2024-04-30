import math as mt

def gener_list_BKGx(length_part_BKG):
    pass
    #return list_BKGx

def preobr_list_BKGx_to_intx(list_BKGx):
    pass 
    #return list_intx

def preobr_list_intx_to_realx(list_intx, length_part_BKG, xL, xH):
    pass
    #return list_realx
    
def grafik_realx(realx1, realx2):
    pass
 
##########
def Kgener_list_BKGx(length_part_BKG):
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
    
def Kpreobr_list_BKGx_to_intx(list_BKGx):
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
      print(dvoich_list_intx)
   #return list_intx

def Kpreobr_list_intx_to_realx(list_intx, length_part_BKG, xL, xH):
    pass
    #return list_realx
    
def Kgrafik_realx(realx1, realx2):
    pass
##########

list_BKGx = Kgener_list_BKGx(4)
Kpreobr_list_BKGx_to_intx(list_BKGx)