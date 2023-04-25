import os
import random
import rand_list

def Cls():
    os.system("cls")

def f_finde_sort():
    Cls()
    A = [64, 25, 12, 22, 11]
    my_list = rand_list.f_rand_list(100,1000)

    # გზა 1   linear search
    for i in range(len(A)):
        if A[i] == 12:
            print(i, " = ", 12)

    # გზა 2 python
    if 12 in A:
        print(True)
    else:
        print(False)

    #გზა 3 binary search მუშაობს მხოლოდ დასორტირებულ მასივებზე
    ricxvebi = random.sample(my_list,11)
    # print(sorted(ricxvebi))
    sorted_num = [177, 249, 304, 380, 496, 558, 740, 830, 898, 976]
    
    def binarySearch(arr,x):
        low, high = 0, len(sorted_num)
        while low != high:
            mid = (low + high) // 2
            if (x == arr[mid]):
                return mid
            
            elif (x > arr[mid]):
                low = mid + 1

            else:
                high = mid - 1

    print(binarySearch(sorted_num, 976))

    #გზა 4 რეკურსია
    # import sys
    # sys.setrecursionlimit(100000)
    # print(sys.getrecursionlimit())
    def factorial(n):
        while True:
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)
    print(factorial(5))
        






if __name__ == "__main__":
    f_finde_sort()