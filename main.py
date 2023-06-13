hotbar = [
    "Torcia",
    "Piccone",
    "Spada",
    "Ascia",
    "Arco",
    "Secchio d'acqua"
]

print("Benvenuto giocatore quale oggetto vuoi selezioanre per iniziare la tua avventura?")

print(hotbar)

#! La variabile di input per far sciegliere al giocatore l'elemento
x = input()

index = hotbar.index(x) #? Prendo l'indice dell'oggetto selezionato
item = hotbar.pop(index) #? Tolgo l'oggetto selezionato dalla lista con l'indice, la variabile "item" è l'oggetto 
hotbar.insert(0,item) #? Riinserisco l'oggetto selezionato all'inizio della lista


#// Scambia i valori della posizione "x" con quelli in posizione 0
#// ovvero il primo elemento della "hotbar" con il quarto elemento
#//hotbar[x], hotbar [0] = hotbar[0], hotbar [x]

print(hotbar)