lista_usuario = []
lista_copia = []
lista_palabras_repetidas = []
lista_mismos_caracteres = []

def igualdad_caracteres(lista_usuario, lista_copia, lista_palabras_repetidas, lista_mismos_caracteres): 
    for i in lista_usuario:             # Iterate over each word in the list
        i = ''.join(sorted(i))          # Sort the letters of the word in alphabetical order to make them easier to compare
        lista_copia.append(i)           # Add them to the list where all words with their letters in alphabetical order will be placed
           
    # This loop is to check for repeated words that by default will have the same characters
    for j in range(len(lista_usuario)): # Take the first word to compare
        for k in range(len(lista_usuario)): # Take the second word to compare
            if j == k:                  # Don't compare the word with itself
                continue
            else:
                if lista_usuario[j] == lista_usuario[k]:  # If there are two elements with the same characters 
                    if lista_usuario[j] in lista_palabras_repetidas:    # If it's not in the list, add it
                        continue
                    else:
                        lista_palabras_repetidas.append(lista_usuario[j])   # Add it to repeated words because it's not a new one

    # This loop is to check the words that remained with the characters sorted in alphabetical order
    # Same logic as the previous nested loop
    for i in range(len(lista_copia)):
        for k in range(len(lista_copia)):
            if i == k:
                continue
            else:
                if lista_copia[i] == lista_copia[k]:
                    if lista_usuario[i] in lista_mismos_caracteres:
                        continue
                    else:
                        lista_mismos_caracteres.append(lista_usuario[i])
        
    # Now both resulting lists from the previous loops are added together
    # The list of words that are written more than once and that by default have the same number of characters
    # The list of words that have the same characters without being repeated
    
    lista_mismos_caracteres = lista_mismos_caracteres + lista_palabras_repetidas
    
    print("The words with the same characters are: " + str(lista_mismos_caracteres))

# Exception handling
try:
    cantidad_palabras = int(input("Enter the number of words in the list: "))  
    if cantidad_palabras <= 0:  # Check if the entered value for the number of words is non-positive
        raise ValueError("The number of words must be a positive integer.")
    for i in range(cantidad_palabras):            # A loop that repeats according to the number of words the user wants to enter
        palabra = input("Enter the word: ")  
        lista_usuario.append(palabra)
    igualdad_caracteres(lista_usuario, lista_copia, lista_palabras_repetidas, lista_mismos_caracteres)     # Call the function

except ValueError as error:             # Invalid value
    print(f"Error: {error}")
except IndexError as error:             # List index out of range
    print(f"Error: {error}")
except Exception as error:              # Other exceptions
    print(f"Error: {error}")