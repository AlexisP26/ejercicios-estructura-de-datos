#repaso de matrices
class producto:
    def __init__(self. nombre. precio. cantidad):
        self.nombre = nombre
        self.precio = precio 
        self.cantidad = cantidad

almacen= [[producto("aretes",5000, 50), producto("collares", 10000, 20)], [producto("manillas", 12000, 100), producto("anillos", 5000, 150)]]

def buscar_producto(matriz, nombre_a_buscar):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna].nombre ==nombre_a_buscar:
                return fila, columna
    return "producto no encontrado"        
