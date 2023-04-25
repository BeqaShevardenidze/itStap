import os
import time
import random
def Cls():
    os.system("cls")

def f_davaleba_2():
    Cls()
    now = time.time()
    input("დააჭირეთ enter -ს >>>> ")
    future = time.time()
    result = future - now
    print(f"პროგრამის მუსაობსი ხანგრძლივობაა {int(result)} წამი")

    Randint = random.randint(2,7)
    
    if Randint > result:
        print("თქვენ ადრე დააჭირეთ")
    elif Randint < result:
        print("თქვენ დააგვიანეთ")
    elif Randint == result:
        print("გილოცავთ თქვენ დროულად დააჭირეთ")

if __name__ == "__main__":
    f_davaleba_2()