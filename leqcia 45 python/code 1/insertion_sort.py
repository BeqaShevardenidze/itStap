import os

def Cls():
    os.system("cls")

def f_insertion_sort():
    Cls()
    arr = [64, 25, 12, 22, 11]

    for i in range(1, len(arr)):
        for j in range(i - 1, - 1, -1):
            if arr[i] > arr[j]:
                arr.insert(j + 1, arr.pop(i))
                break
            if j == 0:
                arr.insert(0, arr.pop(i))
    print(arr)



if __name__ == "__main__":
    f_insertion_sort()