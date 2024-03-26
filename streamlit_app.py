import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import altair as alt
import time
import zipfile

# Page title
st.set_page_config(page_title='ML Model Building', page_icon='🤖')
st.title('🤖 ML Model Building')

with st.expander('About this app'):
  st.markdown('**What can this app do?**')
  st.info('This app allow users to build a machine learning (ML) model in an end-to-end workflow. Particularly, this encompasses data upload, data pre-processing, ML model building and post-model analysis.')

  st.markdown('**How to use the app?**')
  st.warning('To engage with the app, go to the sidebar and 1. Select a data set and 2. Adjust the model parameters by adjusting the various slider widgets. As a result, this would initiate the ML model building process, display the model results as well as allowing users to download the generated models and accompanying data.')

  st.markdown('**Under the hood**')
  st.markdown('Data sets:')
  st.code('''- Drug solubility data set
  ''', language='markdown')
  
  st.markdown('Libraries used:')
  st.code('''- Pandas for data wrangling
- Scikit-learn for building a machine learning model
- Altair for chart creation
- Streamlit for user interface
  ''', language='markdown')


# Lista de variables
variables = ["Tamaño del mercado", "PIB per cápita", "Estabilidad política", "Competencia", 
"Infraestructura", "Acceso a recursos naturales", "Capital humano", "Cultura", "Idioma", 
"Regulaciones comerciales", "Riesgo político", "Riesgo económico", "Competencia local", 
"Barreras de entrada", "Potencial de crecimiento", "Rentabilidad", "Ajuste estratégico"]

# Función para asignar pesos
def asignar_pesos(variables):
  """
  Asigna pesos a las variables de forma automática utilizando una distribución exponencial decreciente.

  Args:
      variables: Lista ordenada de variables.

  Returns:
      Lista de pesos para las variables.
  """

  # Parámetro de la distribución exponencial
  alfa = 0.5

  # Cálculo del peso total
  peso_total = sum(1 / (alfa**i) for i in range(len(variables)))

  # Cálculo de los pesos individuales
  pesos = [1 / (alfa**i) / peso_total for i in range(len(variables))]

  return pesos

# Interfaz de usuario
st.title("Selección y Ponderación de Variables")

# Selección de variables
variables_seleccionadas = st.multiselect("Seleccione las variables relevantes:", variables)

# Ordenamiento de variables
orden = st.slider("Ordene las variables según su importancia (1 = más importante):", 1, len(variables_seleccionadas), len(variables_seleccionadas))

# Cálculo de pesos
pesos = asignar_pesos(variables_seleccionadas[orden-1])

# Visualización de resultados
st.table(pd.DataFrame({"Variable": variables_seleccionadas, "Peso": pesos}))
