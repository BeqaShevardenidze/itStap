import os
os.system("cls")

def Cls():
    os.system("cls")

print("აირჩიეთ ვარიანტი:")
print("""
{1} - os მოდულში გამოყენებული ყველა ფუნქცია
{2} - os.listdir() მიმდინარე დირექტორიაში არსებული ფაილები და ფოლდერები
{3} - os.mkdir() დირექტორიის შექმნა (ფოლდერის)
{3.1}-os.path.exists 
{4} - os.rename() სახელის გადარქმევა
{5} - ფაილის path -ის გაგება
{6} - დირექტორიის წაშლა
{7} - os.system
{8} - os.walk ყველა დირექტორიის ნახვა
{9} - collection მოდული
{10}- defaultdict
""")
x = input(">>>>")
match x:
    case '1':
        Cls()
        print(dir(os))
    case '2':
        Cls()
        print(os.listdir())
    case '3':
        Cls()
        new_folder = "newFolder"
        if os.path.isdir(new_folder):
            print("საქაღალდე არსებობს")
        else:
            os.mkdir(new_folder)
            print("პაპკა შექმნილია")
        
        Path = input("""
        თუგინდათ რომ დაბეჭდოთ Path-ის ფუნქციები მაშინ აკრიფეთ "path" 
        თუ დასრულება გსურთ აკრიფეთ "end"
        >>>> """)
        if Path == "path":
            print(dir(os.path))
        elif Path == "end":
            print("ნახვამდის")
    case '3.1':
        Cls()
        def create_dir(name):
            if not (os.path.exists(name)):
                os.mkdir(name)
            
        print(os.listdir())
        create_dir("myname")
    case '4':
        Cls()
        oldFolder = "newFolder"
        newFolder = "newFolder_1"
        
        if os.path.isdir(oldFolder):
            os.rename(oldFolder, newFolder)
            print("სახელი შეიცვალა")
        elif os.path.isdir(newFolder):
            os.rename(newFolder, oldFolder)
            print("სახელი შეიცვალა")

    case '5':
        Cls()
        # v1
        with open ("newFolder\ტესტ.txt", "r", encoding="utf-8") as f:
            text = f.read()
            print(text)
            f.close()
        # v2
        with open (os.path.join("newFolder","ტესტ.txt"), "r", encoding="utf-8") as f:
            text = f.read()
            print(text)
            f.close()

    case '6':
        Cls()
        test= "test"
        os.mkdir(test)

        with open(os.path.join("test","text.txt"),"w",encoding="utf-8") as f:
            f.write("text")
            f.close()

        import time
        time.sleep(10)

        os.remove(os.path.join("test","text.txt"))

        time.sleep(10)

        os.rmdir("test")
            
    case '7':
        Cls()
        os.system("dir")

        # მიმდინარე სამუშაო დირექტორია
        print(10*"_")
        print(os.getcwd())

        # სამუშაო დირექტორიის შეცვლა
        os.chdir('code 1/newFolder')
        print(os.getcwd())

        text = """
print("mushaobs")
        """
        with open("py.py", "w", encoding="utf-8") as f:
            f.write(text)
            f.close()

    case '8':
        Cls()
        for root, dirs, files in os.walk('.'):
            print(root, dirs, files)

    case '9':
        Cls()
        from collections import Counter
        cnt = Counter("""
        {1} - os მოდულში გამოყენებული ყველა ფუნქცია
        {2} - os.listdir() მიმდინარე დირექტორიაში არსებული ფაილები და ფოლდერები
        {3} - os.mkdir() დირექტორიის შექმნა (ფოლდერის)
        {3.1}-os.path.exists 
        {4} - os.rename() სახელის გადარქმევა
        {5} - ფაილის path -ის გაგება
        {6} - დირექტორიის წაშლა
        {7} - os.system
        {8} - os.walk ყველა დირექტორიის ნახვა
        {9} - collection მოდული
        """)

        print(cnt)

    case '10':
        Cls()
        from collections import defaultdict

        # my_dict = defaultdict(int)
        # my_dict['1'] = 'one'
        # my_dict['2'].append('two')
        # print(my_dict)

        
