
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

list1=['seashell', 'strange berry', 'lint']
inventory['pocket']=list1

sorted_inventory=sorted(inventory.values())
print(inventory)

