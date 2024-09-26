import streamlit as st

# Función de saludo simple (Ejercicio 1)
def saludar(nombre):
    # Retorna un saludo personalizado con el nombre ingresado
    return f"Hola, {nombre}!"

# Función sumar (Ejercicio 2)
def sumar(a, b):
    # Retorna la suma de dos números
    return a + b

# Función calcular área del triángulo (Ejercicio 3)
def calcular_area_triangulo(base, altura):
    # Retorna el área del triángulo utilizando la fórmula 0.5 * base * altura
    return 0.5 * base * altura

# Función calcular precio final (Ejercicio 4)
def calcular_precio_final(precio_original, descuento=10, impuesto=16):
    # Calcula el precio final con descuento e impuesto
    precio_descuento = precio_original - (precio_original * (descuento / 100))
    precio_final = precio_descuento + (precio_original * (impuesto / 100))
    return precio_final

# Función sumar lista (Ejercicio 5)
def sumar_lista(lista_numeros):
    # Inicializa la suma en 0
    suma = 0
    # Itera sobre la lista de números y suma cada elemento
    for numero in lista_numeros:
        suma += numero
    return suma

# Función producto (Ejercicio 6)
def producto(nombre_producto, cantidad=1, precio_unidad=10):
    # Retorna el precio total del producto
    return cantidad * precio_unidad

# Función números pares e impares (Ejercicio 7)
def numeros_pares_e_impares(lista_numeros):
    # Inicializa listas vacías para números pares e impares
    pares = []
    impares = []
    # Itera sobre la lista de números y clasifica cada elemento como par o impar
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

# Función multiplicar todos (Ejercicio 8)
def multiplicar_todos(*args):
    # Inicializa el resultado en 1
    resultado = 1
    # Itera sobre los argumentos y multiplica cada elemento
    for numero in args:
        resultado *= numero
    return resultado

# Función información personal (Ejercicio 9)
def informacion_personal(**kwargs):
    # Itera sobre los argumentos clave-valor y muestra la información personal
    for clave, valor in kwargs.items():
        st.write(f"{clave.capitalize()}: {valor}")

# Función calculadora flexible (Ejercicio 10)
def calculadora_flexible(num1, num2, operacion="suma"):
    # Define un diccionario de operaciones
    operaciones = {
        "suma": num1 + num2,
        "resta": num1 - num2,
        "multiplicacion": num1 * num2,
        "division": num1 / num2 if num2 != 0 else "Error: División por cero"
    }
    # Retorna el resultado de la operación seleccionada
    return operaciones.get(operacion, "Error: Operación no válida")

# Crear pestañas para separar los ejercicios
st.title("Tablero interactivo")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["Ejercicio 1: Saludo", "Ejercicio 2: Sumar", "Ejercicio 3: Área del Triángulo", "Ejercicio 4: Calculadora de descuento", "Ejercicio 5: Suma de lista", "Ejercicio 6: Producto", "Ejercicio 7: Números pares e impares", "Ejercicio 8: Multiplicar todos", "Ejercicio 9: Información personal", "Ejercicio 10: Calculadora flexible"])

# Ejercicio 1: Saludo
with tab1:
    st.title("Ejercicio 1: Función de saludo simple")
    nombre = st.text_input("Ingrese su nombre:", key="saludo_nombre")
    if nombre:
        resultado = saludar(nombre)
        st.write(resultado)

# Ejercicio 2: Sumar
with tab2:
    st.title("Ejercicio 2: Función sumar")
    num1 = st.number_input("Ingrese el primer número:", key="num1_sumar")
    num2 = st.number_input("Ingrese el segundo número:", key="num2_sumar")
    if num1 and num2:
        resultado = sumar(num1, num2)
        st.write(f"La suma de {num1} y {num2} es {resultado}")

