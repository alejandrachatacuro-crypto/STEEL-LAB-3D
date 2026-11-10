import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

st.set_page_config(page_title="LABSTEEL 3D", page_icon="⚙️", layout="wide")

st.markdown("""
<style>
.stApp { background: #0b111a; color: #e8eef6; }
[data-testid="stSidebar"] { background: #111c2a; }
.block-container { padding-top: 1.5rem; }
h1,h2,h3 { color: #edf4fb; }
div[data-testid="stMetric"] {
  background: #142235; border: 1px solid #263c55;
  padding: 14px; border-radius: 12px;
}
.lab-note { color:#9fb2c8; font-size:0.9rem; }
</style>
""", unsafe_allow_html=True)

st.title("⚙️ LABSTEEL 3D")
st.caption("LABORATORIO VIRTUAL DE TRATAMIENTOS TÉRMICOS DEL ACERO · PROTOTIPO ACADÉMICO")

with st.sidebar:
    st.header("Panel de control")
    section = st.radio("Módulo", [
        "Inicio", "Tratamiento térmico", "Ensayo de dureza",
        "Microestructura", "Resultados"
    ])
    st.divider()
    st.caption("Versión inicial · Modelo educativo")

if section == "Inicio":
    st.subheader("Centro de simulación metalúrgica")
    st.markdown("Explora el comportamiento del acero mediante parámetros controlables, visualizaciones 3D y cálculos transparentes.")
    c1,c2,c3 = st.columns(3)
    c1.metric("Módulos", "4")
    c2.metric("Material de referencia", "AISI 1045")
    c3.metric("Estado", "Prototipo")
    st.info("Esta primera versión establece la interfaz y el flujo de trabajo. Los resultados simulados se identifican como estimaciones educativas, no como mediciones de laboratorio.")
    st.markdown("**Ruta de desarrollo**")
    st.markdown("1. Configurar material y ciclo térmico.\n2. Visualizar probeta y horno en 3D.\n3. Incorporar modelos metalúrgicos validados.\n4. Añadir ensayos de dureza y tracción.\n5. Exportar resultados y preparar publicación web.")

elif section == "Tratamiento térmico":
    st.subheader("Simulador de ciclo térmico")
    left, right = st.columns([1, 1.35])
    with left:
        steel = st.selectbox("Material", ["AISI 1045 (acero medio carbono)", "AISI 1020 (acero bajo carbono)", "AISI 4140 (acero aleado)"])
        treatment = st.selectbox("Tratamiento", ["Temple", "Normalizado", "Recocido", "Temple y revenido"])
        temp = st.slider("Temperatura de calentamiento (°C)", 400, 1000, 850, 5)
        hold = st.slider("Tiempo de permanencia (min)", 5, 180, 30, 5)
        cooling = st.selectbox("Medio de enfriamiento", ["Agua", "Aceite", "Aire", "Horno"])
        run = st.button("▶ Ejecutar simulación", type="primary", use_container_width=True)
    with right:
        # Geometric visualization only: no claim that color predicts real temperature.
        theta = np.linspace(0, 2*np.pi, 80)
        z = np.linspace(0, 5, 50)
        T,Z = np.meshgrid(theta,z)
        radius = 0.72
        X = radius*np.cos(T); Y = radius*np.sin(T)
        fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, surfacecolor=Z,
            colorscale=[[0,"#526477"],[0.45,"#a84b32"],[1,"#ff9b45"]],
            showscale=False, lighting=dict(ambient=0.45, diffuse=0.8, specular=0.65, roughness=0.35))])
        fig.update_layout(title="Probeta cilíndrica · vista 3D conceptual",
            paper_bgcolor="#0b111a", plot_bgcolor="#0b111a", font_color="#e8eef6",
            margin=dict(l=0,r=0,t=45,b=0), height=390,
            scene=dict(xaxis_visible=False,yaxis_visible=False,zaxis_visible=False,
                       bgcolor="#0b111a", aspectmode="manual", aspectratio=dict(x=1,y=1,z=2.4)))
        st.plotly_chart(fig, use_container_width=True)
    if run:
        st.success("Ciclo registrado en el prototipo.")
        st.write(f"**Configuración:** {steel} · {treatment} · {temp} °C · {hold} min · enfriamiento en {cooling}.")
        st.warning("La selección registra las condiciones, pero todavía no predice fases ni dureza. Esa función se añadirá cuando se definan modelos y fuentes metalúrgicas para cada acero.")

