import os
os.system("cls")

print("""
აირჩიეთ ვარიანტი:
1.	დაწერეთ პროგრამა „კალკულატორი“, რომელიც მომხმარებელს მოთხოვს, შეიყავნოს ორი რიცხვი და აირჩიოს მოქმედება - შეკრება, გამოკლება, გამრავლება ან გაყოფა (‘+’, ‘-‘, ‘*’, ‘/’). ამის მიხედვით გამოთვალეთ და დაბეჭდეთ შედეგი.

2.	მომხმარებელს მოთხოვეთ სახელის და ასაკის შეყვანა. შემდეგ ეს მონაცემები შეიყვანეთ tuple-ში. დაბეჭდეთ მიღებული tuple.

3.	დაწერეთ ფუნქცია, რომელიც არგუმენტად მიიღებს ტექსტს. ფუნქციამ უნდა დაბეჭდოს ტექსტში არსებული განსხვავებული სიტყვები. მითითება: გამოიყენეთ set. ასევე string-ის split მეთოდი (https://docs.python.org/3/library/stdtypes.html#str.split).

4.	მომხმარებელს სთხოვეთ, რიგ-რიგობით შეიყვანოს თავისი ინტერესები (ჰობი), შემდეგ სთხოვეთ, შეიყვანოს თავისი მეგობრის ინტერესები. ბოლოს დაბეჭდეთ მომხმარებლის და მისი მეგობრის საერთო ინტერესები. 

5.	დაწერეთ ფუნქცია, რომელსაც ექნება ერთი არგუმენტი - string ტიპის მონაცემი. ფუნქციამ უნდა დააბრუნოს dictionary, რომელშიც გასაღებები იქნება შემავალ string-ში არსებული სიმბოლოები, ხოლო მნიშვნელობები - ამ სიმბოლოების რაოდენობა. მაგალითად, თუ ფუნქციას გადავცემთ „Hello world”. მან უნდა დაგვიბრუნოს შემდეგი:
{
   ‘H’ : 1,
   ‘e’ : 1,
   ‘l’ : 3,
   ‘o’ : 2,
   ‘ ‘ : 1,
   ‘w’: 1,
   ‘r’ : 1,
   ‘d’ : 1
}

""")

x = input(">>>> ")
match (x):
    case "1":
        os.system("cls")
        num1 = int(input("პირველი რიცხვი = "))
        num2 = int(input("მეორე რიცხვი = "))
        operation = input("აირჩიეთ მოქმედება: + - * / % \n >>>> ")
        if operation == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == "/":
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        elif operation == "%":
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
    case '2':
        os.system("cls")
        Name = input("ჩაწერეთ თქვენი სახელი: >>>> ")
        age = int(input("ჩაწერეთ თქვენი ასაკი >>>> "))
        myTupple = (Name, age)
        print(myTupple)
    case "3":
        os.system("cls")
        def func(word):
            wordSplit = word.split()
            wordSet = set(wordSplit)
            return wordSet

        string = input("ჩაწერეთ ტექსტი: >>>> ")
        print(func(string))
    case "4":
        os.system("cls")
        you = input("რა არის თქვენი ჰობი? ჩამოწერეთ: \n>>>> ")
        your_friend = input("ახლა ჩაწერეთ თქვენი მეგობრის ჰობი: \n>>>> ")
        you = you.split()
        your_friend = your_friend.split()
        you_set = set(you)
        your_friend_set = set(your_friend)

        result = you_set & your_friend_set
        print(f"თაქვენი და თქვენი მეგობრის საერთო ჰობია: {result}")
    case "5":
        os.system("cls")

        def func(string):
            string_len = len(string)
            string_arr = [""] * string_len
            temp_arr = [0] * string_len
            temp = 0
            my_dict = {}
            for i in range(string_len):
                string_arr[i] = string[i]

            for i in range(string_len):
                for j in range(string_len):
                    if string_arr[i] == string_arr[j]:
                        # print(f"სიმბოლოები {i} და {j} უდრის ერთმანეთს: {string[i]}")
                        temp = 1
                        temp_arr[j] += temp
                        my_dict[string_arr[j]] = temp_arr[j]
                    else:
                        # print(f"სიმბოლოენი {i} და {j} უდრის ერთმანეთს: {string[i]} - {string[j]}")
                        temp = 0
                        temp_arr[j] += temp
                        my_dict[string_arr[j]] = temp_arr[j]
            # print(string_arr)
            # print(temp_arr)
            # set_string_arr = set(string_arr)
            # print(set_string_arr)
            return my_dict

        print(func("hello world"))