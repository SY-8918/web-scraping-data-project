from matplotlib import pyplot as plt

from Convert import df

top10 = df.sort_values("price_cad", ascending=False).head(10)

plt.barh(top10["title"], top10["price_cad"])
plt.title("Top 10 des livres les plus chers ($ CAD)")
plt.xlabel("Prix ($ CAD)")
plt.gca().invert_yaxis()
plt.show()
