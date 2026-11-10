# LABSTEEL 3D — prototipo inicial

Aplicación educativa en Python + Streamlit para organizar simulaciones y datos de tratamientos térmicos del acero.

## 1. Requisitos
- Python 3.10 o superior
- Conexión a internet para instalar dependencias

## 2. Instalación local
Abre una terminal dentro de la carpeta del proyecto y ejecuta:

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS / Linux:
```bash
source .venv/bin/activate
```

Instala las dependencias y ejecuta:

```bash
pip install -r requirements.txt
streamlit run app.py
```

La aplicación se abrirá en el navegador, normalmente en `http://localhost:8501`.

## 3. Publicación en línea
Una opción sencilla es publicar el repositorio en GitHub y desplegarlo en Streamlit Community Cloud:
1. Crear un repositorio y subir `app.py` y `requirements.txt`.
2. Entrar a https://share.streamlit.io/ e iniciar sesión.
3. Crear una aplicación indicando repositorio, rama y `app.py`.
4. Publicar y compartir el enlace generado.

No subir datos personales ni credenciales al repositorio.

## 4. Alcance científico de esta versión
- La probeta 3D es una representación geométrica conceptual.
- El registro del ciclo térmico no calcula todavía transformaciones de fase.
- El módulo de dureza calcula la variación porcentual a partir de valores introducidos.
- Los valores de demostración están identificados como ficticios.
- No reemplaza un horno, durómetro, máquina de tracción ni análisis metalográfico real.

## 5. Próximas etapas
1. Definir acero, composición y condición inicial usando fichas técnicas verificables.
2. Incorporar curvas de calentamiento y enfriamiento con parámetros editables.
3. Añadir modelos metalúrgicos adecuados (TTT/CCT y transformaciones) con fuentes.
4. Añadir ensayo Rockwell y conversión de escalas solo bajo normas aplicables.
5. Implementar ensayo de tracción y exportación CSV/PDF.
6. Mejorar escena 3D con Three.js y animación del horno/probeta.
7. Validar los resultados contra bibliografía, normas y ensayos físicos.
