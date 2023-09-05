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


