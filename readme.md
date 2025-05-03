# Análisis Básico de Ventas

Esta es una aplicación interactiva desarrollada con **Streamlit** para explorar y analizar datos de ventas. Permite filtrar los datos por categoría y rango de precios, y muestra estadísticas clave como el total de ventas y el precio promedio.

## 📂 Estructura del proyecto

├── static/datasets/ sales_data.csv
├── app.py
└── README.md

## 🚀 Cómo ejecutar la aplicación

1️⃣ **Clonar el repositorio:**

```bash
git clone https://github.com/tu_usuario/analisis-ventas.git
cd analisis-ventas
```

2️⃣ **Instalar dependencias:**

Recomendado usar un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3️⃣ **Ejecutar la aplicación:**

```bash

streamlit run app.py
```

📊 **¿Qué hace la app?**
Carga de datos:
Lee el archivo sales_data.csv y muestra la tabla completa.

**Filtros:**

Seleccionar categoría: Electronics, Accessories o todas.

Elegir un rango de precios usando un control deslizante.

**Datos filtrados:**

Tabla filtrada en tiempo real.

Muestra la cantidad de registros encontrados.

**Estadísticas clave:**

Total de Ventas (suma de la columna Total_Sales).

Precio Promedio (media de la columna Price).

**📑 Formato del CSV esperado**
El archivo sales_data.csv debe incluir al menos las siguientes columnas:
| Column Name   | Descripción                                             |
| ------------- | ------------------------------------------------------- |
| `Category`    | Categoría del producto (e.g., Electronics, Accessories) |
| `Price`       | Precio unitario del producto                            |
| `Total_Sales` | Valor total de la venta (precio x cantidad vendida)     |

Ejemplo:

| Category    | Price  | Total\Sales |
| ----------- | ------ | ------------ |
| Electronics | 150.00 | 3000.00      |
| Accessories | 25.00  | 500.00       |

**Exportar datos filtrados.**

Filtros avanzados (por fecha o región).

🛠 **Tecnologías usadas**
Streamlit

Pandas
