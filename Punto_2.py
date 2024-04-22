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