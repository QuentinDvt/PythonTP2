#!/usr/bin/python3

land_use_dict = {'Wheat & Rye (Bread)': 2.7,
    'Maize (Meal)': 1.8,
    'Potatoes': 0.8,
    'Beet Sugar': 1.5,
    'Tofu': 3.4,
    'Rapeseed Oil': 9.4,
    'Olive Oil': 17.3,
    'Tomatoes': 0.2,
    'Root Vegetables': 0.3,
    'Other Vegetables': 0.2,
    'Bananas': 1.4,
    'Apples': 0.5,
    'Berries & Grapes': 2.6,
    'Coffee': 11.9,
    'Dark Chocolate': 53.8,
    'Bovine Meat (beef herd)': 170.4,
    'Poultry Meat': 11.0,
    'Eggs': 5.7
  }

GHG_emissions_dict = {'Wheat & Rye (Bread)': 1.3,
    'Maize (Meal)': 1.2,
    'Potatoes': 0.5,
    'Beet Sugar': 1.8,
    'Tofu': 2.6,
    'Rapeseed Oil': 3.5,
    'Olive Oil': 5.1,
    'Tomatoes': 0.7,
    'Root Vegetables': 0.4,
    'Other Vegetables': 0.4,
    'Bananas': 0.8,
    'Apples': 0.4,
    'Berries & Grapes': 1.4,
    'Coffee': 8.2,
    'Dark Chocolate': 5.0,
    'Bovine Meat (beef herd)': 60.4,
    'Poultry Meat': 7.5,
    'Eggs': 4.2
  }

acidifying_emissions_dict = {'Wheat & Rye (Bread)': 13.3,
    'Maize (Meal)': 10.2,
    'Potatoes': 3.6,
    'Beet Sugar': 12.4,
    'Tofu': 6.0,
    'Rapeseed Oil': 23.2,
    'Olive Oil': 33.9,
    'Tomatoes': 5.2,
    'Root Vegetables': 2.9,
    'Other Vegetables': 3.7,
    'Bananas': 6.1,
    'Apples': 4.0,
    'Berries & Grapes': 6.9,
    'Coffee': 87.2,
    'Dark Chocolate': 29.0,
    'Bovine Meat (beef herd)': 270.9,
    'Poultry Meat': 64.7,
    'Eggs': 54.2
  }

eutrophying_emissions_dict = {'Wheat & Rye (Bread)': 5.4,
    'Maize (Meal)': 2.4,
    'Potatoes': 4.4,
    'Beet Sugar': 4.3,
    'Tofu': 6.6,
    'Rapeseed Oil': 16.4,
    'Olive Oil': 39.1,
    'Tomatoes': 1.9,
    'Root Vegetables': 1.0,
    'Other Vegetables': 1.8,
    'Bananas': 2.1,
    'Apples': 2.0,
    'Berries & Grapes': 1.0,
    'Coffee': 49.9,
    'Dark Chocolate': 67.3,
    'Bovine Meat (beef herd)': 320.7,
    'Poultry Meat': 34.5,
    'Eggs': 21.3
  }

water_use_dict = {'Wheat & Rye (Bread)': 12822,
    'Maize (Meal)': 350,
    'Potatoes': 78,
    'Beet Sugar': 115,
    'Tofu': 32,
    'Rapeseed Oil': 14,
    'Olive Oil': 24396,
    'Tomatoes': 4481,
    'Root Vegetables': 38,
    'Other Vegetables': 2940,
    'Bananas': 31,
    'Apples': 1025,
    'Berries & Grapes': 16245,
    'Coffee': 341,
    'Dark Chocolate': 220,
    'Bovine Meat (beef herd)': 441,
    'Poultry Meat': 334,
    'Eggs': 18621
  }


def impact(meal):
	land_use = 0
	gas_emissions = 0
	acidifying = 0
	eutrophying = 0
	water = 0
	for aliment, quantity in meal:
		land_use += land_use_dict[aliment]*10**(-3)*quantity
		gas_emissions += GHG_emissions_dict[aliment]*10**(-3)*quantity
		acidifying += acidifying_emissions_dict[aliment]*10**(-3)*quantity
		eutrophying += eutrophying_emissions_dict[aliment]*10**(-3)*quantity
		water += water_use_dict[aliment]*10**(-3)*quantity
	return land_use, gas_emissions, acidifying, eutrophying, water



meal = (("Poultry Meat", 39), ("Wheat & Rye (Bread)",180), ("Olive Oil",16), ("Root Vegetables", 125),("Berries & Grapes", 50), ("Coffee",8))
def affich(tuple):
	print("#########################")
	print("# Environmental impact #")
	print("#########################")
	print(f"This meal uses {tuple[0]:.2f} square meters of land.")
	print(f"This meal emits {tuple[1]:.2f} kg CO2 eq. (greenhouse gas emissions).")
	print(f"This meal emits {tuple[2]:.2f} g SO2 eq. (acidifying emissions).")
	print(f"This meal emits {tuple[3]:.2f} P043- eq. (eutrophying emissions).")
	print(f"This meal uses {tuple[4]:.2f} L of freshwater.")

affich(impact(meal))



