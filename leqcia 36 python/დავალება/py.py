import os
os.system("cls")
print("აირჩეთ ვარიანტი")
print("""
1. ჩაშენებული ციკლის გამოყენებით დაწერეთ პროგრამა, რომელიც დაბეჭდავს გამრავლების ტაბულას შემდეგნაირად:
""")
print("""
2. დაწერეთ ფუნქცია სახელად reverse_string, რომელსაც ექნება ერთი არგუმენტი, string ტიპის მონაცემი და დააბრუნებს შებრუნებულ ტექსტს. მაგალითად, თუ გადავცემთ “Python”, უნდა დაგვიბრუნოს “nohtyP”.
""")
print("3) დავალება 2 (V2)")
print("4) მათემნატიკური ოპერაციები ფუნქციებით")
print(">>>>", end=""); x = int(input())
match (x):
    case 1:
        os.system("cls")
        for i in range(1,11):
            for j in range(1, 11):
                result = i * j
                print(f"{i} * {j} = {result}")
            print('  ')
    case 2:
        os.system("cls")
        def reverse_string(string):
            size = len(string)
            print('სიტყვის შებრუნებული ვარიანტი: ', end = " "); 
            for i in range(size - 1, -1, -1):
                print(string[i], end = " "); 
        print("ჩაწერეტ სიტყვა: >>>>",end = " "); string = input()
        reverse_string(string)
    case 3:
        os.system("cls")
        def reverse_string(string):
            x = string [::-1]
            print('სიტყვის შებრუნებული ვარიანტი: ', end = " "); print(x)
        print("ჩაწერეთ სიტყვა", end = " "); string = input()
        reverse_string(string)
    case 4:
        os.system("cls")
        def mimateba(a,b):
            print(f"a + b = {a+b}")
        def gamokledba(a,b):
            print(f"a - b = {a-b}")
        def gamravleba(a,b):
            print(f"a * b = {a*b}")
        def gayofa(a,b):
            print(f"a / b = {a/b}")
        def nashti(a,b):
            print(f"a % b = {a%b}")
        def gamodzaxeba():
            print("a = ", end = " "); a = int(input()) 
            print("b = ", end = " "); b = int(input())
            # time.sleep(2.4) 
            mimateba(a,b); gamokledba(a,b); gamravleba(a,b); gayofa(a,b); nashti(a,b); 
        gamodzaxeba()
    case _ :
        print("ERROR")