import os
from datetime import date, time, datetime 
def Cls():
    os.system("cls")
def f_davaleba_1():
    Cls()
    user_month = int(input("ჩაწერეთ დაბადების თვე >>>> "))
    Cls()
    user_day = int(input("ჩაწერეთ დაბადების დღე >>>> "))

    Cls()

    today = datetime.now()
    today_month = today.month
    today_day = today.day

    if user_month > today_month:
        remaining_month = user_month - today_month
    elif user_month < today_month:
        remaining_month = today_month - user_month
    else:
        remaining_month = 0

    if user_day > today_day:
        remaining_day = user_day - today_day
    elif user_day < today_day:
        remaining_day = today_day - user_day
    else:
        remaining_day = 0

    print(f"თქვენს დაბადების დღემდე დარჩენილია {remaining_month} თვე და {remaining_day} დღე")




if __name__ == "__main__":
    f_davaleba_1()