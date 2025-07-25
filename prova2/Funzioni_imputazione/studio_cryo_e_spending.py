import pandas as pd
import matplotlib.pyplot as plt

# === 1. Caricamento dataset (input dinamico) ===
csv_path = input("Inserisci il percorso del file train.csv: ")
df = pd.read_csv(csv_path)

# === 2. Lista delle colonne di spesa ===
spending_cols = ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']

# === 3. Riempie i NaN con 0 per sommare correttamente ===
df[spending_cols] = df[spending_cols].fillna(0)

# === 4. Crea la colonna booleana 'Spending' ===
df['Spending'] = df[spending_cols].sum(axis=1) > 0

# === 5. Analisi: relazione tra CryoSleep e Spending ===
cryosleep_true_spending_true   = df[(df['CryoSleep'] == True)  & (df['Spending'] == True)]
cryosleep_true_spending_false  = df[(df['CryoSleep'] == True)  & (df['Spending'] == False)]
cryosleep_false_spending_true  = df[(df['CryoSleep'] == False) & (df['Spending'] == True)]
cryosleep_false_spending_false = df[(df['CryoSleep'] == False) & (df['Spending'] == False)]

# === 6. Stampa i risultati con conteggi ===
print("CryoSleep == True  & Spending == True:  ", cryosleep_true_spending_true.shape[0])
print("CryoSleep == True  & Spending == False: ", cryosleep_true_spending_false.shape[0])
print("CryoSleep == False & Spending == True:  ", cryosleep_false_spending_true.shape[0])
print("CryoSleep == False & Spending == False: ", cryosleep_false_spending_false.shape[0])

# === 7. Calcolo percentuali ===
cryosleep_true = df[df['CryoSleep'] == True]
cryosleep_false = df[df['CryoSleep'] == False]

if not cryosleep_true.empty:
    perc_ctst = (cryosleep_true_spending_true.shape[0] / cryosleep_true.shape[0]) * 100
    perc_ctsf = (cryosleep_true_spending_false.shape[0] / cryosleep_true.shape[0]) * 100
    print(f"\nPercentuale di persone in CryoSleep che hanno speso: {perc_ctst:.2f}%")
    print(f"Percentuale di persone in CryoSleep che NON hanno speso: {perc_ctsf:.2f}%")

if not cryosleep_false.empty:
    perc_cfst = (cryosleep_false_spending_true.shape[0] / cryosleep_false.shape[0]) * 100
    perc_cfsf = (cryosleep_false_spending_false.shape[0] / cryosleep_false.shape[0]) * 100
    print(f"\nPercentuale di persone NON in CryoSleep che hanno speso: {perc_cfst:.2f}%")
    print(f"Percentuale di persone NON in CryoSleep che NON hanno speso: {perc_cfsf:.2f}%")

# === 8. Grafico a barre: combinazioni CryoSleep / Spending ===
combinations = {
    "CryoSleep=True & Spending=True": cryosleep_true_spending_true.shape[0],
    "CryoSleep=True & Spending=False": cryosleep_true_spending_false.shape[0],
    "CryoSleep=False & Spending=True": cryosleep_false_spending_true.shape[0],
    "CryoSleep=False & Spending=False": cryosleep_false_spending_false.shape[0],
}

labels = list(combinations.keys())
values = list(combinations.values())

plt.figure(figsize=(10, 6))
bars = plt.bar(labels, values, color=['orange', 'blue', 'orange', 'blue'])

# Aggiunge etichette numeriche sopra ogni barra
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height + 50, f'{int(height)}', ha='center', va='bottom')

plt.title('Conteggi combinati di CryoSleep e Spending')
plt.ylabel('Numero di persone')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
