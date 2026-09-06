# Encabezados: le dicen al servidor que enviamos JSON
headers = {
    "Content-Type": "application/json"
}

# Datos para crear un usuario
user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

# IDs de productos para buscar kits
product_ids = {
    "ids": [1, 2, 3]
}
# Caso 1: 2 caracteres → VÁLIDO
user_body_2chars = {
    "firstName": "Aa",
    "phone": "+1234567890",
    "address": "123 Elm Street, Hilltop"
}
# Caso 2: 15 caracteres → VÁLIDO
user_body_15chars = {
    "firstName": "Aaaaaaaaaaaaaaa",
    "phone": "+521234567890",
    "address": "123 Elm Street, Hilltop"
}
# Caso 3: 1 carácter → INVÁLIDO
user_body_1char = {
    "firstName": "A",
    "phone": "+521234567890",
    "address": "123 Elm Street, Hilltop"
}
# Caso 4: 16 caracteres → excede el límite → INVÁLIDO
user_body_16chars = {
    "firstName": "Aaaaaaaaaaaaaaaa",   # 16 caracteres
    "phone": "+1234567890",            # ✅ El que dice tu guía
    "address": "123 Elm Street, Hilltop"
}
# Caso 5: Nombre CON ESPACIO → No se permiten espacios → INVÁLIDO
user_body_with_space = {
    "firstName": "A Aaa",
    "phone": "+1234567890",
    "address": "123 Elm Street, Hilltop"
}
# Caso 6: Caracteres especiales → INVÁLIDO
user_body_special = {
    "firstName": "Nº%@",
    "phone": "+1234567890",
    "address": "123 Elm Street, Hilltop"
}
# Caso 7: No se permiten números → INVÁLIDO
user_body_numbers = {
    "firstName": "123",
    "phone": "+1234567890",
    "address": "123 Elm Street, Hilltop"
}
# Caso 8: Falta el parámetro firstName → INVÁLIDO
user_body_no_name = {
    "phone": "+1234567890",
    "address": "123 Elm Street, Hilltop"
}
# Caso 9: Valor de parámetro vacío → INVÁLIDO
user_body_empty_name = {
    "firstName": "",
    "phone": "+1234567890",
    "address": "123 Elm Street, Hilltop"
}
# Caso 10: firstName con tipo de dato incorrecto (número) → INVÁLIDO
user_body_number_type = {
    "firstName": 12,          # ⚠️ SIN comillas: es número, NO texto
    "phone": "+1234567890",
    "address": "123 Elm Street, Hilltop"
}
user_body = {
    "firstName": "Ana",
    "email": "prueba@ejemplo.com",
    "password": "123456"
}
