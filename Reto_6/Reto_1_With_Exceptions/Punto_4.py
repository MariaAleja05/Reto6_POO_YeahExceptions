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