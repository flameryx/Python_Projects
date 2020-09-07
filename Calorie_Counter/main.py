def fats_to_calories(fats):
    return fats * 9

def carbs_to_calories(carbs):
    return carbs * 4

def prots_to_calories(prots):
    return prots * 4


class Food():
    portion_size = "100g"

    def __init__(self, food_type, full_name, fats, carbs, prots):
        self.food_type = food_type
        self.full_name = full_name
        self.fats = fats
        self.carbs = carbs
        self.prots = prots

    def get_fats(self):
        return self.fats

    def get_carbs(self):
        return self.carbs

    def get_prots(self):
        return self.prots



bacon = Food("BACON", "Ja! Delikatess Bacon mild geräuchert", 29.0, 0.2, 15.0)
boiled_eggs = Food("BOILED EGGS", "Internet: Healthline Nutrition Facts", 10.6, 1.2, 12.6)
scrambled_eggs = Food("SCRAMBLED EGGS", "Internet: Fitbit Nutrition Facts", 11.0, 1.6, 10.0)
ja_butter_toast = Food("BREAD", "Ja! Butter-Toastbrot", 3.7, 48.0, 8.5)
spaghetti = Food("SPAGHETTI", "Ja! Spaghetti", 1.9, 72.0, 12.0)
haferflocken = Food("HAFERFLOCKEN", "Ja! Zarte Haferflocken", 7.0, 58.7, 13.5)
chiquita_banana = Food("BANANA", "Chiquita Bananas", 0.0, 23.8, 0.8)
nutella = Food("NUTELLA", "Nutella Ferrero", 30.9, 57.5, 6.3)
peanut_butter = Food("PEANUT BUTTER", "Jeff's Peanut Butter Creamy", 50.0, 15.0, 25.0)
milk = Food("MILK", "Ja! Frische Vollmilch", 3.6, 4.8, 3.3)
mash_potatoes = Food("MASH POTATOES", "Maggi Kartoffel Püree, Das Lockere", 0.9, 75.0, 7.5)
tuna = Food("TUNA", "Ja! Thunfischfilets in eigenem Saft", 1.1, 0.1, 25.3)


food_objs = [bacon, boiled_eggs, scrambled_eggs, ja_butter_toast, spaghetti, haferflocken, chiquita_banana,
             nutella, peanut_butter, milk, mash_potatoes, tuna]

total_fats = 0
total_carbs = 0
total_prots = 0
total_calories = 0

meals = ["BREAKFAST", "LUNCH", "DINNER", "SNACK"]
meal = ""


while meal not in ["1", "2", "3", "4"] :
    meal = input("Enter number of meal:\n1) Breakfast\n2) Lunch\n3) Dinner\n4) Snack\n")

    if meal not in ["1", "2", "3", "4"]:
        print("Not an option. Try again\n\n")

meal_index = int(meal) - 1


while True:

    food = input("Enter food: ")
    food = food.upper()

    if food == "" or food == "EXIT" or food == "NONE":
        break

    for obj in food_objs:

        if obj.food_type == food:
            amount = input("Enter amount (grams): ")
            print()
            amount = int(amount)

            amount_multiplier = amount/100

            obj_fats = obj.get_fats() * amount_multiplier
            obj_carbs = obj.get_carbs() * amount_multiplier
            obj_prots = obj.get_prots() * amount_multiplier
            obj_calories = fats_to_calories(obj_fats) + carbs_to_calories(obj_carbs) + prots_to_calories(obj_prots)

            total_fats += obj_fats
            total_carbs += obj_carbs
            total_prots += obj_prots
            total_calories += obj_calories

            obj_fats = round(obj_fats, 1)
            obj_carbs = round(obj_carbs, 1)
            obj_prots = round (obj_prots, 1)
            obj_calories = int(round(obj_calories, 0))

            print("Fats: " + str(obj_fats) + " grams")
            print("Carbs: " + str(obj_carbs) + " grams")
            print("Prots: " + str(obj_prots) + " grams")
            print("CALORIES: " + str(obj_calories) + "\n")



total_fats = round(total_fats, 1)
total_carbs = round(total_carbs, 1)
total_prots = round(total_prots, 1)
total_calories = int(round(total_calories, 0))

print()
print(meals[meal_index] + " FINISHED")
print("Total Fats: " + str(total_fats) + " grams")
print("Total Carbs: " + str(total_carbs) + " grams")
print("Total Prots: " + str(total_prots) + " grams")
print("TOTAL CALORIES: " + str(total_calories) + "\n")



