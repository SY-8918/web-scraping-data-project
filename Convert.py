#visualisation
import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier
df = pd.read_csv("books_dataset.csv")

# Vérifier les colonnes
print("Colonnes trouvées :", df.columns)

# 1. Nettoyer les symboles £ et Â£
df["price_clean"] = (
    df["price"]
    .astype(str)
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
)

# 2. Convertir en float
df["price_num"] = pd.to_numeric(df["price_clean"], errors="coerce")

# 3. Enlever les lignes invalides
df = df.dropna(subset=["price_num"])

# 4. Conversion GBP → CAD
GBP_TO_CAD = 1.75
df["price_cad"] = df["price_num"] * GBP_TO_CAD

# ---- Vérification console ----
print(df[["price", "price_clean", "price_num", "price_cad"]].head())

# ---- Visualisation ----
plt.hist(df["price_cad"], bins=10)
plt.title("Distribution des prix des livres en $ CAD")
plt.xlabel("Prix ($ CAD)")
plt.ylabel("Nombre de livres")
plt.show()
