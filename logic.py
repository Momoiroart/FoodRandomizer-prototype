import random as r
import json

class FoodRecommender:
    def __init__(self, db_path = "food_database.json"):
        with open(db_path, 'r', encoding='utf-8') as file:
            self.fooddb = json.load(file)
        self.categories = list(self.fooddb["category"].keys())
        self.current_category = None

    def get_random_food(self,category = None):
        if category == None:
            randomcat = r.choice(self.categories)
            return r.choice(self.fooddb["category"][randomcat]["menues"])
        else:
            return r.choice(self.fooddb["category"][category]["menus"])
            
    def get_category(self):
        return self.categories

    def is_valid(self, category):
        return category in self.categories

