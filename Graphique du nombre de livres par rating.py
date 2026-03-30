from matplotlib import pyplot as plt

from Convert import df

plt.bar(df["rating"].value_counts().index, df["rating"].value_counts().values)
plt.title("Nombre de livres par rating")
plt.xlabel("Rating")
plt.ylabel("Nombre de livres")
plt.show()
