# Portfolio – Analyse Exploratoire des Données (Fraude & Marketing)

Ce dépôt GitHub contient deux mini-projets EDA :

1. **Fraude Bancaire** – Dataset *Credit Card Fraud Detection*  
2. **Campagne Marketing** – Dataset *Marketing Campaign*

Chaque projet inclut :

- Un **notebook Jupyter** pas‑à‑pas (`eda_*.ipynb`)
- Un **dashboard Streamlit** (`dashboard.py`) pour explorer les données
- Un dossier `data/` (vide) dans lequel placer le CSV correspondant

## Installation rapide

```bash
git clone <votre‑repo‑url>
cd portfolio-EDA
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate sous Windows
pip install -r requirements.txt
```

## Lancer les notebooks

```bash
jupyter notebook
```

## Lancer un dashboard

```bash
cd fraude_eda   # ou marketing_eda
streamlit run dashboard.py
```

> **Remarque :** Téléchargez les datasets depuis Kaggle et placez-les dans le dossier `data/` :
> - `creditcard.csv` (fraude)  
> - `marketing_campaign.csv` (marketing)

## Arborescence

```
portfolio-EDA/
├── fraude_eda/
│   ├── data/
│   ├── eda_credit_fraud.ipynb
│   └── dashboard.py
├── marketing_eda/
│   ├── data/
│   ├── eda_marketing.ipynb
│   └── dashboard.py
├── requirements.txt
└── .gitignore
```## 📊 Visualisations

### 1. Répartition des classes (fraude vs normale)
> Les transactions frauduleuses représentent une part infime du total. Cela justifie l’utilisation de méthodes de rééquilibrage.

### 2. Matrice de corrélation
> Certaines variables sont faiblement corrélées à la variable cible. Cela aidera pour la sélection de variables pertinentes.

### 3. Montant par type de transaction
> Le montant moyen et les outliers varient selon qu’il s’agisse d’une fraude ou non.

### 4. Distribution du montant
> Distribution très asymétrique. Une transformation log est à envisager.

