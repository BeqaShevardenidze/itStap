import os
import rand_list

def Cls():
    os.system("cls")

def f_buble_sort():
    Cls()
    size = 11
    my_list = rand_list.f_rand_list(size)

    print("საწყისი მასივი: ", my_list)
    for i in range(size):
        for j in range(size - 1):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    print("დალაგებული მასივის ზრდადობის მიხედვით", my_list)

def f_buble_sort_v2():
    Cls()
    size = 10
    my_list = rand_list.f_rand_list(size)
    print("საწყისი ლისტი: ",my_list)

    for i in range(size):
        for j in range(size):
            if my_list[i] < my_list[j]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    print("დალაგებული ლისტი",my_list)





if __name__ == "__main__":
    f_buble_sort()
    f_buble_sort_v2()