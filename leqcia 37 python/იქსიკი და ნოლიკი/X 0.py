import os
os.system("cls")

print("აირჩიეთ ვარიანტი")
print("[1] პირველი ვარიანტი (სტანდარტული)")
print("[2] მეორე ვარიანტი (ფუნქციებში) (ჯერ არ მუშაობს)")
print(">>>>", end = " "); x = int(input())

match x:
    case 1:
        os.system("cls")
        arr1 = ['|-|'] * 10
        #ციფრების დაფა
        for i in range(1,10):
            if i == 3 or i == 6:
                print("|", i, "|", end = " ")
                print("\n")
            elif i==9:
                print("|", i, "|",)
                print("\n")
            else:
                print("|", i, "|", end = " ")

        #ცარიელი დაფა
        for i in range(1,10):
            if i == 3 or i == 6:
                print(arr1[i], end = " ")
                print("\n")
            elif i==9:
                print(arr1[i])
                print("\n")
            else:
                print(arr1[i], end = " ")

        start = True


        while start == True:
            # ////////////////////////////// პირველი მოთამაშე /////////////////////////////
            empty = False
            # პირველი მოთამაშის ლოგიკა: ცარიელი არის თუ არა ადგილი
            while empty == False:
                print(">>>>", end = " "); User1 = int(input())
                if(arr1[User1] == "|X|"):
                    os.system("cls")
                    #ციფრების დაფა
                    for i in range(1,10):
                        if i == 3 or i == 6:
                            print("|", i, "|", end = " ")
                            print("\n")
                        elif i==9:
                            print("|", i, "|",)
                            print("\n")
                        else:
                            print("|", i, "|", end = " ")
                    # ბეჭდავს დაფას
                    for i in range(1,10):
                        if i == 3 or i == 6:
                            print(arr1[i], end = " ")
                            print("\n")
                        elif i==9:
                            print(arr1[i])
                            print("\n")
                        else:
                            print(arr1[i], end = " ")
                    print("ადგილი დაკავებულია: \n სცადეთ ხელ-ახლა:")
                    empty = False
                elif (arr1[User1] == "|0|"):
                    os.system("cls")
                    #ციფრების დაფა
                    for i in range(1,10):
                        if i == 3 or i == 6:
                            print("|", i, "|", end = " ")
                            print("\n")
                        elif i==9:
                            print("|", i, "|",)
                            print("\n")
                        else:
                            print("|", i, "|", end = " ")
                    # ბეჭდავს დაფას
                    for i in range(1,10):
                        if i == 3 or i == 6:
                            print(arr1[i], end = " ")
                            print("\n")
                        elif i==9:
                            print(arr1[i])
                            print("\n")
                        else:
                            print(arr1[i], end = " ")
                    print("ადგილი დაკავებულია: \n სცადეთ ხელ-ახლა:")
                    empty = False
                else:
                    os.system("cls")
                    empty = True

            # os.system("cls")
            #ციფრების დაფა
            for i in range(1,10):
                if i == 3 or i == 6:
                    print("|", i, "|", end = " ")
                    print("\n")
                elif i==9:
                    print("|", i, "|",)
                    print("\n")
                else:
                    print("|", i, "|", end = " ")
            User1Temp = "|X|"
            for i in range(1,10):
                arr1[User1] = User1Temp
                if i == 3 or i == 6:
                    print(arr1[i], end = " ")
                    print("\n")
                elif i==9:
                    print(arr1[i])
                    print("\n")
                else:
                    print(arr1[i], end = " ")

            # //////////////////////////// მოგების გადამოწმება /////////////////////////////
            # ჰორიზონტალურად
            if arr1[1] ==  "|X|" and arr1[2] ==  "|X|" and arr1[3] ==  "|X|":
                print("გილოცავთ იქსიკმა მოიგო")
                start = False
            elif arr1[4] ==  "|X|" and arr1[5] ==  "|X|" and arr1[6] ==  "|X|":
                print("გილოცავთ იქსიკმა მოიგო")
                start = False
            elif arr1[7] ==  "|X|" and arr1[8] ==  "|X|" and arr1[9] ==  "|X|":
                print("გილოცავთ იქსიკმა მოიგო")
                start = False
            # დიაგონალი
            elif arr1[1] ==  "|X|" and arr1[5] ==  "|X|" and arr1[9] ==  "|X|":
                print("გილოცავთ იქსიკმა მოიგო")
                start = False
            elif arr1[3] ==  "|X|" and arr1[5] ==  "|X|" and arr1[7] ==  "|X|":
                print("გილოცავთ იქსიკმა მოიგო")
                start = False
            # ვერტიკალური
            elif arr1[1] ==  "|X|" and arr1[4] ==  "|X|" and arr1[7] ==  "|X|":
                print("გილოცავთ იქსიკმა მოიგო")
                start = False
            elif arr1[2] ==  "|X|" and arr1[5] ==  "|X|" and arr1[8] ==  "|X|":
                print("გილოცავთ იქსიკმა მოიგო")
                start = False
            elif arr1[3] ==  "|X|" and arr1[6] ==  "|X|" and arr1[9] ==  "|X|":
                print("გილოცავთ იქსიკმა მოიგო")
                start = False


            # //////////////////////////////////// მეორე მოთამაშე ////////////////////////////////
            empty = False

            # მეორე მოთამაშის ლოგიკა: ცარიელი არის თუ არა ადგილი
            while empty == False:
                print(">>>>", end = " "); User2 = int(input())
                if(arr1[User2] == "|X|"):
                    os.system("cls")
                    #ციფრების დაფა
                    for i in range(1,10):
                        if i == 3 or i == 6:
                            print("|", i, "|", end = " ")
                            print("\n")
                        elif i==9:
                            print("|", i, "|",)
                            print("\n")
                        else:
                            print("|", i, "|", end = " ")
                    # ბეჭდავს დაფას
                    for i in range(1,10):
                        if i == 3 or i == 6:
                            print(arr1[i], end = " ")
                            print("\n")
                        elif i==9:
                            print(arr1[i])
                            print("\n")
                        else:
                            print(arr1[i], end = " ")
                    print("ადგილი დაკავებულია: \n სცადეთ ხელ-ახლა:")
                    empty = False
                elif (arr1[User2] == "|0|"):
                    os.system("cls")
                    #ციფრების დაფა
                    for i in range(1,10):
                        if i == 3 or i == 6:
                            print("|", i, "|", end = " ")
                            print("\n")
                        elif i==9:
                            print("|", i, "|",)
                            print("\n")
                        else:
                            print("|", i, "|", end = " ")
                    # ბეჭდავს დაფას
                    for i in range(1,10):
                        if i == 3 or i == 6:
                            print(arr1[i], end = " ")
                            print("\n")
                        elif i==9:
                            print(arr1[i])
                            print("\n")
                        else:
                            print(arr1[i], end = " ")
                    print("ადგილი დაკავებულია: \n სცადეთ ხელ-ახლა:")
                    empty = False
                else:
                    os.system("cls")
                    empty = True


            #ციფრების დაფა
            for i in range(1,10):
                if i == 3 or i == 6:
                    print("|", i, "|", end = " ")
                    print("\n")
                elif i==9:
                    print("|", i, "|",)
                    print("\n")
                else:
                    print("|", i, "|", end = " ")
            User2Temp = "|0|"
            for i in range(1,10):
                arr1[User2] = User2Temp
                if i == 3 or i == 6:
                    print(arr1[i], end = " ")
                    print("\n")
                elif i==9:
                    print(arr1[i])
                    print("\n")
                else:
                    print(arr1[i], end = " ")

            # //////////////////////////// მოგების გადამოწმება /////////////////////////////
            # ჰორიზონტალურად
            if arr1[1] ==  "|0|" and arr1[2] ==  "|0|" and arr1[3] ==  "|0|":
                print("გილოცავთ ნოლიკმა მოიგო")
                start = False
            elif arr1[4] ==  "|0|" and arr1[5] ==  "|0|" and arr1[6] ==  "|0|":
                print("გილოცავთ ნოლიკმა მოიგო")
                start = False
            elif arr1[7] ==  "|0|" and arr1[8] ==  "|0|" and arr1[9] ==  "|0|":
                print("გილოცავთ ნოლიკმა მოიგო")
                start = False
            # დიაგონალი
            elif arr1[1] ==  "|0|" and arr1[5] ==  "|0|" and arr1[9] ==  "|0|":
                print("გილოცავთ ნოლიკმა მოიგო")
                start = False
            elif arr1[3] ==  "|0|" and arr1[5] ==  "|0|" and arr1[7] ==  "|0|":
                print("გილოცავთ ნოლიკმა მოიგო")
                start = False
            # ვერტიკალური
            elif arr1[1] ==  "|0|" and arr1[4] ==  "|0|" and arr1[7] ==  "|0|":
                print("გილოცავთ ნოლიკმა მოიგო")
                start = False
            elif arr1[2] ==  "|0|" and arr1[5] ==  "|0|" and arr1[8] ==  "|0|":
                print("გილოცავთ ნოლიკმა მოიგო")
                start = False
            elif arr1[3] ==  "|0|" and arr1[6] ==  "|0|" and arr1[9] ==  "|0|":
                print("გილოცავთ ნოლიკმა მოიგო")
                start = False
# ////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////-end-//////////////////////////////////////////////////////////
    case 2:
        os.system("cls")
        arr1 = ['|-|'] * 10

        #ციფრების დაფა
        def cifrebis_dafa():
            for i in range(1,10):
                if i == 3 or i == 6:
                    print("|", i, "|", end = " ")
                    print("\n")
                elif i==9:
                    print("|", i, "|",)
                    print("\n")
                else:
                    print("|", i, "|", end = " ")
            cifrebis_dafa()
        cifrebis_dafa()

        # def test():
        #     size = 11
        #     arr = [''] * size
        #     for i in range(1, size):
        #         arr[i] = i
        #     return arr
        #     # print(arr)
        
        # test1 = test()
        # print(test1)


        # #ცარიელი დაფა
        # def carieli_dafa():
        #     for i in range(1,10):
        #         if i == 3 or i == 6:
        #             pirveli_xazi = arr1[i]
        #             # print(pirveli_xazi, "\n")
        #         elif i==9:
        #             print(arr1[i])
        #             print("\n")
        #         else:
        #             print(arr1[i], end = " ")
        # carieli_dafa()

    