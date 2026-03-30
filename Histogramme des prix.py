import os
import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV
df = pd.read_csv("books_dataset.csv")

# Vérifier les colonnes
print("Colonnes trouvées :", df.columns)

# Nettoyer la colonne prix si nécessaire
if "price_cad" in df.columns:
    prices = df["price_cad"]
else:
    df["price_clean"] = df["price"].astype(str).str.replace("Â£", "", regex=False).str.replace("£", "", regex=False)
    df["price_num"] = pd.to_numeric(df["price_clean"], errors="coerce")
    df["price_cad"] = df["price_num"] * 1.75
    prices = df["price_cad"]

# Créer le graphique
plt.figure(figsize=(8, 5))
plt.hist(prices.dropna(), bins=10)
plt.title("Distribution des prix des livres en $ CAD")
plt.xlabel("Prix ($ CAD)")
plt.ylabel("Nombre de livres")

# Créer le dossier images si nécessaire
os.makedirs("images", exist_ok=True)

# Sauvegarder l'image
plt.savefig("images/histogramme_prix.png", bbox_inches="tight")
plt.close()