# Ejercicio 3: Área del Triángulo
with tab3:
    st.title("Ejercicio 3: Área del Triángulo")
    base = st.number_input("Ingrese la base del triángulo:")
    altura = st.number_input("Ingrese la altura del triángulo:")
    if base and altura:
        resultado = calcular_area_triangulo(base, altura)
        st.write(f"El área del triángulo es {resultado}")

# Ejercicio 4: Calculadora de descuento
with tab4:
    st.title("Ejercicio 4: Calculadora de descuento")
    precio_original = st.number_input("Ingrese el precio original del producto:")
    descuento = st.number_input("Ingrese el porcentaje de descuento (Por defecto 10%):", value=10)
    impuesto = st.number_input("Ingrese el impuesto (Por defecto 16%):", value=16)
    if precio_original:
        resultado = calcular_precio_final(precio_original, descuento, impuesto)
        st.write(f"El precio final del producto es {resultado}")

# Ejercicio 5: Suma de lista
with tab5:
    st.title("Ejercicio 5: Suma de lista")
    lista_numeros = st.text_input("Ingrese la lista de números separados por comas:", key="suma_lista_numeros")
    if lista_numeros:
        try:
            lista_numeros = [float(x) for x in lista_numeros.split(",")]
            resultado = sumar_lista(lista_numeros)
            st.write(f"La suma de la lista es {resultado}")
        except ValueError:
            st.error("Error: La lista debe contener solo números separados por comas.")

# Ejercicio 6: Producto
with tab6:
    st.title("Ejercicio 6: Producto")
    nombre_producto = st.text_input("Ingrese el nombre del producto:")
    cantidad = st.number_input("Ingrese la cantidad (Por defecto 1):", value=1)
    precio_unidad = st.number_input("Ingrese el precio por unidad (Por defecto 10):", value=10)
    if nombre_producto:
        resultado = producto(nombre_producto, cantidad, precio_unidad)
        st.write(f"El precio total a pagar de {nombre_producto} es {resultado}")

# Ejercicio 7: Números pares e impares
with tab7:
    st.title("Ejercicio 7: Números pares e impares")
    lista_numeros = st.text_input("Ingrese la lista de números separados por comas:", key="numeros_pares_impares_lista_numeros")
    if lista_numeros:
        try:
            lista_numeros = [int(x) for x in lista_numeros.split(",")]
            pares, impares = numeros_pares_e_impares(lista_numeros)
            st.write(f"Los números pares son: {pares}")
            st.write(f"Los números impares son: {impares}")
        except ValueError:
            st.error("Error: La lista debe contener solo números enteros separados por comas.")

# Ejercicio 8: Multiplicar todos
with tab8:
    st.title("Ejercicio 8: Multiplicar todos")
    numeros = st.text_input("Ingrese los números separados por comas:", key="multiplicar_todos_numeros")
    if numeros:
        try:
            numeros = [float(x) for x in numeros.split(",")]
            resultado = multiplicar_todos(*numeros)
            st.write(f"El resultado de multiplicar todos los números es {resultado}")
        except ValueError:
            st.error("Error: La lista debe contener solo números separados por comas.")

# Ejercicio 9: Información personal
with tab9:
    st.title("Ejercicio 9: Información personal")
    nombre = st.text_input("Ingrese su nombre:")
    edad = st.number_input("Ingrese su edad:")
    direccion = st.text_input("Ingrese su dirección:")
    telefono = st.text_input("Ingrese su teléfono:")
    if nombre:
        informacion_personal(nombre=nombre, edad=edad, direccion=direccion, telefono=telefono)

# Ejercicio 10: Calculadora flexible
with tab10:
    st.title("Ejercicio 10: Calculadora flexible")
    num1 = st.number_input("Ingrese el primer número:")
    num2 = st.number_input("Ingrese el segundo número:")
    operacion = st.selectbox("Seleccione la operación:", ["suma", "resta", "multiplicacion", "division"])
    if num1 and num2:
        resultado = calculadora_flexible(num1, num2, operacion)
        st.write(f"El resultado de la operación {operacion} es {resultado}")