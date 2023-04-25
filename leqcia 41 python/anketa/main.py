import os
def Cls():
    os.system("cls")

Cls()
print("აირჩიეთ ვარიანტი:")
print("""
    {1} - ანკეტის შევსება
    {2} - ანკეტის ნახვა
""")

x = input(">>>>")
match x:
    case '1':
        Cls()
        print("შეიყვანეთ თქვენი სახელი და გვარი:")
        saxeli = input(">>>>")

        data = open("data.txt", "r", encoding="utf-8")
        new_data = data.read()
        split_new_data = new_data.split()
        for i in split_new_data:
            while saxeli == i:
                for i in split_new_data:
                    Cls()
                    saxeli = input("ასეთი სახელი უკვე არსებობს, შეიყვანეთ ახლიდან\n>>>>")
        data.close()

        data = open("data.txt", "a", encoding="utf-8")
        data.write(saxeli + "\n")
        data.close()

        file = open(saxeli+".txt", "a", encoding="utf-8")
        file.write("სახელი  -  " + saxeli + "\n")

        Cls()
        asaki = input("შეიყვანეთ ასაკი: \n>>>>")
        file.write("ასაკი  -  " + asaki + "\n")

        Cls()
        misamarti = input("შეიყვანეთ მისამართი: \n>>>>")
        file.write("მისამართი  -  " + misamarti + "\n")

        Cls()
        moqalaqeoba = input("რომელი ქვეყნის მოქალაქე ხართ? \n>>>>")
        file.write("მოქალაქეობა  -  " + moqalaqeoba + "\n")

        Cls()
        dabadebis_weli = input("დაბადების წელი: \n>>>>")
        file.write("დაბადების წელი  -  " + dabadebis_weli + "\n")

        Cls()
        dabadebis_tve = input("დაბადების თვე: \n>>>>")
        file.write("დაბადების თვე  -  " + dabadebis_tve + "\n")

        Cls()
        dabadebis_ricxvi = input("დაბადების რიცხვი: \n>>>>")
        file.write("დაბადების რიცხვი  -  " + dabadebis_ricxvi + "\n")

        Cls()
        ganatleba = input("განათლება: \n>>>>")
        file.write("განათლება  -  " + ganatleba + "\n")

        Cls()
        print("თქვენი ანკეტა შევსებულია \n გმადლობთ")


        file.close()

    case '2':
        Cls()
        saxeli = input("ვისი ანკეტის გახსნა გსურთ? \n>>>>")
        file = open(saxeli+".txt", "r", encoding="utf-8")
        Cls()
        print(file.read())