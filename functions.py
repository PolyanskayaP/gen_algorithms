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

import math as mt
def generate_gray_list(my_val):
   if (my_val <= 0):
      return
   my_list = list()
   my_list.append("0")
   my_list.append("1")
   i = 2
   j = 0
   while(True):
      if i >= 1 << my_val:
         break
      for j in range(i - 1, -1, -1):
         my_list.append(my_list[j])
      for j in range(i):
         my_list[j] = "0" + my_list[j]
      for j in range(i, 2 * i):
         my_list[j] = "1" + my_list[j]
      i = i << 1
   for i in range(len(my_list)):
      print(my_list[i])
my_num = 3
print("The number is :")
print(my_num)
print("Method to convert gray code to binary is being called...")
generate_gray_list(my_num)