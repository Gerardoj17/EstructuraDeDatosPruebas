import datetime

class Cliente:
    def __init__(self, nombre, fecha, folio):
        self.nombre = nombre
        self.fecha = fecha
        self.folio = folio
        self.servicios = []
    
    def imprimir_info(self):
        print(f'Nombre: {self.nombre}\nFolio: {self.folio}\nFecha: {self.fecha}')
        
        
    def servicios_clientes(self):
        if len(self.servicios) > 0:
            print('Servicios:')
            for servicio in self.servicios:
                print(f'- {servicio[0]} (${servicio[1]})')
            total = sum([servicio[1] for servicio in self.servicios])
            print(f'Total: ${total}')
            print("")



clientes = []
clientes_eliminados = []
folio = 0

def agregarDatos():
    global folio
    nombre = input('Ingresa el nombre del usuario: ')
    fecha = datetime.date.today()
    folio += 1
    cliente = Cliente(nombre, fecha, folio)
    
    while True:
        servicio = input('Ingresa el nombre del servicio: ')
        monto = float(input('Ingresa el monto del servicio: '))
        cliente.servicios.append((servicio, monto))
        print("")
        print('**Servicio agregado**')
        print("")
        
        opcion = input('¿Deseas agregar otro servicio? (s/n): ')
        if opcion.lower() == 'n':
            break
        
    if len(cliente.servicios) > 0:
        clientes.append(cliente)
        print('Nota subida:)')
        print("")
    else:
        print('Debe seleccionar al menos un servicio')





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
            
def eliminar_cliente():
    print("Eliminar cliente")
    opc_folio = int(input("Ingrese el folio del cliente que desea eliminar: "))
    cliente_encontrado = False
    for cliente in clientes:
        if cliente.folio == opc_folio:
            cliente_encontrado = True
            print('Nota a eliminar:')
            cliente.imprimir_info()
            cliente.servicios_clientes()
            confirmacion = input('¿Está seguro de que desea eliminar esta nota? (s/n): ')
            if confirmacion.lower() == 's':
                clientes.remove(cliente)
                clientes_eliminados.append(cliente)
                print("Cliente eliminado")
                return
            else:
                print('La nota no fue cancelada')
                return
    if not cliente_encontrado:
        print("El cliente no existe")
            
            
def recuperar_nota():
    print("Recuperar nota")
    print('Notas eliminadas:')
    for cliente in clientes_eliminados:
        cliente.imprimir_info()
        print('')
    opc_folio = int(input("Ingresa el folio del cliente eliminado que deseas recuperar o 0 para no seleccionar ninguno: "))
    if opc_folio == 0:
        return
    cliente_encontrado = False
    for cliente in clientes_eliminados:
        if cliente.folio == opc_folio:
            cliente_encontrado = True
            print('Nota a recuperar:')
            cliente.imprimir_info()
            cliente.servicios_clientes()
            confirmacion = input('¿Está seguro de que desea recuperar esta nota? (s/n): ')
            if confirmacion.lower() == 's':
                clientes.append(cliente)
                clientes_eliminados.remove(cliente)
                print("Cliente recuperado")
                return
            else:
                print('Nota no recuperada')
                return
    if not cliente_encontrado:
        print("El cliente no existe")
        


        
    


while True:
    print('Bienvenido a GeraMotors')
    print('Elija una opción:')
    print("[1]. Registrar una nota")
    print("[2]. Consultas y reportes")
    print("[3]. Cancelar una nota")
    print("[4]. Recuperar una nota")
    print("[5]. Salir del sistema")
    opcion = int(input('Ingrese la opción que desea realizar: '))
    if opcion == 1:
        agregarDatos()
        
        
    elif opcion == 2:
        print("")
        print("[1]. Consultas por folio")
        print("[2]. Consultas por periodo")
        print("[3]. Salir del sistema")
        
        consulYreport = int(input("Metodo de consultas? \n"))
        if consulYreport==1:
            consulta()
        elif consulYreport==2:
            consultaPorFecha()
    
    elif opcion == 3:
        eliminar_cliente()
        
    elif opcion == 4:
        recuperar_nota()
        
    elif opcion==5:
        confirmacion = input('¿Esta seguro que desea salir del programa? (s/n): ')
        if confirmacion.lower() == 's':
            break
        