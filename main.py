import streamlit as st
import numpy as np
import time
import pandas as pd
st.set_page_config(layout="wide")

df = pd.read_excel('df_tratado.xlsx')



st.sidebar.title('Filtros')
st.sidebar.markdown('Selecione os filtros desejados')
cidades = df['Cidade'].unique().tolist()
cidades.sort()
cidade = st.sidebar.multiselect('Cidade:', cidades,default=cidades, placeholder='Selecione uma ou mais cidades')


if not cidade:
    cidade = cidades

df_filtered = df[df['Cidade'].isin(cidade)][['Cidade', 'Paróquia', 'Grupo de Jovens']]


st.title('Setor Juventude - Diocese de São José dos Pinhais') 
st.divider()

col1, col2, col3, = st.columns(3)
col6 = st.columns(1)
col4, col5 = st.columns(2)

col1.metric('Cidades', df_filtered['Cidade'].nunique())
col2.metric('Paróquias', df_filtered['Paróquia'].nunique())
col3.metric('Grupos', df_filtered['Grupo de Jovens'].nunique())

st.divider()

st.table(df_filtered)


st.divider()

st.write('Mapa de coordenadas')

st.map(df,
    latitude='Latitude',
    longitude='Longitude')

# result = st.button('Inserir um novo registro')
# if result:
#     st.write('Clicado!')  
#     nome_coordenador = st.text_input('Coordenador(a)')
#     new_cidade = st.selectbox('Cidade', df['Cidade'].unique())
#     new_parioquia = st.selectbox('Paróquia', df['Paróquia'].unique())
#     new_grupo = st.selectbox('Grupo de Jovens', df['Grupo de Jovens'].unique())
#     salvo = st.button('Salvar')
#     calcelado = st.button('Cancelar')

#     if salvo:
#         df = df.append({'Cidade': new_cidade, 'Paróquia': new_parioquia, 'Grupo de Jovens': new_grupo, 'Coordenador(a)': nome_coordenador}, ignore_index=True)
#         st.table(df)
#         st.write('Registro salvo com sucesso!')
#     elif calcelado:
#         st.write('Registro cancelado!')
#     else:
#         st.write('Nenhuma ação realizada!')












# @st.cache # Função para armazenar os dados em cache
# def load_data(nrows):
    
#     data = pd.read_csv('https://example.com/data.csv', nrows=nrows)
#     return data
