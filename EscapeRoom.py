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

examine_dict = {
"coffee table": {
	"text": "You check the coffee table. There are some magazines, a coffee mug, and a coaster.",
	"options": {
		"1": "magazines", 
		"2": "coffee mug",
		"3": "coaster",
		"4": "return"}	
	},
"magazines": {
	"text": "These editions are from last week",
	"options": {
		"1": "collect",
		"2": "return"}
	},
"coffee mug": {
	"text": "There's still some coffee left",
	"options": {
		"1": "collect fingerprint",
		"2": "return"}
	},
"coaster": {
	"text": "It's just a coaster",
	"options": {
		"1": "return"}
	},
"plant": {
	"text": "This plant has seen better days...looks like it's been neglected for weeks. Look, it's leaves are all curled and wrinkled up. Not that water will save it now.",
	"options": {
		"1": "dirt",
		"2": "leaves",
		"3": "return"}
	},
"dirt": {
	"text": "The dirt's all dried up. You feel no resistance as you push your fingers through, until you hit something solid.",
	"options": {
		"1": "collect object",
		"2": "return"}
	},
"leaves": {
	"text": "You start to unfold some of the leaves and notice some dark brown spots on some of the leaves.",
	"options": {
		"1": "Scratch at the leaves",
		"2": "return" }
	},
"desk": {
	"text": "What a mess..where should I start looking?",
	"options": {
		"1": "files",
		"2": "drawers",
		"3": "coffee mug",
		"4": "return"}
	},
"files": {
	"text": "--insert something interesting--",
	"options": {
		"1": "read more",
		"2": "return"}
	},
"drawers": {
	"text": "It's locked...",
	"options": {
		"1": "use key",
		"2": "return"}
	},
"coffee mug": {
	"text": "There's still some coffee left",
	"options": {
		"1": "collect fingerprint",
		"2": "return"}
	}
}
	
main_ = {"Q": "The coffee table", "W": "The pitcher plant", "E": "The computer desk"}

def select():
	select = input("let's search: ").upper()
def select1():
	select1 = input("examine: ")
def select2():
	select2 = input("What do you want to do?: ")
def screen_main():
	print("Where do you want to search?")
	print()
	print(main_)
	print()
	print(select())

print(screen_main())

while select == "Q":
	print(examine_dict["coffee table"]["text"])
	print(examine_dict["coffee table"]["options"])
	print(select1())
	if select1 == "1":
		print(examine_dict["magazine"]["text"])
		print(examine["magazine"]["options"])
		print(select2())
	elif select2 == "1":
		print("added to inventory")
	elif select2 == "2":
		print(examine_dict["coffee table"]["options"])
		print(select())
else:
	print(screen_main())



