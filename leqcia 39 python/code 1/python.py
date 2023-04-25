import os
import math
# RED = "\033[1;31m"
# GREEN = "\033[1;32m"
# YELLOW = "\033[1;33m"
# BLUE = "\033[1;34m"
# RESET = "\033[0m"
os.system("cls")

print("აირჩიეთ ვარიანტი:")
print("""
1) დავალება
2) დავალება
3) დავალება   (დასამტავრებელია)
4) დიქშენერი
5) იქშენერის შექმნა ტაფლების სილტისგან
6) მოკლე სინტაქსი
7) დიქშენერის შექმნა ფუნქციაში
8) loop
9) ორი ლისტიდან რიგრიგობით ამოღება ინფორმაციის
10) მასივის რევერსი
11) import math
12) მოდულები
""")


x = input(">>>> ")
match x:
    case "1":
        os.system("cls")
        name = input('Enter your name: ')
        age = int(input('Enter your age: '))

        result = (name,age)
        print(result)
    
    case '2':
        os.system("cls")
        def different_words(text):
            text_list = text.split()
            print(set(text_list))

        text = "lorem l;khdfiu iuhdoiuhf uihdoiuhfioeui uihdoiuhfioeui iudhifuhdoih"
        different_words(text)

    case "3":
        os.system("cls")

        def ask_user(my_interests):
            my_interests = set()
            while True:
                user_in = input("Enter your interest, enter 'end' to finish.")
                if user_in == 'end':
                    break
                my_interests.add(user_in)
            return my_interests

        my_interests = set()
        my_friend_set = set()

    case "4":
        os.system("cls")
        my_dict = {
            "giorgi": [19,12,'a'],
            "nino": 25,
            "tamazi": 35,
            "elene": {
                "height": 170,
                "age": 29
            }
        }
        print(my_dict)
        my_dict["ana"] = 28
        print(my_dict)

        del my_dict["ana"]
        print(my_dict)

        print(my_dict["giorgi"])

        print(my_dict["elene"])
        print(my_dict["elene"]["age"])

        print(list(my_dict))

        print("giorgi" in my_dict)
        
        if "rati" in my_dict:
            print("rati is in the database")
        else:
            print("rati" in my_dict)

    case "5":
        os.system("cls")
        dict_2 = dict([('spare',4139),('guido',4127),('jack',4098)])
        print(dict_2)

        empty_dict = {dict()}

    case "6":
        os.system("CLS")
        squares = {x: x**2 for x in (2,4,6)}
        print(type(squares), " = ", squares)
    case "7":
        os.system("cls")
        def test_func(**kwargs):
            print(kwargs)
            # return kwargs
        test_func(argument_1='abc',bbss=123)
    
    case "8":
        os.system("cls")
        d = {
            "სეხელი":"რონალდინიო",
            "გვარი":"ჭიჭვეიშვილი",
            "ასეკი":125
        }

        print("პირველი ვარიანტი:")
        for i in d:
            print(i, d[i])

        print("\nმეორე ვარიანტი: გვიბრუნებს თაფლების ლისტს")
        print(d.items())

        print("\nმესამე ვარიანტი: ფორ ლუპში ჩასმა  items() ფუნქციის")
        for k, v in d.items():
            print(k, v)

    case "9":
        os.system("cls")
        questions = ["name", "quest", "favorite color"]
        answers = ['lancelot',"the hole grail", "blue"]
        for q, a in zip(questions,answers):
            print(f'what is your {q}?    it is {a}.')

    case "10":
        os.system("cls")
        for i in reversed(range(0,5)):
            print(i)

        for i in reversed("test"):
            print(i, end="")

    case "11":
        os.system("cls")
        raw_data = [56.2, float('NaN'), 51.7, 55.3,]
        filtered_data = []
        for value in raw_data:
            if not math.isnan(value):
                filtered_data.append(value)

        print(filtered_data)

    case "12":
        os.system("cls")
        import module_1
        module_1.fib(10)

    case _:
        print("error")