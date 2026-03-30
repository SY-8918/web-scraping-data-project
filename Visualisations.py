import pandas as pd
import matplotlib.pyplot as plt

# Charger le CSV généré par ton script de scraping
df = pd.read_csv("books_dataset.csv")

# Nettoyer les prix en GBP → nombre float
df["price_clean"] = (
    df["price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .str.strip()
    .astype(float)
)


# Convertir en CAD (si tu l’avais fait) sinon tu peux ajouter ceci
df["price_cad"] = df["price_clean"] * 1.74  # taux approximatif

# --- VISUALISATION ---
plt.boxplot(df["price_cad"])
plt.title("Boxplot des prix des livres ($ CAD)")
plt.ylabel("Prix ($ CAD)")
plt.show()

