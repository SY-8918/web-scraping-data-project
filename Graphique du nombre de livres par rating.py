import os
import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV
df = pd.read_csv("books_dataset.csv")

# Vérifier les colonnes
print("Colonnes trouvées :", df.columns)

# Compter le nombre de livres par rating
rating_counts = df["rating"].value_counts().sort_index()

# Créer le graphique
plt.figure(figsize=(8, 5))
plt.bar(rating_counts.index.astype(str), rating_counts.values)
plt.title("Nombre de livres par rating")
plt.xlabel("Rating")
plt.ylabel("Nombre de livres")

# Créer le dossier images si nécessaire
os.makedirs("images", exist_ok=True)

# Sauvegarder l'image
plt.savefig("images/livres_par_rating.png", bbox_inches="tight")
plt.close()