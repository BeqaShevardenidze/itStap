import os
import buble_sort
import select_sort
def Cls():
    os.system("cls")

Cls()
print("""
{1} - ბუშტისებრი დახარისხება
{2} - არჩევითი დახარისხება
{3} - ლექცია
""")

x = input(">>>>")
match x:
    case '1':
        buble_sort.f_buble_sort()
        buble_sort.f_buble_sort_v2()
    case '2':
        select_sort.f_select_sort()
    case '3':
        Cls()
        areuli = [2, 7, 8, 13, 2, 5, 9, 1]
        
        # ადგილის შეცვლა
        def change(areuli, index1, index2):
            droebiti = areuli[index1]
            areuli[index1] = areuli[index2]
            areuli[index2] = droebiti
            print(areuli)
        change(areuli,1,2)