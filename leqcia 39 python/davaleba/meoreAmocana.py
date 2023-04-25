def main():
    import os
    os.system("cls")
    def kerdzis_damateba():
        os.system("cls")
        kerdzi = {}
        k, i = "",""
        End = "დასრულება"
        print("დასასრულებლად აკრიფეთ: 'დასრულება'")
        while k or i != End:
            k = input("დაამატეთ კერძი: ")
            if k == End:
                break
            i = input("ინგრედიენტი: ")            
            if i == End:
                break
            kerdzi[k] = ["ინგრედიენტი: ",i]
        
        # print("თქვენი დამატებული კერძია: ",kerdzi)
        os.system("cls")
        return kerdzi

    def standartuli_kerdzebi():
        Standartuli_kerdzebi = {
            "გამომცხვარი ბრიუსელის კომბოსტო": ["150   გრამი ბრიუსელის კომბოსტო","2   ს/კ ბალზამიკო","გემოვნებით მარილი","1   კბილი ნიორი","1   ს/კ ზეითუნის ზეთი", "გემოვნებით პილპილი"],
            "ფელამუში":["1   ლიტრი ბადაგი","40   გრამი პურის ფქვილი","ნიგოზი მოსართავად","160   გრამი სიმინდის ფქვილი","2   ს/კ შაქარი (საჭიროებისამებრ)"],
            "ჩაშუშული კომბოსტო":["2   ს/კ კარაქი","1   თავი დაჭრილი ხახვი","1⁄2  ჭიქა ბოსტნეულის ბულიონი","მარილი და პილპილი გემოვნებით","1   თავი კომბოსტო","12ს/კ ტომატი","ქინძი და ოხრახუში",]
        }
        return Standartuli_kerdzebi
    Standartuli_kerdzebi = standartuli_kerdzebi()
    
    print("დასასრულებლად აკრიფეთ: დასრულება")
    x = ""
    while x != "დასრულება":
        print(20*"-","რეცეპტები",20*"-")
        print("აირჩიეთ ვარიანტი:")
        print("""
    {1}  თუ შეიძლება დაამატეთ კერძის სახელი და ინგრედიენტი
    {2}  ყველა კერძის და ინგრედიენტის ნახვა
    {3}  კერძების მოჩებნა ინგრედიენტების მიხედვით
    {4}  პროგრამიდან გამოსვლა
        """)
        x = input(">>>>")
        match x:
            case "1":
                print("თქვენი დამატებული კერძია: ",kerdzis_damateba())
            case "2":
                os.system("cls")
                # damatebuli_kerdzi = kerdzis_damateba()
                print(Standartuli_kerdzebi)






main()