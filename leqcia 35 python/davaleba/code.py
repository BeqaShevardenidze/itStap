import os
import random
os.system("color 2"); os.system("cls")
print("აირჩიეთ ვარიანტი")
print("1) მომხმარებლის პაროლი")
print("2) Rand ციფრის გამოცნობა")
print("3) For ციკლი")
print(">>>>", end = ' '); x = int(input())
match x:
    case 1:
        os.system("cls")
        print("""
1. მომხმარებელს მოთხოვეთ პაროლის შეყვანა. თუ შეყვანილი პაროლი არის “123”, უთხარით რომ პაროლი სწორად შეიყვანა. სხვა შემთხვევაში უთხარით, რომ პაროლი არასწორად შეიყვანა.
        """) 
        cda = 3; 
        print("თუ შეიძლება შეიყვანეთ პაროლი >>>>", end = " "); password = input(); 
        if password == "123":
            os.system("cls")
            print("თქვენი პაროლი სწორია: მობრძანდით!!!!")
        else:
            while password != "123" and cda > 0:
                if password == "123":
                    os.system("cls")
                    print("თქვენი პაროლი სწორია.  მობრძანდით!!!!")
                else:
                    os.system("cls")
                    cda = cda - 1
                    print(f"დაგრჩათ {cda} მცდელობა")
                    print("თქვენი პაროლი არ არის სწორი")
                    print("ჩაწერეთ ხელახლა  >>>>", end = " "); password = input()
                    if password == "123":
                        os.system("cls")
                        print("თქვენი პაროლი სწორია.  მობრძანდით!!!!")        
                    elif cda == 0:
                        os.system("cls")
                        print("თქვენი იუზერი დაიბლოკა")

    case 2:
        os.system("cls")
        print("""
2. შექმენით ცვლადი და მასში შეინახეთ 1-დან 10-მდე რომელიმე რიცხვი. While ციკლის გამოყენებით მომხმარებელს მოთხოვეთ, გამოიცნოს შეყვანილი რიცხვი მანამ, სანამ არ გამოიცნობს. გამოცნობის შემთხვევაში ცილკლიდან გამოდით break-ის გამოყენებით.
        """)
        RandNum = random.randint(0, 10)
        print(RandNum)
        UserNum1 = -1
        while True:
            print("ჩაწერეთ რიცხვი 1-დან 10ის ჩათვლით >>>>", end = " "); UserNum1 = int(input())
            os.system("cls")
            if RandNum != UserNum1:
                print("""თქვენ ვერ გამოიცანით: 
                ცადეთ ხელახლა:  >>>>""", end = " "); UserNum1 = int(input())
            if RandNum == UserNum1:
                os.system("cls")
                print("თქვენ გამოიცანით")
                break
            
    
    case 3:
        os.system("cls")
        print("""
3. For ციკლის გამოყენებით დაბეჭდეთ 1-დან 10-მდე შუალედში ყველა ლუწი რიცხვი. 
        """)
        for x in range(10):
            if x % 2 == 0:
                print(x)
    case _:
        print("თქვენი ჩაწერილი რიცხვი არ არსებობს")