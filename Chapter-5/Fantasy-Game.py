def displayInventory(inventory):
    sumAll = 0
    print("Inventory: ")
    for k, v in inventory.items():
        print(str(v) + " " + k)
        sumAll += v
    print("Total number of Items: " + str(sumAll))


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(inventory)
