def consulta():
    folio = int(input('Ingresa el folio de la nota que deseas ver: '))
    print("")
    nota_encontrada = False
    for cliente in clientes:
        if cliente.folio == folio:
            cliente.imprimir_info()
            cliente.servicios_clientes()
            nota_encontrada=True
            print("")
            return
    if nota_encontrada==False:
        print('**Esta nota no se encuentra en el sistema**')
        print("")
            
            
def consultaPorFecha():
    fecha_inicio = input('Ingresa la fecha de inicio (YYYY-MM-DD): ')
    fecha_fin = input('Ingresa la fecha de fin (YYYY-MM-DD): ')
    print("")
    fecha_encontrada=False
    for cliente in clientes:
        if fecha_inicio <= str(cliente.fecha) <= fecha_fin:
            cliente.imprimir_info()
            print('')
            fecha_encontrada = True
    if fecha_encontrada==False:
        print('**No se encontro ninguna nota en este lapso de tiempo**')
        print("")
            
