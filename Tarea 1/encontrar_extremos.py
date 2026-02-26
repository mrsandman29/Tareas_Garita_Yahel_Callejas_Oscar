def encontrar_extremos(lista):
    error_tipo=1
    error_num=2
    error_vacia=3
    error_longitud=4
    exito=0
    if not isinstance(lista,list):
        return error_tipo,None ,None
    for i in lista:
        if not isinstance(i, (int,float)):
             return error_num, None, None
    if len(lista) == 0:
        return error_vacia, None, None
       
    if len(lista) > 15:
        return error_longitud, None, None 
    return exito,min(lista),max(lista)
print(encontrar_extremos(1))


    