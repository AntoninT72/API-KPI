
# 📦 Analyse de Performance Supply Chain - Visualisation KPI Radar

Ce projet a pour objectif de fournir une **analyse décisionnelle de la performance logistique** d'une entreprise à partir de données de KPI accessibles via une API. Il inclut le **calcul et la visualisation graphique** des indicateurs clés sous forme de graphique radar.

---

## 🎯 Objectifs

- Extraire les données brutes depuis une API REST.
- Calculer les principaux KPI de la Supply Chain.
- Identifier les points de faiblesse ou d’alerte.
- Proposer des recommandations concrètes.
- Visualiser les résultats de manière claire et interactive.

---

## 📊 KPI Analyés

- Lead Time (délai de livraison)
- Order Fulfillment Rate (taux de satisfaction des commandes)
- Inventory Turnover (rotation des stocks)
- Order Accuracy (taux de commandes parfaites)
- Supplier Lead Time (ponctualité des fournisseurs)
- Return Rate (taux de retour)

> ⚠️ Certains KPI comme le Return Rate peuvent être calculés à partir de données complémentaires si disponibles (`Total Returns` / `Total Orders`).

---

## 🔗 Données

Les données sont récupérées depuis l'API suivante :

```
http://10.101.1.116:8000/kpis
```

---

## 🛠️ Technologies utilisées

- Python 3.11+
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
- API REST (GET request via `requests`)

---

## 📌 Installation

1. **Cloner le projet**

```bash
git clone https://github.com/votre-utilisateur/nom-du-projet.git
cd nom-du-projet
```

2. **Créer un environnement virtuel (recommandé)**

```bash
python -m venv venv
source venv/bin/activate  # sur Windows : venv\Scripts\activate
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

> Exemple de contenu de `requirements.txt` :
```txt
pandas
matplotlib
seaborn
requests
```

---

## ▶️ Utilisation

Lancez le script principal pour générer l'analyse KPI avec graphique radar :

```bash
python main.py
```

Un graphique radar s'affichera avec les valeurs de chaque KPI. Des recommandations stratégiques seront également affichées dans la console.

---

## 📈 Exemple de sortie visuelle

<img src="docs/graphique_radar_exemple.png" alt="Radar KPI" width="500"/>

---

## 💡 Recommandations Automatisées

Le script fournit automatiquement des recommandations en fonction des résultats observés sur les KPI, comme :

- Réduction du Lead Time.
- Amélioration de la précision des commandes.
- Optimisation des niveaux de stock.
- Diversification des fournisseurs.

---

## 📂 Structure du projet

```
.
├── main.py                 # Script principal d'analyse
├── requirements.txt        # Dépendances
├── README.md               # Documentation
└── docs/
    └── graphique_radar_exemple.png  # (optionnel) Exemple d'image
```

---

## 📄 Licence

Ce projet est open-source sous licence MIT.

---

## 🙌 Contributions

Les contributions sont les bienvenues !  
Merci de créer une _issue_ ou une _pull request_ pour proposer une amélioration.

---

## 👤 Auteur

**Antonin** – Analyste Logistique  


---
