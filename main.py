import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Récupération des données via l'API
url = "http://10.101.1.116:8000/kpis"
response = requests.get(url)
data = response.json()

# Conversion des données en DataFrame pour une analyse facile
df = pd.DataFrame(data)

# Afficher les premières lignes du DataFrame pour vérifier la structure des données
print(df.head())

# Afficher les noms des colonnes
print(df.columns)

# Filtrer les données pour récupérer les KPI spécifiques et leurs valeurs
kpis = {
    "Lead Time": None,
    "Order Fulfillment Rate": None,
    "Inventory Turnover": None,
    "Order Accuracy": None,
    "Supplier Lead Time": None,
    "Return Rate": None  # Ajouter le Return Rate ici
}

# Remplir les KPI avec leurs valeurs
for kpi in kpis.keys():
    value = df[df['kpi_name'] == kpi]['value'].values
    if len(value) > 0:
        kpis[kpi] = value[0]

# Vérifier si le "Return Rate" est calculable à partir des données disponibles
# Simulation de la donnée si elle n'est pas présente explicitement dans l'API
# Exemple : calculer le Return Rate si le nombre de retours et le nombre de commandes sont disponibles.
# Vous devrez ajuster cette logique selon les données réelles disponibles.

# Supposons que vous ayez ces deux KPI dans l'API ou que vous les calculiez :
# "Total Returns" (Nombre total de retours) et "Total Orders" (Nombre total de commandes)

# Si ces données sont présentes, calculez le Return Rate :
total_returns = df[df['kpi_name'] == 'Total Returns']['value'].values
total_orders = df[df['kpi_name'] == 'Total Orders']['value'].values

if len(total_returns) > 0 and len(total_orders) > 0:
    return_rate = total_returns[0] / total_orders[0] * 100
    kpis["Return Rate"] = return_rate
else:
    print("Données manquantes pour calculer le Return Rate.")

# Afficher les valeurs des KPI récupérées
print("\nValeurs des KPI récupérées :")
print(kpis)

# Préparer les données pour le graphique radar
labels = list(kpis.keys())
values = list(kpis.values())

# Assurez-vous que toutes les valeurs des KPI sont valides (non nulles)
if None in values:
    print("Certaines valeurs des KPI sont manquantes, vérifiez les données.")
else:
    # Créer un graphique radar
    # Nombre de variables
    num_vars = len(labels)

    # Calculer l'angle pour chaque axe du graphique
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Répéter la première valeur pour fermer le graphique
    values += values[:1]
    angles += angles[:1]

    # Créer le graphique
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Tracer les valeurs sur le graphique radar
    ax.fill(angles, values, color='skyblue', alpha=0.6)
    ax.plot(angles, values, color='blue', linewidth=3)  # Ajouter le contour du graphique

    # Ajouter les labels des axes
    ax.set_yticklabels([])  # Masquer les labels de l'axe radial
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=12, fontweight='bold', color='black')

    # Ajouter les valeurs des KPI sur le graphique
    for i, (angle, value) in enumerate(zip(angles[:-1], values[:-1])):
        ax.text(angle, value + 0.05, f"{value:.2f}", horizontalalignment='center', size=12, color='black', fontweight='bold')

    # Titre du graphique
    ax.set_title("KPI Performance", size=16, color='blue', fontweight='bold')

    # Afficher le graphique
    plt.tight_layout()
    plt.show()

    # Recommandations
    recommendations = """
    1. Si le "Lead Time" est trop élevé, essayer d'optimiser les processus de production ou d'approvisionnement.
    2. Si le "Order Fulfillment Rate" est faible, améliorer la gestion des stocks et des commandes.
    3. Un "Inventory Turnover" bas peut suggérer un excédent de stock, il peut être nécessaire de réévaluer la stratégie de gestion des stocks.
    4. Si "Order Accuracy" est faible, renforcer les contrôles qualité dans le processus de préparation des commandes.
    5. Si le "Supplier Lead Time" est élevé, envisager de diversifier les fournisseurs ou de négocier de meilleurs délais.
    6. Si le "Return Rate" est élevé, envisager d'analyser les raisons des retours pour améliorer les processus de production ou de contrôle qualité.
    """
    print("Recommandations stratégiques :\n", recommendations)
