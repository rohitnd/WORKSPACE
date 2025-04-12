from zona_fit_db.cliente import Cliente
from zona_fit_db.cliente_dao import ClienteDAO

print('*** Clientes Zona Fit (GYM) ***')
opcion = None
while opcion != 5:
    print(f'''Menu:
    1. Listar clientes
    2. Agregar cliente
    3. Modificar cliente
    4. Eliminar cliente
    5. Salir''')
    opcion = int(input('Escribe tu opcion (1-5): '))
    if opcion == 1:  # Listar clientes
        clientes = ClienteDAO.seleccionar()
        print('\n*** Listado de Clientes ***')
        for cliente in clientes:
            print(cliente)
    elif opcion == 2:  # Agregar cliente
        nombre_var = input('Escribe el nombre: ')
        apellido_var = input('Escribe el apellido: ')
        membresia_var = input('Escribe la membresia: ')
        cliente = Cliente(nombre=nombre_var, apellido=apellido_var,
                          membresia=membresia_var)
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f'Clientes insertados: {clientes_insertados}')