elif section == "Ensayo de dureza":
    st.subheader("Registro y comparación de dureza")
    st.markdown("Introduce resultados obtenidos en el laboratorio físico. También puedes probar el cálculo con datos de ejemplo, siempre identificados como demostrativos.")
    mode = st.radio("Origen de los datos", ["Medición experimental", "Ejemplo demostrativo"], horizontal=True)
    if mode == "Medición experimental":
        initial = st.number_input("Dureza inicial (HRC)", min_value=0.0, max_value=80.0, value=20.0, step=0.5)
        final = st.number_input("Dureza final (HRC)", min_value=0.0, max_value=80.0, value=35.0, step=0.5)
        label = "Datos introducidos por el usuario; verificar escala y procedimiento."
    else:
        initial, final = 20.0, 55.0
        label = "Datos ficticios de demostración; no son resultados medidos ni valores garantizados del AISI 1045."
    delta = final - initial
    pct = (delta / initial * 100) if initial else np.nan
    a,b,c = st.columns(3)
    a.metric("Dureza inicial", f"{initial:.1f} HRC")
    b.metric("Dureza final", f"{final:.1f} HRC")
    c.metric("Variación relativa", f"{pct:.1f} %" if np.isfinite(pct) else "No calculable")
    st.caption(label)
    st.markdown("**Nota técnica:** HRC solo debe usarse cuando el material y el rango cumplen las condiciones del método Rockwell C. No convertir escalas sin una norma o tabla apropiada.")

elif section == "Microestructura":
    st.subheader("Atlas de microestructuras")
    phase = st.selectbox("Estructura para estudiar", ["Ferrita y perlita", "Martensita", "Bainita", "Austenita"])
    st.info("En esta versión se presenta una ficha conceptual. Las micrografías reales deberán proceder de fuentes autorizadas o de fotografías metalográficas propias.")
    descriptions = {
        "Ferrita y perlita": "Constituyentes habituales en aceros al carbono enfriados lentamente; la proporción depende de la composición.",
        "Martensita": "Producto de una transformación sin difusión asociada a un enfriamiento suficientemente rápido desde la austenita.",
        "Bainita": "Microestructura formada en intervalos de temperatura intermedios, con morfología dependiente de las condiciones.",
        "Austenita": "Fase de estructura cúbica centrada en las caras, estable a temperaturas elevadas para muchos aceros."
    }
    st.markdown(f"**{phase}**")
    st.write(descriptions[phase])
    st.caption("La apariencia de una microestructura no debe inferirse solo por el nombre del tratamiento: depende de composición, temperatura, tiempo y velocidad de enfriamiento.")

elif section == "Resultados":
    st.subheader("Hoja de resultados")
    st.write("Registra aquí los datos de cada probeta para compararlos en una etapa posterior.")
    df = pd.DataFrame([
        {"Probeta":"A","Condición":"Sin tratamiento","Dureza (HRC)":None,"Origen":"Pendiente"},
        {"Probeta":"B","Condición":"Temple","Dureza (HRC)":None,"Origen":"Pendiente"},
        {"Probeta":"C","Condición":"Temple + revenido","Dureza (HRC)":None,"Origen":"Pendiente"},
        {"Probeta":"D","Condición":"Recocido","Dureza (HRC)":None,"Origen":"Pendiente"},
    ])
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.caption("La tabla es una plantilla. Completar únicamente con mediciones reales o datos de simulación debidamente documentados.")
