import os
def Cls():
    os.system("cls")
Cls()


print("""
{1} - დავალება 1
        1.	დააიმპორტეთ os მოდული; +
        2.	შექმენით ახალი ფოლდერი სახელად „PracticeFolder”; +
        3.	შეცვალეთ მიმდინარე სამუშაო დირექტორია ისე, რომ აღმოჩნდეთ თქვენს მიერ შექმნილ ფოლდერში; +
        4.	For ციკლით შექმენით სამი ფაილი: “file1.txt”, “file2.txt”, “file3.txt”
        5.	os.listdir ფუნქციის გამოყენებით ჩამოთვალეთ შექმნილი ფაილები.

{2} - დავალება 2
        1.	დააიმპორტეთ collections მოდული;
        2.	განმარტეთ string ტიპის ცვლადი და შეინახეთ მასში ტექსტი, რომელიც რამდენიმე ხაზისგან შედგება.
        3.	გადაიყვანეთ ტექსტი პატარა ასოებში და დაყავით სიტყვებად (გამოიყენეთ .lower და .split მეთოდები)
        4.	დაითვალეთ თითოეული სიტყვის რაოდენობა Counter-ის გამოყენებით.
        5.	დაბეჭდეთ სიტყვები და მათი რაოდენობები.


""")

x = input(">>>> ")
match x:
    case '1':
        Cls()
        folder_1 = "PracticeFolder"
        if os.path.isdir(folder_1):
            print("ასეთი ფოლდერი უკვე არსებობს")
        else:
            os.mkdir(folder_1)
            print("ფოლდერი უკვე შეიქმნა")

        os.chdir("PracticeFolder")

        for i in range(1, 4):
            fileName = "text" + str(i) + ".txt"
            with open(fileName, "w", encoding="utf-8") as f:
                f.write("text" + str(i))

            f.close()

        print(os.listdir())

    case '2':
        Cls()
        from collections import Counter
        string = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

        print("სტანდარტული სტრინგი: ", string)
        
        print("_"*20,'\n')
        lower_string = string.lower()
        print("სტრინგი პატარა ასოებად: ", lower_string)
        
        print("_"*20,'\n')
        split_string = string.split()
        print("სტრინგი დაყოფილი სიტყვებად: ",split_string)

        print("_"*20,'\n')
        word_num = Counter(split_string)
        print("სიტყვების რაოდენობა სტრინგში: ", word_num)