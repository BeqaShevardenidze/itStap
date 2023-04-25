import os
os.system("cls")

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

print("""
წინა დავალება
1) დაწერეთ ფუნქცია რომელიც არგუმენტად მიიღებს სიტყვების სიას
2) დაწერეთ ფუნქცია რომელიც მიიღებს ნებისმიერი რაოდენობის ციფრებს
2.1) v2
3) დაწერეთ ლამბდ ფუნქცია
4) დაწერეთ ფუნქცია რომელიც დაითვლის რიცხვის ფაქტორიალს

5) რიცხვის კვადრატების ლისტში ჩაწერა | list comprehension
6) index  (დაუბრუნდი)
7) pop & del
8) tuple
9) set
10) dict
""")
x = input("აირჩიეთ ვარიანტი >>>> ")
match x:
    case "1":
        os.system("cls")
        def list_func(word_list):
            output_list = []
            for word in word_list:
                if len(word) >= 5:
                    output_list.append(word)
            return output_list

        result = list_func(["python", "saxli", "gza", "avtobusi"])
        print(result)
    
    case "2":
        os.system("cls")
        def average_func(*numbers):
            result = 0
            for num in numbers:
                result += num
            result = result / len(numbers)
            print(result)

        average_func(10,15,10)

    case "2.1":
        os.system("cls")
        def average_func(*numbers):
            print(sum(numbers) / len(numbers))

        average_func(10,15,10)

    case "3":
        os.system("cls")
        a = lambda x: x**2
        print(a(4))
    
    case "4":
        os.system("cls")
        def factorial(n):
            if n == 0:
                return 1
            
            result = 1
            for i in range(1, n+1):
                result *= i
            return result
        
        print(factorial(5))

    case "5":
        os.system("cls")
        squares = []
        for x in range(10):
            squares.append(x**2)
        print(squares)

        squares = [x ** 2 for x in range(10)]
        print(squares)

        def square(x):
            return x ** 2
        squares = list(map(square, range(10)))
        print(squares)

        squares = list(map(lambda x: x**2, range(10)))
        print(squares)
        
        my_list = [5, 7, 1, 2, 9]
        squares = list(map(lambda x: x**2, my_list))
        print(squares)

    case "6":
        os.system("cls")
        # my_list = [5, 7, 1, 2, 9, 1, 4]
        # for i in range(len(my_list)):
        #     if my_list[i] == 1:
        #         print(my_list[i]," = index ",my_list.index(i))
        # print(my_list.index(1))

        my_list = [5, 7, 1, 2, 9, 1, 4]
        #          0  1  2  3  4  5  6  
        num_to_finde = 1
        indexes = []
        for n, num in enumerate(my_list):
            if num == num_to_finde:
                indexes.append(n)
        print(indexes)

    case "7":
        os.system("cls")
        new_list = []
        my_list = [5, 7, 1, 2, 9, 1, 4]
        #          0  1  2  3  4  5  6  
        a = my_list.pop(4)
        print(my_list)

        new_list.append(a)
        print(new_list)

        del my_list[0]
        print(my_list)

        # print(my_list[1:4])
        test_list = []
        test_list.append(my_list[1:4])
        print(test_list)

    case "8":
        os.system("cls")
        # immutable: string, tuple - შეცვლა არ შეგვიძლია
        # mutable: list - შეცვლა შეგვიძლია

        my_tuple = (5, 7, 1, 2, 9, 1, 4)
        print(my_tuple[5])
        print(my_tuple[1:4])

        my_tuple = 1, 2, 3
        a, b, c = my_tuple
        print(a,b,c)

        def my_func():
            return 5, 1, 2
        a, b, c = my_func()
        print(a,b,c)

        my_tuple = (5, 7, 1, [1, 2, 3], 9, (1, 2), 'stringi')
        print(7 in my_tuple)
        print(7 not in my_tuple)

    case "9":
        os.system("cls")
        # list = []
        # tuple = ()
        # set = {}
        basket = {"apple", "orange", "apple", "pear", 123, "orange", "banana",}
        print(basket)

        a = "test"
        a = set(a)
        print(a)

        c = set([5, 7, 1, 2, 9, 1, 4])
        print(c)

        print(set("cba"))
        a = set([5,4,3,7,1])
        print(a)

        a.add(100)
        a.add(30)
        a.add(200)
        print(a)

        a.remove(200)
        print(a)

        a = set("abracadabra")
        b = set("alacazam")
        print(f"set a: {a}, set b: {b} ")
        print(a-b) # a-ში არის და b-ში არ არის
        print(b-a) # b-ში არის და a-ში არ არის
        print(a | b) # ყველა სიმბოლო
        print(a & b) # ორივეშია
        print(a ^ b) # 

    case "10":
        os.system("cls")
        # dictionary
        # key: value

        my_dict = {
            "giorgi": 19,  
            "nino":  25,
            "tamazi":  35,
            "elene":  45
        }

        print(my_dict["giorgi"])

        my_dict["ana"] = 28
        print(my_dict)

    case _:
        print("ERROR")
