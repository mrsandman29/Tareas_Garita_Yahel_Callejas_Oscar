def filtrar_vocales(cadena, bandera):
    error_tipo = -100
    error_letras= -200
    error_vacia= -300
    error_longitud=-400
    error_bandera=-500
    exito=0 

    if not isinstance(cadena,str): 
        return error_tipo, None
    if cadena == "":
        return error_vacia, None

    if len(cadena) > 30: 
        return error_longitud, None
    if not cadena.isalpha():
        return error_letras, None
    if not isinstance(bandera, bool):
        return error_bandera, None 
    
    vocales = "aeiouAEIOU"
    resultado = ""

    for letra in cadena:
        if bandera:
            if letra in vocales: 
                resultado += letra
        else: 
            if letra not in vocales: 
                resultado += letra
    return exito, resultado     
codigo, texto = filtrar_vocales("porro", False)    
print("Codigo:",codigo) 
print("Resultado:", texto) 


def encontrar_extremos(lista):
    error_tipo=-600
    error_num=-700
    error_vacia=-800
    error_longitud=-900
    exito=0
    if not isinstance(lista,list):
        return error_tipo,None ,None
    for i in lista:
        if not isinstance(i, (int,float)) or isinstance(i, bool):
             return error_num, None, None
    if len(lista) == 0:
        return error_vacia, None, None
       
    if len(lista) > 15:
        return error_longitud, None, None 
    return exito,min(lista),max(lista)
print(encontrar_extremos(1))