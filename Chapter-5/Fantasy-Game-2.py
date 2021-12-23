def displayInventory(inventory):
    sumAll = 0
    print("Inventory: ")
    for k, v in inventory.items():
        print(str(v) + " " + k)
        sumAll += v
    print("Total number of Items: " + str(sumAll))


def addToInventory(inventory, addItems):
    for i in addItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory


inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = addToInventory(inventory, dragonLoot)
displayInventory(inventory)
