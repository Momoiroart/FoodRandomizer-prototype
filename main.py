import random as r
import json

try:
    with open('food_database.json', 'r',encoding = 'utf-8') as file:
        fooddb = json.load(file)
    while True:
        randomcat = r.choice(list(fooddb["category"].keys()))
        randommenu = r.choice(fooddb["category"][randomcat]["menus"])

        print("\n [Recomend Menu!!!!]")
        print(f'Would you like to try: {randommenu}')
        ans = input("Or Would you like something else? (Y/N)").lower()
        if ans == 'y':
            specificcat = input('Would you like any specific Category?(Y/N)').lower()            
            if specificcat == 'y':
                print(f"Available categories: {list(fooddb["category"].keys())}")
                choice = input("What do you want to eat? (japanese/thai/western): ").lower()
                randommenu = r.choice(fooddb["category"][choice]["menus"])
                print("\n [Recomend Menu!!!!]")
                print(f'Would you like to try: {randommenu}')
                ans = input("Or Would you like something else? (Y/N)").lower()
            else:
                randomcat = r.choice(list(fooddb["category"].keys()))
                randommenu = r.choice(fooddb["category"][randomcat]["menus"])
                print("\n [Recomend Menu!!!!]")
                print(f'Would you like to try: {randommenu}')
                ans = input("Or Would you like something else? (Y/N)").lower()
        else:
            print('Enjoy your meal XD')
            break



except FileNotFoundError:
    print("Error: หาไฟล์ 'food_database.json' ไม่เจอครับ กรุณาตรวจสอบไฟล์อีกครั้ง")



'''print(f"Available categories: {list(food.keys())}")
choice = input("What do you want to eat? (japanese/thai/western): ").lower()

while True:
    print(f"Available categories: {list(food.keys())}")
    choice = input("What do you want to eat? (japanese/thai/western): ").lower()

    try:
        # พยายามดึง list อาหารจาก Dictionary ทันที
        random_food = r.choice(food[choice])
        print(f"Recommend {choice.capitalize()} Food is: {random_food}.")
        
        ans = input('Wanna continue? (yes/no): ').lower()
        if ans != 'yes':
            print("Arigatou gozaimasu! ขอให้อร่อยกับมื้ออาหารนะ!")
            break

    except KeyError:
        # ถ้าไม่มี key ที่พิมพ์มาใน Dictionary จะตกมาทำงานที่บล็อกนี้
        print("Invalid category! Please try again.\n")'''
