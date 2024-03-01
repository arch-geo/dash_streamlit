#%%
import streamlit as st
import pandas as pd


st.set_page_config(layout = 'wide')

with st.sidebar:
    st.title('Análise de Lucro')
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    with st.sidebar:
        distinct_regions = df['Region'].unique()
        region_selected = st.selectbox('Escolha uma região', distinct_regions)
        if region_selected:
            df = df[df["Region"] == region_selected] 

        country_selected = st.radio("Tipo de item", df["Country"].unique())

        
        if country_selected:
            df = df[df["Country"] == country_selected]

    st.header("Lucro por tipo de item")
    st.bar_chart(df, x="Item Type", y=["Total Profit", "Total Cost"], use_container_width=True, )
    st.info('This is a purely informational message', icon="ℹ️")
    st.dataframe(df, use_container_width=True)

# %%
st.altair_chart