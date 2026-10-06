import configuration
import requests
import data

def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )
# === CASO 10 ===
# print("📋 Prueba 10: Otro tipo de parámetro...")
# respuesta = post_new_user(data.user_body_number_type)
# print("Código:", respuesta.status_code)
# print("Respuesta:", respuesta.json())

## 1. Verificar que el archivo es rastreado por Git
git ls-files README.md

# 2. Ver el estado — debe mostrar si hay cambios para confirmar
git status

# 3. Verificar que ya está registrado en el repositorio
git log --oneline -- README.md

# 4. Ver el contenido que Git tiene guardado
git show HEAD:README.md