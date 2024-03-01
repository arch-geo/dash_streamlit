#%%
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(layout = 'wide')
home = r"C:\repos\estudos\dash_streamlit\testes"

df = pd.read_csv(os.path.join(home,"supermarket_sales.csv"))
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].apply(lambda x: x.year*100 + x.month)
df = df.sort_values("Date")

month = st.sidebar.selectbox("Escolha um mês", df["Month"].unique())

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

df_filtered = df[df["Month"] == month]
fig_data = px.bar(df_filtered, 
                  x="Date", 
                  y="Total", 
                  title="Faturamento por Mês", 
                  color="City")
col1.plotly_chart(fig_data, use_container_width=True)

fig_prod = px.bar(df_filtered, 
                  x="Date", 
                  y="Total", 
                  title="Faturamento por Tipo de Produto", 
                  color="Product line", 
                  orientation="v")
col2.plotly_chart(fig_prod, use_container_width=True)

city_total = df_filtered.groupby("City")["Total"].sum().reset_index()   
fig_city = px.bar(city_total, 
                  x="City", 
                  y="Total", 
                  title="Faturamento por Filial")
col3.plotly_chart(fig_city, use_container_width=True)

fig_kind = px.pie(df_filtered, 
                  names="Payment", 
                  values="Total", 
                  title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

city_total = df_filtered.groupby("City")["Rating"].mean().reset_index()   
fig_city = px.bar(city_total, 
                  x="City", 
                  y="Rating", 
                  title="Faturamento por Avaliação",
                  color="Rating",
                  range_color=[6,10])
col5.plotly_chart(fig_city, use_container_width=True)

# %%
#left zeroes
