spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    
    return [food["name"] for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
    pass


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        
        # Create the heat level string with emojis
        heat_emojis = "🌶" * heat_level
        
        # Format and print the output
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [food for food in spicy_foods if food["cuisine"] == cuisine]
    pass
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spiciest_foods(spicy_foods):
    # Get the list of spiciest foods
    spiciest_foods = get_spiciest_foods(spicy_foods)
    
    # Print each food in the required format
    for food in spiciest_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        
        # Create the heat level string with emojis
        heat_emojis = "🌶" * heat_level
        
        # Format and print the output
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")


    pass

def average_heat_level(spicy_foods):
    # Return 0 if the list of foods is empty
    if not spicy_foods:
        return 0
    
    # Calculate the sum of heat levels and the number of foods
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    number_of_foods = len(spicy_foods)
    
    # Calculate the average heat level and return it as an integer
    return total_heat // number_of_foods



def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
