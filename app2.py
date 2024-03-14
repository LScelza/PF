import streamlit as st
import requests

# URL de tu función en la nube
cloud_function_url = "https://us-central1-silicon-carver-416314.cloudfunctions.net/Prueba"

# Definir los parámetros específicos para cada modelo
modelo_params = {
    "Predicción del cargo por tráfico": ["Zona de inicio", "Zona de finalización", "Distancia estimada", "Tiempo estimado"],
    "Predicción de tarifa": ["Tiempo estimado", "Distancia estimada"]}

# Definir una función para realizar la solicitud HTTPS
def invoke_cloud_function(params, selected_modelo):
    try:
        data = {
            "selected_modelo": selected_modelo,
            "modelo_params": params
        }
        response = requests.post(cloud_function_url, json=data)
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            st.write("La función se activó con éxito. Predicción:", prediction)
        else:
            st.write("Error al activar la función:", response.status_code)
    except Exception as e:
        st.write("Error:", e)

# Interfaz de usuario en Streamlit
def main():
    st.title("Activar función en la nube")
    st.write("Selecciona un modelo y ajusta los parámetros para la predicción:")
    
    modelos = list(modelo_params.keys())
    selected_modelo = st.selectbox("Selecciona el modelo", modelos)
    
    params = {}
    for param_name in modelo_params[selected_modelo]:
        params[param_name] = st.text_input(f"{param_name}", "")
    
    if st.button("Activar Función"):
        invoke_cloud_function(params, selected_modelo)

if __name__ == "__main__":
    main()
