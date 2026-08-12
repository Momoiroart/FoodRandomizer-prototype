import random as r

food = {
    "japanese": [
        "Ramen",
        "Sushi",
        "Tonkatsu",
        "Curry"
    ],
    "thai": [
        "Pad Thai",
        "Som Tum",
        "Krapow",
        "Suki/Shabu"
    ],
    "western": [
        "Pizza",
        "Spaghetti",
        "Burger",
        "Steak"
    ]
}

print(f"Available categories: {list(food.keys())}")
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
        print("Invalid category! Please try again.\n")




