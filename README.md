# Reto número 6 repo POO

 ### **Fecha:** 15-04-2024

**1.** Add the required exceptions in the Reto 1 code assigments.

- Basic operations:

  Mirar archivo: Punto_1.py

```python
suma = 0          # Se definen variables
resta = 0
divi = 0
multi = 0
num1 : float = 0
num2 : float = 0
operacion: str

def operaciones(num1, num2, operacion): # Función para realizar la operación deseada, con valores de entrega establecidos por el usuario
    if operacion == "+":
        suma = num1 + num2
        print("El resultado de la suma es: " + str(suma))

    elif operacion == "-":
        resta = num1 - num2
        print("El resultado de la resta es: " + str(resta))

    elif operacion == "/":
        if num2 != 0:         # Si se puede realizar la división cuando el segundo número es diferente de cero
            divi = num1 / num2
            print("El resultado de la división es: " + str(divi))
        else:                 # No se puede realizar la división cuando el segundo número es cero
            print("Los números ingresados no son válidos para realizar la operación")

    elif operacion == "*":
        multi = num1 * num2
        print("El resultado de la multiplicación es: " + str(multi))
# Manejo excepciones
try:
    operacion = input("Ingrese '+' si desea realizar una suma; '-' si desea realizar una resta; '/' si desea realizar una división; '*' si desea realizar una multiplicación: ")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operaciones(num1, num2, operacion)    # Se llama la función operaciones para que se realice el calculo entre los números

except ValueError as error:             # Valor no valido
    print(f"Error general: {error}")
except ZeroDivisionError as error:      # División por cero
    print(f"Error general: {error}")
except Exception as error:              # Otras excepciones
    print(f"Error general: {error}")
```
- Palindrome:

  Mirar archivo: Punto_2.py

```python

```
  
- Prime numbers:

  Mirar archivo: Punto_3.py

```python

```
   
- Greatest sum:

  Mirar archivo: Punto_4.py

```python

```
  
- Same characters:

  Mirar archivo: Punto_5.py

```python

```

**2.** In the package Shape identify at least cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.

```python

```

* Mirar archivo
