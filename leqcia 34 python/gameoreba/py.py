import os
os.system('color 2')
os.system("cls")
print("აირჩიეთ ვარიანტი")
print("1) მაგალითი პირველი: ტიპები")
print("2) გაყოფა / დახრილი ხაზით, გაყოფა // დახრილი ხაზით")
print("3) რიცხვების ახარისხება num**2    num**3")
print("4) premda -ს მეთოდი")
print("5) ნაშთი %")
print("6) string")
print("7) Print 1+ line")
print("8) string *")
print("9) input")


print("cls")
print("ipconfig")
print("your Wifi password comand = Wifi")
print("Run Windows Camera comand = Camera")
print("Ping 8.8.8.8 Comand = Ping")
print(">>>>", end = " "); x = input()
match x:
    case '1':
        print("//////////////////////////////////////////")
        tipi = type(90)
        print(type(tipi))
    case '2':
        print("//////////////////////////////////////////")
        print(95/10)
        print(95//10)
    case '3':
        print("//////////////////////////////////////////")
        num = 5
        kvadrati = num**2
        kubi = num**3
        print(f"num = {num}")
        print(f"num ** 2 = {kvadrati}")
        print(f"num ** 3 = {kubi}")
    case '4':
        print("//////////////////////////////////////////")
        result = ((2+5**2)**3-2)/3.5 
        print(f"((2+5**2)**3-2)/3.5 = {result}")
        print(f"დამრგვალებული = ((2+5**2)**3-2)/3.5 = {int(result)}")
    case '5':
        print("//////////////////////////////////////////")
        print(f"95 % 10 = {95 % 10}")
    case '6':
        print("//////////////////////////////////////////")
        str1 = "hello'"
        print(str1)
        str2 = '"hello2"'
        print(str2)
        str3 = "\"hello\""
        print(str3)
    case '7':
        print("""
        line 1
        line 2
        line 3
        """)
        num1, num2 = [5,10]
        result = num1 + num2
        print(f"""
        num1 + num2 = {result} 
        """)
        print("hello" + "world")
    case '8':
        str1 = "hello"
        print(str1 * 10)
    case '9':
        # a = input()
        # print(a)
        arr = [10,20]
        arr2 = ["null","null"]
        arr2[1] =+ arr[1]
        arr2[0] =+ arr[0]
        print(arr2)


# Windows comands :D :D
    case 'cls':
        os.system('cls')
    case 'ipconfig':
        os.system('ipconfig')
    case 'Wifi':
        os.system('cls')
        os.system('netsh wlan show profile')
        print("აირჩიეთ თქვენი Wifi -ს სახელი:")
        WifiName = input()
        all_comand = "netsh wlan show profile name=\"" + WifiName +  "\" key=clear"
        os.system(all_comand)
    case 'Camera':
        os.system('start microsoft.windows.camera:')
    case 'Ping':
        os.system('color 2')
        os.system('ping 8.8.8.8 -t')
    case _:
        print("თქვენი ჩაწერილი ციფრი არ არსებობს")