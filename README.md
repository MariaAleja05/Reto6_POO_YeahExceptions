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

```
  
- Prime numbers:

  Look at the file: Punto_3.py

```python

```
   
- Greatest sum:

  Look at the file: Punto_4.py

```python

```
  
- Same characters:

  Look at the file: Punto_5.py

```python

```

**2.** In the package Shape identify at least cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.

```python

```

* Mirar archivo
