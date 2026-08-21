import random as r
import json

class FoodRecommender:
    def __init__(self, db_path = "food_database.json"):
        with open(db_path, 'r', encoding='utf-8') as file:
            self.fooddb = json.load(file)
        self.categories = list(self.fooddb["category"].keys())
        self.current_category = None
    
    def get_random_food(self, category=None):
        """คืนค่า dict {"name": ..., "image": ...} ของเมนูที่สุ่มได้"""
        if category is None or category == "All Category":
            randomcat = r.choice(self.categories)
            return r.choice(self.fooddb["category"][randomcat]["menus"])
        else:
            # รองรับทั้งชื่อ lowercase และ capitalize
            cat_key = category.lower()
            return r.choice(self.fooddb["category"][cat_key]["menus"])
            
    def get_category(self):
        return self.categories

    def is_valid(self, category):
        return category in self.categories

