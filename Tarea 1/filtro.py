def filtro_vocales(palabra, bandera):
    error_tipo = 1
    error_letras= 2
    error_vacia= 3
    error_longitud=4
    error_bandera=5
    exito=0 

    if not isinstance(palabra,str): 
        return error_tipo, None
    if palabra == "":
        return error_vacia, None

    if len(palabra) > 30: 
        return error_longitud, None
    if not palabra.isalpha():
        return error_letras, None
    if not isinstance(bandera, bool):
        return error_bandera, None 
    
    vocales = "aeiouAEIOU"
    resultado = ""

    for letra in palabra:
        if bandera:
            if letra in vocales: 
                resultado += letra
        else: 
            if letra not in vocales: 
                resultado += letra
    return exito, resultado     
codigo, texto = filtro_vocales("porro", False)    
print("Codigo:",codigo) 
print("Resultado:", texto) 