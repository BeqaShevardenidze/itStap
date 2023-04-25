import os
import rand_list
def Cls():
    os.system("cls")

# def f_select_sort():
#     pass

# def selection_sort(lst):
#     for num in range(len(lst)):
#         min_val = num
#         for item in range(num, len(lst)):
#             if lst[min_val] > lst[item]:
#                 min_val = item
        
#         lst[num], lst[min_val] = lst[min_val], lst[num]

#         return lst
    
def f_select_sort(my_list):
    Cls()
    size = len(my_list)
    for i in range(size):
        min_idx = i
        for j in range(i + 1, size):
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list

def f_print():
    my_list = [64, 25, 12, 22, 11]
    sorted_list = f_select_sort(my_list)
    print(sorted_list)
    


if __name__ == "__main__":
    Cls()
    f_print()
