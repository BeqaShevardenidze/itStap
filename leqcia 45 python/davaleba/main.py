import os
def Cls():
    os.system("cls")

def fibonacci(n):
    Cls()
    f1,f2 = 1,1
    while n>2:
        temp = f1           #1 - 1 - 2 - 3 - 
        f1 = f2             #1 - 2 - 3 - 5 -
        f2 = temp + f2      #2 - 3 - 5 - 8 - 
        print(f2, end=" ")
        n -= 1

def fibonacci_2(n):
    f1,f2 = 1,1
    while n>2:
        f1, f2 = f2, f1 + f2
        print(f2, end=" ")
        n -= 1

def fibonacci_3(n):
    f1,f2 = 1,1
    for i in range(2, n):
        f1, f2 = f2, f1 + f2
        print(f2, end=" ")

def fibonacci_4(n,f1=1,f2=1):
    while n > 2:
        f1, f2 = f2, f1 + f2
        print(f2, end=" ")
        return fibonacci_4(n - 1,f1,f2)

def fibonacci_5(n):
    pass
            


def f_menu():
    Cls()
    print("""
{1} - v1 while (temp)
{2} - v2 while (without temp)
{3} - v3 for
{4} - v4 რეკურსია
{5} - v5 რეკურსია
    """)
    x = input(">>>>")
    match x:
        case '1':
            Cls()
            n = int(input("ჩაწერეთ ციფრი >>>>"))
            fibonacci(n)
        case '2':
            Cls()
            n = int(input("ჩაწერეთ ციფრი >>>>"))
            fibonacci_2(n)
        case '3':
            Cls()
            n = int(input("ჩაწერეთ ციფრი >>>>"))
            fibonacci_3(n)
        case '4':
            Cls()
            n = int(input("ჩაწერეთ ციფრი >>>>"))
            fibonacci_4(n)
        case '5':
            Cls()
            n = int(input("ჩაწერეთ ციფრი >>>>"))
            fibonacci_5(n)


if __name__ == "__main__":
    Cls()
    f_menu()