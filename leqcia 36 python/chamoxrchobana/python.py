import os
os.system('cls')
arr1 = ['ს','ა','ხ','ლ','ი']
arr1Len = len(arr1)
arr2 = [''] * arr1Len
sicocxle = 10

print("თამაში 'ჩამოხრჩობანა'")
print("ჩაწერეთ ასო")
while arr1 != arr2 and sicocxle > 0:
    #ჩაწერა შედარება მინიჭება სიცოცხლის დაკლება
    print(">>>>", end = " "); UserStr = input()
    os.system("cls")
    temp2 = False
    for i in range(0,arr1Len):
        if UserStr == arr1[i]:
            temp2 = True
            arr2[i] = UserStr

    #სიცოცხლეების ლოგიკა
    if temp2 == False:
        sicocxle = sicocxle - 1
    else:
        temp2 = True
    
    #მოგება წაგება
    if arr1 == arr2:
        os.system("color 2")
        os.system("cls")
        print("გილოცავთ თქვენ მოიგეთ")
    elif sicocxle == 0:
        os.system("cls")
        os.system("color 4")
        print("სამწუხაროდ თქვენ წააგეთ")

    print(f"სიცოცხლე = {sicocxle}")
    print(arr2)

