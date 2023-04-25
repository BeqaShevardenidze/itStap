import os
import random
os.system("cls")

print("აირჩიე ვარიანტი:")
print("""
1. დაწერეთ ფუნქცია, რომელიც არგუმენტად მიიღებს სიტყვების სიას, ამ სიიდან ამოიღებს მხოლოდ იმ სიტყვებს რომლებიც მინიმუმ 5 სიმბოლოსგან შედგება და დააბრუნებს ამ სიტყვებისგან შემდგარ სიას.

1.1 V2
1.2 V3 Input()

2. დაწერეთ ფუნქცია, რომელიც მიიღებს ნებისმიერი რაოდენობის რიცხვებს და დააბრუნებს მათ საშუალო არითმეტიკულს.

2.1 + rand

3. დაწერეთ ლამბდა ფუნქცია, რომელიც მიიღებს რიცხვს და დააბრუნებს ამ რიცხვის კვადრატს.

3.1

4.	დაწერეთ ფუნქცია, რომელიც დაითვლის რიცხვის ფაქტორიალს. (მაგ, 5-ის ფაქტორიალი: 5! = 5*4*3*2*1)
0! = 1
1! = 1
2! = 2*1
""")
print(">>>>", end = " "); x = input()
match x:
    case '1':
        os.system("cls")
        def func():
            arr = ['oppo', 'xiaomi', 'samsung', 'apple', 'oneplus', 'meizu', 'huawei', 'vivo', 'motorola', 'lenovo', 'lg', 'nokia']
            arrLen = len(arr)
            for i in range(0,arrLen):
                if len(arr[i]) <= 5:
                    arr[i] = "-"
            
            while "-" in arr:
                arr.remove("-")
            print(arr)
        func() 

    case '1.1':
        os.system("cls")
        def func(arr):
            arrLen = len(arr)
            for i in range(arrLen):
                if len(arr[i]) <= 5:
                    arr[i] = "-"
            while "-" in arr:
                arr.remove("-")
            return arr
        
        Phone_arr = ['oppo', 'xiaomi', 'samsung', 'apple', 'oneplus', 'meizu', 'huawei', 'vivo', 'motorola', 'lenovo', 'lg', 'nokia']
        print(func(Phone_arr))

    case '1.2':
        os.system("cls")
        def func(arr):
            arrLen = len(arr)
            for i in range(arrLen):
                if len(arr[i]) <= 5:
                    arr[i] = "-"
                elif arr[i] == "print":
                    arr[i] = "-"
            while "-" in arr:
                arr.remove("-")
            return arr
        
        print("""
        ჩაწერეთ სიტყვები:
        დასაბეჭდად ჩაწერეთ 'print'
        """)
        user_input = ""
        num = 0
        user_arr = []
        while user_input != "print":
            print(">>>>", end = " "); user_input = input()
            num = num + 1
            user_arr.append(user_input)

        print(func(user_arr))

    case '2':
        os.system("cls")
        def func(*arr2):
            arr = []
            arr = arr2
            sum = 0
            arr_len = len(arr)
            for i in range(arr_len):
                sum = sum + arr[i]
            result = sum/arr_len
            print(result)
        func(1,4,2,6,7)
    
    case '2.1':
        os.system("cls")
        def func(arr2):
            arr = []
            arr = arr2
            sum = 0
            arr_len = len(arr)
            for i in range(arr_len):
                sum = sum + arr[i]
            result = sum/arr_len
            print(result)
        def rand_fanc():
            size = 0
            print("ჩაწერეთ მასივის ზომა: >>>>", end = " "); size = int(input())
            arr = [0] * size
            for i in range(size):
                arr[i] = random.randint(1, 100)
            print(arr)
            return arr
        func(rand_fanc())

    case '3':
        os.system("cls")
        print(
            (lambda x: x**2)(10)
        )
    
    case '3.1':
        os.system("cls")
        num = int(input("ჩაწერეთ ციფრი: >>>>"))
        lambda_result = (lambda x: x**2)(num)
        print(f"{num} -ის კვადრატი = {lambda_result}")

    case '4':
        os.system("cls")
        def func(num):
            result = 1
            for i in range(1,num+1):
                result = result * i
                print(f"!{num} = {result}")
        func(num = int(input(">>>>")))

    case _:
        os.system("cls")
        print("ERROR")