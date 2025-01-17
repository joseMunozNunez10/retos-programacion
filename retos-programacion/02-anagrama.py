
"""* Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama."""
 
 
def es_anagrama(palabra1, palabra2):   
    if palabra1 == palabra2:
        return False    
    return sorted(palabra1) == sorted(palabra2)


print(es_anagrama("amor", "roma"))  
print(es_anagrama("amor", "amor"))  
