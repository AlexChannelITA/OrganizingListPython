hotbar = [
    "Torch",
    "Shield",
    "Sword",
    "Axe",
    "Bow",
    "Bucket of waterr"
]

print("Benvenuto giocatore quale oggetto vuoi selezioanre per iniziare la tua avventura?")

print(hotbar)

#! input to let the person pick what they have in their "hotbar"
x = input()

index = hotbar.index(x) #? i take the index of the item he/she selected
item = hotbar.pop(index) #? i delete the old object inside the list
hotbar.insert(0,item) #? i place it on the first place of the list making every other move

#! This one below is more simple
#! i take the "x" variable and the first index of "hotbar"
#! and i switch places 
#! so the "Sword" switch places with "Torch"
#! and the others remain the same
#//hotbar[x], hotbar [0] = hotbar[0], hotbar [x]

print(hotbar)
