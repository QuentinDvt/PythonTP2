#!/usr/bin/python3

CarbSource = ["Wheat & Rye (Bread)", "Maize (Meal)", "Potatoes"]
Extra = ["Beet Sugar", "Coffee", "Dark Chocolate"]
FatSource = ["Rapeseed Oil", "Olive Oil"]
Fruit = ["Bananas", "Apples", "Berries & Grapes"]
ProteinSource = ["Tofu", "Bovine Meat (beef herd)", "Poultry Meat", "Eggs"]
Vegetable = ["Tomatoes", "Root Vegetables", "Other Vegetables"]

def meals():
	repas = []
	meal = []
	for i in ProteinSource:
		meal.append(i)
		for j in CarbSource:
			meal.append(j)
			for k in FatSource:
				meal.append(k)
				for l in Vegetable:
					meal.append(l)
					for m in Fruit:
						meal.append(m)
						for n in Extra:
							meal.append(n)
							print(meal)
							repas.append(meal[:])
							del meal[-1]
						del meal[len(meal)-1:len(meal)]
					del meal[len(meal)-1:len(meal)]
				del meal[len(meal)-1:len(meal)]
			del meal[len(meal)-1:len(meal)]
		del meal[len(meal)-1:len(meal)]
	del meal[len(meal)-1:len(meal)]
	return repas


#repas = meals()
#print(['Eggs', 'Potatoes', 'Olive Oil', 'Other Vegetables', 'Berries & Grapes', 'Dark Chocolate'] in repas )

Calorie = {
	"Wheat & Rye (Bread)" : 2490,
	"Maize (Meal)" : 3630,
	"Potatoes" : 670,
	"Beet Sugar" : 3870,
	"Coffee" : 560,
	"Dark Chocolate" : 3930,
	"Rapeseed Oil" : 8096,
	"Olive Oil" : 8096,
	"Bananas" : 600,
	"Apples" : 480,
	'Berries & Grapes' : 530,
	"Tofu" : 765,
	"Bovine Meat (beef herd)" : 1500,
	"Poultry Meat" : 1220,
	"Eggs" : 1630,
	"Tomatoes" : 170,
	"Root Vegetables" : 380,
	"Other Vegetables" : 220,
}

gProteins = {
	"Wheat & Rye (Bread)" : 82,
	"Maize (Meal)" : 84,
	"Potatoes" : 16,
	"Beet Sugar" : 0,
	"Coffee" : 80,
	"Dark Chocolate" : 42,
	"Rapeseed Oil" : 0,
	"Olive Oil" : 0,
	"Bananas" : 7,
	"Apples" : 1,
	'Berries & Grapes' : 5,
	"Tofu" : 82,
	"Bovine Meat (beef herd)" : 185,
	"Poultry Meat" : 123,
	"Eggs" : 113,
	"Tomatoes" : 8,
	"Root Vegetables" : 9,
	"Other Vegetables" : 14,
}

gFat = {
	"Wheat & Rye (Bread)" : 12,
	"Maize (Meal)" : 12,
	"Potatoes" : 1,
	"Beet Sugar" : 0,
	"Coffee" : 0,
	"Dark Chocolate" : 357,
	"Rapeseed Oil" : 920,
	"Olive Oil" : 920,
	"Bananas" : 3,
	"Apples" : 3,
	'Berries & Grapes' : 4,
	"Tofu" : 42,
	"Bovine Meat (beef herd)" : 79,
	"Poultry Meat" : 77,
	"Eggs" : 121,
	"Tomatoes" : 2,
	"Root Vegetables" : 2,
	"Other Vegetables" : 2,
}

gCarb = {
	"Wheat & Rye (Bread)" : 514.1,
	"Maize (Meal)" : 797.1,
	"Potatoes" : 149.3,
	"Beet Sugar" : 967.5,
	"Coffee" : 60,
	"Dark Chocolate" : 155.1,
	"Rapeseed Oil" : 0,
	"Olive Oil" :0,
	"Bananas" : 136.4,
	"Apples" : 112.4,
	'Berries & Grapes' : 118.7,
	"Tofu" : 16.85,
	"Bovine Meat (beef herd)" : 16.2,
	"Poultry Meat" : 12.6,
	"Eggs" : 28.3,
	"Tomatoes" : 30.1,
	"Root Vegetables" : 81.6,
	"Other Vegetables" : 36.6,
}


def CRepas(qProt, ProteinSource, qCarb, CarbSource, qFat, FatSource, qVeg, Vegetable, qF, Fruit, qE, Extra):
	print("The meal is composed of :\n------------------------------------------------------------------------------")
	calorie = []
	gprot = []
	gfat = []
	gcarb = []
	Hash={
		ProteinSource : qProt,
		CarbSource : qCarb,
		FatSource : qFat,
		Vegetable : qVeg,
		Fruit : qF,
		Extra : qE,
	}
	for i in (ProteinSource, CarbSource, FatSource, Vegetable, Fruit, Extra):
		calorie.append(Hash[i]*10**(-3)*Calorie[i])
		gprot.append(Hash[i]*10**(-3)*gProteins[i])
		gfat.append(Hash[i]*10**(-3)*gFat[i])
		gcarb.append(Hash[i]*10**(-3)*gCarb[i])
		print(f" - {Hash[i]}\t {i}, contributing\t {Calorie[i]:.2f}kcal,\t{gProteins[i]:.2f}protein,\t{gCarb[i]:.2f}g carb,{gFat[i]:.2f}g fat")
	print("------------------------------------------------------------------------------")
	print(f"TOTAL : \t\t\t\t {sum(calorie):.2f}kcal, {sum(gprot):.2f}g protein, {sum(gcarb):.2f}g carb, {sum(gfat):.2f} g fat ")
CRepas(39, "Poultry Meat", 180, "Wheat & Rye (Bread)", 16, "Olive Oil", 125, "Root Vegetables", 50, "Berries & Grapes", 8, "Coffee")





