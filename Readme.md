### 📂 Archivo: `frontend/README.md`

# 🎨 Calculadora UI (Frontend)

Interfaz de usuario moderna e interactiva construida con **Streamlit** para interactuar con la API de la calculadora.

## 🚀 Funcionalidades
- **Interfaz Intuitiva:** Selección de operaciones mediante componentes visuales.
- **Persistencia Local:** Mantiene una sesión HTTP para mostrar el historial de operaciones del usuario actual.
- **Monitoreo en Tiempo Real:** Sidebar con el estado de conexión del backend.

## 🛠️ Requisitos
- Python 3.9+
- Streamlit
- Requests

## 🔧 Variables de Entorno
| Variable | Descripción |
| :--- | :--- |
| `BACKEND_URL` | Dirección URL donde se encuentra escuchando la API. |
| `API_AUTH_KEY` | Clave de autorización que debe coincidir con la del Backend. |

## 🚀 Ejecución Local
```bash
# Instalar dependencias
pip install streamlit requests

# Ejecutar aplicación
export BACKEND_URL="http://localhost:8000"
export API_AUTH_KEY="clave_api_local"
streamlit run app.py