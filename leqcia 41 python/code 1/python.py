import os
os.system("cls")
def Cls():
    os.system("cls")

print("აირჩიეთ ვარიანტი:")
print("""
{1} ფაილში ჩაწერა, პირველი ვარიანტი
{2} ფაილში ჩაწერა მეორე ვარიანტი
{3} ფაილის წაკითხვა 
{4} ფაილის გახსნა აფენდის რეჟიმში
{5} აფდეითი +   -   r+ წაკითხვაც და შეცვლაც
{6} readline() ფუნქცია
{7} json
""")

x = input(">>>>")

match x:
    case '1':
        Cls()
        f = open('workfile.txt', 'w', encoding="utf-8")
        f.write("text")
        f.close()

    case '2':
        Cls()
        with open('workfile.txt', encoding="utf-8") as f:
            f.read()
            read_data = f.read()

    case '3':
       Cls()
       f = open('workfile.txt', 'r', encoding="utf-8")
       text = f.read()
       f.close()
       print(text)
    
    case '4':
        Cls()
        f = open('workfile.txt', 'a', encoding="utf-8")
        f.write("\ntext")
        f.close()

        f = open('workfile.txt', 'r', encoding="utf-8")
        text = f.read()
        f.close()
        print(text)

    case '5':
        Cls()
        f = open('workfile.txt', 'a+', encoding="utf-8")
        f.write("\n morre text2")
        text = f.read()
        f.close()
        # print(text)

    case '6':
        Cls()
        f = open("workfile.txt", 'r+', encoding="utf-8")
        # line_1 = f.readline()
        # line_2 = f.readline()
        lines_1 = f.readlines()
        # print(line_1)
        # print(line_2)
        print(lines_1)
        for line in lines_1:
            print(line)
        f.close()

    case '7':
        Cls()
        import json
        t = [1, 'simple', 'list']
        jsonformat =  json.dumps(t)

        f = open("workfile.json", "a+", encoding="utf-8")
        f.write(jsonformat + "\n")
        f.close()
        f = open("workfile.json", "r+", encoding="utf-8")
        print(f.read())
        f.close()

    case _:
        print("ERROR")