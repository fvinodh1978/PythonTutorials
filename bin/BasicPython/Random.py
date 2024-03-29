import random
import time
from msvcrt import getch


def lucky_draw(min_num, max_num):
    coupons = []
    selected_num = random.randint(min_num, max_num)
    while len(coupons) < max_num - min_num + 1:
        if selected_num in coupons:
            pass
        else:
            coupons.append(selected_num)
            print("Lucky Winner is : ", selected_num)
            print("Press Enter Button to Pick the Next Number : ")
            getch()
        selected_num = random.randint(min_num, max_num)
    return coupons


min_num = int(input("Enter the starting Number : "))
max_num = int(input("Enter the Ending Number : "))
lucky_coupons = lucky_draw(min_num, max_num)
print(lucky_coupons)
