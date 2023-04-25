import os
import time

def Cls():
    os.system("cls")

Cls()
print("""
{1} 1970 წლის პირველი იანვრიდან გასული წამების რაოდენობა
{2} რამდენი წამში სრულდება პროგრამა
{3} date time მოდული
{4} ახლანდელი დრო
{5} თარიღის და დროის გაერთიანება (combine)
""")

x = input(">>>>")
match x:
    case '1':
        Cls()
        while True:
            print("1970 წლის პირველი იანვრიდან გასული წამების რაოდენობა: ",time.time())
    case '2':
        Cls()
        start = time.time()
        count = 0
        for i in range(10000):
            count += 1
        end = time.time()
        print(f"start = {start},  end = {end}")
        result = end - start
        print("პროგრამის შესრულების ხანგძლივობა = ", result)
        print(count)
    case '3':
        Cls()
        from datetime import date, time, datetime
        today = date.today()
        print("ერთად: ",today)
        print(today.year)
        print(today.month)
        print(today.day)
    case '4':
        Cls()
        from datetime import date, time, datetime
        now = datetime.now()
        print(now)
        print(now.year)
        print(now.month)
        print(now.day)
        print(now.hour)
        print(now.minute)
        print(now.second)

        current_time = time(now.hour, now.minute, now.second)
        print(current_time)
    case '5':
        Cls()
        from datetime import date, time, datetime
        today = date.today()
        now = datetime.now()
        current_time = time(now.hour, now.minute, now.second)

        carrent_date = datetime.combine(today,current_time)
        print(carrent_date)