from matplotlib import pyplot as plt

from Convert import df

df["in_stock"] = df["availability"].str.contains("In stock", case=False)

plt.bar(["En stock", "Rupture"], df["in_stock"].value_counts().values)
plt.title("Disponibilité des livres")
plt.ylabel("Nombre de livres")
plt.show()
