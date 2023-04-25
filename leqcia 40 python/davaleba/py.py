# დაწერეთ პროგრამა „რეცეპტები“, რომელიც მომხმარებელს საშუალებას მისცემს, დაათვალიეროს, შეინახოს და მოძებნოს სხვადასხვა კერძების რეცეპტები. 

# პროგრამას უნდა ჰქონდეს მთავარი მენიუ, რომელიც მომხმარებელს საშუალებას მისცემს, აირჩიოს სასურველი მოქმედება.
# მოქმედება 1: დაამატოს კერძის სახელი და ინგრედიენტები. 
# მოქმედება 2: ნახოს ყველა კერძი და შესაბამისი ინგრედიენტები.
# მოქმედება 3: მოძებნოს კერძები ინგრედიენტის მიხედვით. (შეიყვანოს ინგრედიენტი და პროგრამამ დაუწეროს კერძები, რომლებსაც გააჩნიათ შეყვანილი ინგრედიენტი)
# მოქმედება 4: პროგრამიდან გამოსვლა.
# მითითებები: 
# გამოიყენეთ „dictionary” კერძების და ინგრედიენტების შესანახად;
# გამოიყენეთ ფუნქციები და განმარტეთ ისინი ცალკე ფაილში (მოდულში)
import os
Global_User_dict, Global_Standartuli_kerdzebi = {}, {}

def kerdzis_damateba():
    os.system("cls")
    user_dict = {}
    kerdzi, ingredienti = "",""
    while True:
        kerdzi = input("ჩაწერეთ კერძი: >>>> ")
        if kerdzi == "დასრულება":
            break
        ingredienti = input("ჩაწერეთ ინგრედიენტი: >>>> ")
        if ingredienti == "დასრულება":
            break
        user_dict[kerdzi] = ingredienti
    return user_dict

def standartuli_kerdzebi():
    Standartuli_kerdzebi = {
        "გამომცხვარი ბრიუსელის კომბოსტო": ["150   გრამი ბრიუსელის კომბოსტო","2   ს/კ ბალზამიკო","გემოვნებით მარილი","1   კბილი ნიორი","1   ს/კ ზეითუნის ზეთი", "გემოვნებით პილპილი"],
        "ფელამუში":["1   ლიტრი ბადაგი","40   გრამი პურის ფქვილი","ნიგოზი მოსართავად","160   გრამი სიმინდის ფქვილი","2   ს/კ შაქარი (საჭიროებისამებრ)"],
        "ჩაშუშული კომბოსტო":["2   ს/კ კარაქი","1   თავი დაჭრილი ხახვი","1⁄2  ჭიქა ბოსტნეულის ბულიონი","მარილი და პილპილი გემოვნებით","1   თავი კომბოსტო","12ს/კ ტომატი","ქინძი და ოხრახუში",]
    }
    return Standartuli_kerdzebi

def kerdzebi_da_ingredientebi():
    global Global_User_dict, Global_Standartuli_kerdzebi
    Global_Standartuli_kerdzebi = standartuli_kerdzebi()
    Global_User_dict = kerdzis_damateba()
    return Global_Standartuli_kerdzebi,Global_User_dict

os.system("cls")
while True:
    print("_"*10,"menu","_"*10)
    print("""
        აირჩიეთ ვარიანტი:
    1) კერძის და ინგრედიენტების დამატება.
    2) ყველა კერძის და ინგრედიენტის ნახვა.
    3) კერძის მოძებნა ინგრედიენტებით

       მენიუდან გამოსასვლელად აკრიფეთ: დასრულება
    """)

    x = input(">>>>")
    match x:
        case "1":
            Global_User_dict = kerdzis_damateba()
        case "2":
            os.system("cls")
            print(standartuli_kerdzebi())
            print(Global_User_dict)
        case "3":
            os.system("cls")
            Old_menu = standartuli_kerdzebi()
            User_menu = Global_User_dict
            ar_arsebobs = False
            ar_arsebobs2 = False
            user = input("ჩაწერეთ ინგრედიენტი: >>>> ")
            for key, value in Old_menu.items():
                if user in value:
                    print(key)
                else:
                    ar_arsebobs = True
            for key, value in User_menu.items():
                if user in value:
                    print(key)
                else:
                    ar_arsebobs2 = True
            if ar_arsebobs == True:
                print("თქვენი ჩაწერილი ინქგრედიენტი სტანდარტულ მენიუში არ არის")            
            if ar_arsebobs2 == True:
                print("თქვენი ჩაწერილი ინქგრედიენტი ახალ მენიუში არ არის")

        case "დასრულება":
            break