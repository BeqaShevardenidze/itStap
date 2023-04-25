import os
os.system("cls")

print("""
1) ფუნქციის დეფაულთ არგუმენტი
2) ფუნქციის ბევრი არგუმენტი *
3) lambda ანონიმური ფუნქცია
4) test
""")

print(">>>>", end = " "); x = int(input())
match x:
    case 1:
        os.system("cls")
        def ask_ok(prompt, retries=4, reminder='Please try again!'):
            while True:
                ok = input(prompt)
                if ok in ('y','ye','yes'):
                    return True
                if ok in ('n','no','nop','nope'):
                    return False
                retries = retries - 1
                if retries < 0:
                    break
                print(reminder)
        # ask_ok("n")
    case 2:
        os.system("cls")
        def func(*parametrs):
            print(parametrs)
        func(10,20,30,40)

    case 3:
        def rectangle_area(a,b):
            return a * b
        print(rectangle_area(5,10))

        # lambda
        print(
            (lambda a, b: a * b)(10,5)
        )
    case 4:
        print("test")


    case _:
        print("ERROR")