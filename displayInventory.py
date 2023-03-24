stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    print('Inventory:')
    [print(y, x) for x, y in inventory.items()]
    print(f'Total number of items: {sum(inventory.values())}')
if __name__ == "__main__":
    displayInventory(stuff)
