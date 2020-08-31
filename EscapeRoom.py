# Menu Options : Examine, Collect, Use, Return to previous, Return to main

# Inventory : Check inventory, Items collected need to end up in inventory
# def Collect option --> Inventory

# Input : Selecting options from each screen


# First in-game text
print("You're awake! I just came to about 15 minutes ago. My name is Annie.\n")
print("I tried that door but it's locked, not to mention, there's three separate locks holding it shut.\n")
print("You must be as scared as I am, but we'll figure this out together.\n")
print("Let's start by looking around and see where we might be.")

# Defining places and objects ------- how to convert to a dictionary ??

def coffee():
	print("You check the coffee table.")
	print("There are some mazagines, a coffee mug, and a coaster near the edge.")
def plant():
	print("This plant has seen better days...looks like it's been neglected for weeks. Look, it's leaves are all curled and wrinkled up. Not that water will save it now.")
def desk():
	print("What a mess..where should I start looking?")
def magazines():
	print("Magazine editions are from last week.")
def coffeeMug():
	print("There's still some coffee left")
def coaster():
	print("Just a coaster")
def dirt():
	print("The dirt's all dried up. You feel no resistance as you push your fingers through, until you hit something solid.\n")
	print("You found a small brown key!")
def leaves():
	print("You start to unfold some of the leaves and notice some dark brown spots on some of the leaves.\n")
	print("You scratch at the spots and it crumbles off.")
def files():
	print("--insert something interesting--")
def drawers():
	print("It's locked...")
def coffeeMug2():
	print("There's still some coffee left")



def main_menu():
	print("Where would you like to examine?")
	print("--------------------")

# Dictionary for main menu options
printMenu = {"Q": { "function": coffee, "text": "The coffee table"}, 
"W": { "function": plant, "text": "The pitcher plant"}, 
"E": { "function": desk, "text": "The computer desk"}
} 
# Dictionary for coffee
coffee_ = {"1": { "function": magazines, "text": "Magazines"},
"2": { "function": coffeeMug, "text": "Coffee mug"},
"3": { "function": coaster, "text": "Coaster"},
"9": { "function": main_menu, "text": "Back to room"}
}
# Dictionary for pitcher plant
plant_ = {"1": { "function": dirt, "text": "Dirt"},
"2": { "function": leaves, "text": "Leaves"},
"9": { "function": main_menu, "text": "Back to room"}
} 
	
# Dictionary for computer desk
desk_ = {"1": { "function": files, "text": "Scattered files"},
"2": { "function": drawers, "text": "Drawers"},
"3": { "function": coffeeMug2, "text": "Coffee mug"},
"9": { "function": main_menu, "text": "Back to room"}	
}


	
print(main_menu())

for key in printMenu:
	print(key + ":\t" + printMenu[key]["text"])


check = input("Let's check: ").upper()
while check == "Q":
	print(coffee())
	for key in coffee_:
		print(key + ":\t" + coffee_[key]["text"])
	examine = input("Examine: ")
	if examine == "1":
		print(magazines())
		
	elif examine == "2":
		print(coffeeMug())
		
	elif examine == "3":
		print(coaster())
		
	elif examine == "9":
		print(main_menu())
		for key in printMenu:
			print(key + ":\t" + printMenu[key]["text"])
print(main_menu)


if check == "W":
	print(plant())
	for key in plant_:
		print(key + ":\t" + plant_[key]["text"])
	exmaine = input("Examine: ")
	if examine == "1":
		print(dirt())
	elif examine == "2":
		print(leaves())


if check == "E":
	print(desk())
	for key in desk_:
		print(key + ":\t" + desk_[key]["text"])
	examine = input("Examine: ")
	if examine == "1":
		print(files())
	elif examine == "2":
		print(drawers())
	elif examine == "3":
		print(coffeeMug2())

if check == "M":
	print(main_menu())



