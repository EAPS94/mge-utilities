# 📌 mge-utilities

## 📖 Descripción

`mge-utilities` es un conjunto de utilidades diseñadas para el **manejo de datos y evaluación de modelos de Machine Learning**. Contiene funciones optimizadas para limpieza, codificación de variables, selección de características y métricas de evaluación de modelos. Su objetivo es facilitar el flujo de trabajo en proyectos de ciencia de datos.

---

## 📂 **Estructura del Proyecto**
```bash
mge-utilities/
│── src/                      # Código fuente del proyecto
│   ├── utilities/            # Módulos de utilidades
│   │   ├── __init__.py       # Inicializa el paquete utilities
│   │   ├── data_utils.py     # Funciones de limpieza y preprocesamiento
│   │   ├── model_utils.py    # Funciones de evaluación de modelos
│
│── docs/                     # Documentación generada con Sphinx
│   ├── build/                # Archivos HTML generados (no incluir en Git)
│   ├── source/               # Archivos fuente de la documentación
│   │   ├── conf.py           # Configuración de Sphinx
│   │   ├── index.rst         # Página principal de la documentación
│   │   ├── modules.rst       # Lista de módulos documentados
│   │   ├── utilities.rst     # Documentación específica de utilities/
│   ├── Makefile              # Generador de documentación en Linux/macOS
│   ├── make.bat              # Generador de documentación en Windows
│
│── tests/                    # Pruebas unitarias del código (opcional)
│── README.md                 # Este archivo
│── .gitignore                # Archivos que Git debe ignorar
│── requirements.txt          # Lista de dependencias del proyecto
```
---

## 🚀 Instalación

### **Requisitos Previos**
Antes de instalar, asegúrate de tener instalado:
- **Python 3.8 o superior**
- **pip** (administrador de paquetes de Python)
- **Git** (para clonar el repositorio si es necesario)

### **Pasos de Instalación**
1. **Clonar el repositorio** desde GitHub o descargar el código manualmente.
2. **Crear y activar un entorno virtual** para evitar conflictos de dependencias.
3. **Instalar las dependencias necesarias** con `pip`.

Para más detalles sobre la instalación, revisa la documentación oficial del proyecto.

---

## 📜 Uso

El proyecto proporciona funciones clave para:
- **Limpieza de datos:** Eliminación de columnas irrelevantes y manejo de valores nulos.
- **Codificación de variables categóricas:** Conversión de variables de texto en valores numéricos.
- **Selección de características:** Identificación de las variables más relevantes para el modelo.
- **Evaluación de modelos:** Métricas como MAE y RMSE para medir el rendimiento de modelos de Machine Learning.

Para ejemplos detallados sobre el uso de estas funciones, consulta la documentación generada con **Sphinx**.

---

## 📖 Generar y Visualizar la Documentación en HTML

La documentación del proyecto está escrita en **Sphinx**. Para generar y visualizar la documentación en formato HTML, sigue estos pasos:

### **1️⃣ Generar la Documentación**
Ejecuta los siguientes comandos desde la carpeta `docs/`:

```bash
cd docs
sphinx-apidoc -o source/ ../src/
make html  # En macOS/Linux
.\make.bat html  # En Windows
```
### **2️⃣ Abrir la Documentación Generada**
Una vez generada la documentación, puedes abrirla en tu navegador con:

```bash
start build/html/index.html  # En Windows
open build/html/index.html  # En macOS/Linux
```
### 3️⃣ Solución a Errores Comunes
Si la documentación no se genera correctamente:

- Verifica que Sphinx está instalado:

```bash
pip install sphinx
```

- Asegúrate de estar en la carpeta docs/ antes de ejecutar make html.
- Si hay problemas con make.bat, prueba este comando en su lugar:

```bash
sphinx-build -b html source build/html
```
---