import streamlit as st
import requests

# URL de tu función en la nube
cloud_function_url = "https://us-central1-silicon-carver-416314.cloudfunctions.net/Prueba"

# Definir los parámetros específicos para cada modelo
modelo_params = {
    "Modelo 1": ["param1_modelo1", "param2_modelo1", "param3_modelo1", "param4_modelo1"],
    "Modelo 2": ["param1_modelo2", "param2_modelo2", "param3_modelo2", "param4_modelo2"],
    "Modelo 3": ["param1_modelo3", "param2_modelo3", "param3_modelo3", "param4_modelo3"]
}

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
