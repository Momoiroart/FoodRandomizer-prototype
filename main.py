import random as r
import json

def randomFood(category):
    if category == None:
        randomcat = r.choice(list(fooddb["category"].keys()))
        randommenu = r.choice(fooddb["category"][randomcat]["menus"])
        return randommenu
    else:
        randommenu = r.choice(fooddb["category"][category]["menus"])
        return randommenu

try:
    with open('food_database.json', 'r',encoding = 'utf-8') as file:
        fooddb = json.load(file)
    curcategory = None

    while True:    
        randommenu = randomFood(curcategory)
        print("\n [Recomend Menu!!!!]")
        print(f'Would you like to try: {randommenu}')
        ans = input("Or Would you like something else? (Y/N)").lower()
        if ans != 'y':
            print('Enjoy your meal XD')
            break
        specificat = input('Would you like specific food category? (Y/N)').lower()
        if specificat == 'y':
            print(f'Availible food category: {list(fooddb['category'].keys())}')
            choice = input('Which food categoty would you like?').lower()
            while choice not in list(fooddb['category'].keys()):
                print(f'Not a valid category\nAvailable food category: {list(fooddb['category'].keys())}')
                choice = input('Which food category would you like?: ')
            curcategory = choice
        else:
            curcategory = None






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
