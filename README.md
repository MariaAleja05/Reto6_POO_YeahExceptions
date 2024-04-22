# Reto número 6 repo POO

 ### **Fecha:** 15-04-2024

**1.** Add the required exceptions in the Reto 1 code assigments.

- Basic operations:

  Look at the file: Punto_1.py

```python
suma = 0          # Variables are defined
resta = 0
divi = 0
multi = 0
num1 : float = 0
num2 : float = 0
operacion: str

def operaciones(num1, num2, operacion): # Function to perform the desired operation with user-defined values
    if operacion == "+":
        suma = num1 + num2
        print("The result of the addition is: " + str(suma))

    elif operacion == "-":
        resta = num1 - num2
        print("The result of the subtraction is: " + str(resta))

    elif operacion == "/":
        if num2 != 0:         # Perform division if the second number is not zero
            divi = num1 / num2
            print("The result of the division is: " + str(divi))
        else:                 # Cannot perform division if the second number is zero
            print("The numbers entered are not valid for the operation")

    elif operacion == "*":
        multi = num1 * num2
        print("The result of the multiplication is: " + str(multi))

# Exception handling
try:
    operacion = input("Enter '+' for addition, '-' for subtraction, '/' for division, '*' for multiplication: ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operaciones(num1, num2, operacion)    # Call the function to perform the calculation

except ValueError as error:             # Invalid value
    print(f"General error: {error}")
except ZeroDivisionError as error:      # Division by zero
    print(f"General error: {error}")
except Exception as error:              # Other exceptions
    print(f"General error: {error}")
```
- Palindrome:

  Look at the file: Punto_2.py

```python
palabra: str         # Variables are defined
palabra_min: str     
caracteres = []
longitud_palabra = 0
palabra_al_reves : str

def verificar_si_es_palíndromo(palabra): # Function to check if the entered word is a palindrome
    palabra_min = palabra.lower()
    longitud_palabra = len(palabra_min)
    
    for i in range (longitud_palabra - 1, -1, -1): # To reverse the entered word
        caracteres.append(palabra_min[i])
    
    palabra_al_reves = ''.join(caracteres)  # To join those reversed characters into a string

    for i in range(longitud_palabra):       # To check if the character at the location in the original and inverted word is the same
        if palabra_min[i]==palabra_al_reves[i]:
            continue
        else:
            print("The entered word is NOT a palindrome")
            return                          # Exit the loop since it found a letter that does not match
        
    print("The word " + "'" + palabra_min + "'" + " IS a palindrome")   # It will show that it is a palindrome

# Exception handling
try:
    palabra = input("Enter the word: ")
    if not palabra.isalpha():  # Check if the input contains only alphabetic characters
        raise ValueError
    verificar_si_es_palíndromo(palabra)    # Call the function to check if the entered word is a palindrome

except ValueError as error:             # Invalid value
    print(f"Error: Invalid input")
except Exception as error:              # Other exceptions
    print(f"Error: {error}")
```
  
- Prime numbers:

  Look at the file: Punto_3.py
  
```python
cantidad_numeros: int = 0       # Variables are defined
num: int = 0
contador_divisores: int = 0
lista_usuario = []
lista_primos = []

def verificar_si_es_primo(lista_usuario): # Function to check if the numbers are prime
    
    for i in lista_usuario:               # Loop to check if each number in the list is prime
        contador_divisores = 0            # To count the number of divisors, if it has more than 2 then it's not a prime number
        for j in range(1, i+1):           # It searches for all possible divisors from 1 up to that number being evaluated
            if i % j == 0:                # If it's divisible, the remainder is zero
                contador_divisores += 1   # If it's a divisor, add 1 to the counter
        if contador_divisores == 2:       # If the number has only 2 divisors, it's counted as a prime number
            lista_primos.append(i)        # Add the prime number to its corresponding list
    
    if len(lista_primos) != 0:            # If the length of the list is not zero, prime numbers entered will be shown
        print("The following numbers entered are prime: ")
        print(lista_primos)
    else:                                 # If the list of prime numbers has no elements, it means there are no prime numbers
        print("There are no prime numbers")

# Exception handling
try:
    cantidad_numeros = int(input("Enter the number of numbers in the list: "))
    for i in range(cantidad_numeros):      # A loop that repeats according to the number of numbers the user wants to enter
        num = int(input("Enter the integer number: "))
        lista_usuario.append(num)
    verificar_si_es_primo(lista_usuario)   # Call the function to check if the entered numbers are prime

except ValueError as error:             # Invalid value
    print(f"Error: {error}")
except Exception as error:              # Other exceptions
    print(f"Error: {error}")
```

- Greatest sum:

  Look at the file: Punto_4.py

```python
lista_usuario = []

def mayor_suma(lista_usuario): # Function to find the greatest sum between 2 consecutive numbers
    suma_actual = 0
    mayor_suma = 0
    for i in range (cantidad_numeros-1):          # It will repeat the number of entered numbers -1 because it's the number of consecutive pairs that can be formed
        suma_actual = lista_usuario[i] + lista_usuario[i+1]           # Sum the consecutive elements
        if mayor_suma >= suma_actual:               # If the value of greatest sum is greater than or equal to the sum performed, other pairs will continue to be checked to see if any is greater
            continue
        else:                                     # When a greater sum than the previous one is found, that new greater sum is set as the standard for comparison
            mayor_suma = suma_actual
    print("The greatest sum of 2 consecutive elements in the list is: " + str(mayor_suma))

# Exception handling
try:
    cantidad_numeros = int(input("Enter the number of numbers in the list: "))
    if cantidad_numeros <= 0:  # Check if the entered value for the number of numbers is non-positive
        raise ValueError("The number of numbers must be a positive integer.")
    for i in range(cantidad_numeros):      # A loop that repeats according to the number of numbers the user wants to enter
        num = int(input("Enter the integer number: "))
        lista_usuario.append(num)
    mayor_suma(lista_usuario)   # Call the function to find the greatest sum between 2 consecutive numbers

except ValueError as error:             # Invalid value
    print(f"Error: {error}")
except IndexError as error:             # List index out of range
    print(f"Error: {error}")
except Exception as error:              # Other exceptions
    print(f"Error: {error}")
```
  
- Same characters:

  Look at the file: Punto_5.py

```python

```

**2.** In the package Shape identify at least cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.

```python

```

* Mirar archivo
