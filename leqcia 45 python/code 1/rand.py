import os
import random

def Cls():
    os.system("cls")


def f_my_list():
    my_list = "q w e r t y u i o p l k j h g f d s a z x c v b n m"
    my_list_split = my_list.split()
    rand_list = []
    size = len(my_list_split)
    for i in range(10):
        x = random.randint(0,size-1)
        rand_list += my_list_split[x]
    return rand_list

def f_sort_list():
    Cls()
    my_list = f_my_list()
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            if my_list[i] < my_list[j]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    num = 0
    for i in my_list:
        num += 1
        f = open("text.txt", "a", encoding="utf-8")
        f.write(str(num) + " = " + i + ',  ')
        f.close()

    print(my_list)
    my_string = ""
    for i in range(len(my_list)):
        my_string += my_list[i]
    print(my_string)




if __name__ == "__main__":
    Cls()
    f_sort_list()