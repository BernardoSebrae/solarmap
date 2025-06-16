import streamlit as st
import math
import pandas as pd

# Mostra a logo no topo
st.image("solarize.png", width=150)  # Você pode ajustar o tamanho conforme necessário

st.title("☀️ Solarize")
st.write("""
App para estimativa de:
- **Inclinação ideal** de placas solares
- **Número máximo de placas** por área
- **Potência máxima do sistema (kW)**
""")

# Entradas principais
col1, col2 = st.columns(2)
with col1:
    lat = st.number_input("Latitude", 
                          value=-19.9, 
                          min_value=-90.0, 
                          max_value=90.0, 
                          format="%.6f",
                          help="Valores entre -90° e 90°")

with col2:
    lon = st.number_input("Longitude", 
                          value=-43.9, 
                          min_value=-180.0, 
                          max_value=180.0, 
                          format="%.6f",
                          help="Valores entre -180° e 180°")

area_disponivel = st.number_input("Área disponível (m²)", 
                                  value=30.0,
                                  min_value=1.0,
                                  step=1.0)

# Configurações avançadas
with st.expander("⚙️ Configurações Avançadas"):
    tamanho_placa_m2 = st.number_input("Tamanho de cada placa (m²)", 
                                       value=1.7,
                                       min_value=0.1)
    
    potencia_placa_w = st.number_input("Potência por placa (W)", 
                                       value=450,
                                       min_value=10)

# Funções
def angulo_ideal(latitude):
    return abs(latitude) * 0.9 + 3.1  # Fórmula adaptada para o Brasil

def placas_possiveis(area_total, area_placa):
    return math.floor(area_total / area_placa)

# Execução
if st.button("🔍 Calcular"):
    with st.spinner("Calculando..."):
        angulo = angulo_ideal(lat)
        num_placas = placas_possiveis(area_disponivel, tamanho_placa_m2)
        potencia_total_kw = (num_placas * potencia_placa_w) / 1000  # Convertendo para kW

        # Resultados
        st.success(f"**Inclinação ideal:** {angulo:.1f}°")
        st.success(f"**Número de placas:** {num_placas} unidades")
        st.success(f"**Potência total estimada:** {potencia_total_kw:.2f} kW")

        # Mapa
        st.subheader("📍 Localização no Mapa")
        df_coordenadas = pd.DataFrame({'lat': [lat], 'lon': [lon]})
        st.map(df_coordenadas, zoom=16)

st.markdown("---")
st.caption("Desenvolvido por ~Montijo - Fórmulas adaptadas de INPE")
