import os
import random
import selection_sort
import rand
import insertion_sort
import finde_sort

def Cls():
    os.system("cls")


Cls()
print("""
{1} - selection sort
{2} - rand string
{3} - insertion sort
""")

x = input(">>>>")

match x:
    case '1':
        selection_sort.f_selection_sort()
    case '2':
        rand.f_sort_list()
    case '3':
        insertion_sort.f_insertion_sort()