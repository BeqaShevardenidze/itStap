import os
import random

def Cls():
    os.system("cls")

def f_selection_sort():
    Cls()
    A = [64, 25, 12, 22, 11]

    for i in range(len(A)):

        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]

    print(A)

def f_selection_sort_2():
    Cls()
    A = [64, 25, 12, 22, 11]

    for i in range(len(A)):
        min = i
        for j in range(i+1, len(A)):
            if A[min] > A[j]:
                min = j
    
        A[i], A[min] = A[min], A[i]
    print(A)



    


if __name__ == "__main__":
    f_selection_sort_2()