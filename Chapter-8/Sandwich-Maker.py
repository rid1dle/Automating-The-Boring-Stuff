import pyinputplus as pyip

bill = 0

bread = pyip.inputMenu(prompt="Please Select the bread type best suited for your taste and needs...: \n", choices=[
                       'Wheat', 'White', 'Sourdough'])

if (bread == 'Wheat'):
    bill += 40

elif (bread == 'White'):
    bill += 30

else:
    bill += 50

patty = pyip.inputMenu(prompt="Now your what would be a Sandwitch without some patty... Please choose the ingredient for your patty...: \n", choices=[
                       'Chicken', 'Turkey', 'Ham', 'Tofu'])

if (patty == "Chicken"):
    bill += 50

elif (patty == "Turkey"):
    bill += 40

elif (patty == "Ham"):
    bill += 60

else:
    bill += 30

print("What makes a Sandwitch extra Delicious..?? You got it.. Cheese.. Who want some....")
cheese = pyip.inputYesNo(prompt="Cheese (yes/no): ")

cheeseType = None
if (cheese == 'yes'):
    cheeseType = pyip.inputMenu(prompt="Oh! Now now now.. You gotta let us know the Kind of cheese you want in your Mouthwatering Sandwitch come on...: \n", choices=[
                                "Cheddar", "Swiss", "Mozzarella"])

    if (cheeseType == "Cheddar"):
        bill += 30

    elif (cheeseType == "Swiss"):
        bill += 40

    else:
        bill += 50

print("Your Sandwitch is almost ready.. But you know.. A sandwitch is never truly complete without some kind of toppings...: ")
mayo = pyip.inputYesNo(prompt="Mayo: ")

if (mayo == "yes"):
    bill += 30

mustard = pyip.inputYesNo(prompt="Mustard: ")

if (mustard == 'yes'):
    bill += 30

lettuce = pyip.inputYesNo(prompt="Lettuce: ")

if (lettuce == "yes"):
    bill += 30

tomato = pyip.inputYesNo(prompt="Tomato: ")

if (tomato == 'yes'):
    bill += 30

sandwitchNo = pyip.inputInt(
    prompt="Hey Hey.. You need to tell us how many to make you know.. Or We will make just one.. Decide who you or your GF who will eat it..: ", min=1)

bill *= sandwitchNo

print("So, Had your lovely sandwitch.. Now time to PayUp.. Comeon.. Don't be stingy.... Your total is.. ONLY: " + str(bill))
