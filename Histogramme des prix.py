from matplotlib import pyplot as plt

from Convert import df

plt.hist(df["price_cad"], bins=20)
plt.title("Distribution des prix des livres ($ CAD)")
plt.xlabel("Prix ($ CAD)")
plt.ylabel("Fréquence")
plt.show()
