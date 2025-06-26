import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🔍 Dashboard – Détection de Fraude Bancaire")

@st.cache_data
def load_data():
    return pd.read_csv("data/creditcard.csv")

df = load_data()

st.subheader("Aperçu des données")
st.dataframe(df.head())

st.subheader("Distribution des classes")
fig1, ax1 = plt.subplots()
sns.countplot(x="Class", data=df, ax=ax1)
st.pyplot(fig1)

st.subheader("Distribution du montant")
fig2, ax2 = plt.subplots()
sns.histplot(df["Amount"], bins=100, kde=True, ax=ax2)
st.pyplot(fig2)

st.subheader("Montant vs Fraude")
fig3, ax3 = plt.subplots()
sns.boxplot(x="Class", y="Amount", data=df, ax=ax3)
st.pyplot(fig3)

st.subheader("Matrice de corrélation")
fig4, ax4 = plt.subplots(figsize=(10,8))
sns.heatmap(df.corr(), cmap="coolwarm", ax=ax4)
st.pyplot(fig4)