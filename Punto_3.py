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