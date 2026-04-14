"""
APLICACIÓN DE ADMINISTRACIÓN DE INVENTARIO
Estructuras de Datos: Arreglos, Listas Enlazadas, Pilas, Colas, Árbol Binario de Búsqueda
"""

import copy
from collections import deque

# ==================== CLASE PRODUCTO ====================
class Producto:
    """Representa un producto del inventario"""
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def __str__(self):
        return f"Código: {self.codigo} | {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"
    
    def __repr__(self):
        return self.__str__()

# ==================== 1. ARREGLOS ====================
class InventarioArreglo:
    """Gestión de inventario usando arreglos (listas de Python)"""
    
    def __init__(self):
        self.productos = []  # Arreglo de productos
    
    def cargar_inicial(self, productos):
        """Carga un listado inicial de productos"""
        self.productos = productos
    
    def ordenar_alfabeticamente(self):
        """Ordena los productos alfabéticamente por nombre"""
        self.productos.sort(key=lambda p: p.nombre)
        print("✓ Inventario ordenado alfabéticamente")
    
    def ordenar_por_precio(self):
        """Ordena los productos por precio (ascendente)"""
        self.productos.sort(key=lambda p: p.precio)
        print("✓ Inventario ordenado por precio")
    
    def mostrar(self):
        """Muestra todos los productos"""
        if not self.productos:
            print("  Inventario vacío")
            return
        print("\n--- INVENTARIO (ARREGLO) ---")
        for p in self.productos:
            print(f"  {p}")
        print(f"  Total: {len(self.productos)} productos\n")
    
    def obtener_todos(self):
        return self.productos.copy()

# ==================== 2. LISTA ENLAZADA ====================
class Nodo:
    """Nodo para lista enlazada"""
    def __init__(self, producto):
        self.producto = producto
        self.siguiente = None

class ListaEnlazada:
    """Lista enlazada para gestión dinámica de productos"""
    
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0
    
    def agregar(self, producto):
        """Agrega un producto al final de la lista"""
        nuevo_nodo = Nodo(producto)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.tamanio += 1
        print(f"✓ Producto {producto.nombre} agregado a la lista enlazada")
    
    def eliminar(self, codigo):
        """Elimina un producto por su código"""
        if not self.cabeza:
            print("✗ Lista vacía, no se puede eliminar")
            return False
        
        if self.cabeza.producto.codigo == codigo:
            self.cabeza = self.cabeza.siguiente
            self.tamanio -= 1
            print(f"✓ Producto con código {codigo} eliminado")
            return True
        
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.producto.codigo != codigo:
            actual = actual.siguiente
        
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
            self.tamanio -= 1
            print(f"✓ Producto con código {codigo} eliminado")
            return True
        
        print(f"✗ Producto con código {codigo} no encontrado")
        return False
    
    def buscar_por_codigo(self, codigo):
        """Búsqueda lineal por código en la lista enlazada"""
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.producto.codigo == codigo:
                print(f"✓ Producto encontrado en posición {posicion}: {actual.producto}")
                return actual.producto
            actual = actual.siguiente
            posicion += 1
        print(f"✗ Producto con código {codigo} no encontrado")
        return None
    
    def mostrar(self):
        """Muestra todos los productos de la lista enlazada"""
        if not self.cabeza:
            print("  Lista enlazada vacía")
            return
        print("\n--- LISTA ENLAZADA (Productos) ---")
        actual = self.cabeza
        while actual:
            print(f"  {actual.producto}")
            actual = actual.siguiente
        print(f"  Total: {self.tamanio} productos\n")

# ==================== 3. PILA (Historial y Deshacer) ====================
class PilaHistorial:
    """Pila para almacenar historial de operaciones (LIFO)"""
    
    def __init__(self, capacidad_maxima=10):
        self.pila = []
        self.capacidad_maxima = capacidad_maxima
    
    def push(self, operacion):
        """Agrega una operación al historial"""
        self.pila.append(operacion)
        # Mantener solo las últimas 10 operaciones
        if len(self.pila) > self.capacidad_maxima:
            self.pila.pop(0)
        print(f"  Historial: Se agregó '{operacion['tipo']}'")
    
    def pop(self):
        """Elimina y retorna la última operación"""
        if self.pila:
            return self.pila.pop()
        return None
    
    def deshacer(self):
        """Deshace la última operación"""
        operacion = self.pop()
        if operacion:
            print(f"\n↩️ DESHACIENDO: {operacion['tipo']}")
            print(f"   Detalle: {operacion['detalle']}")
            return operacion
        else:
            print("✗ No hay operaciones para deshacer")
            return None
    
    def mostrar(self):
        """Muestra el historial de operaciones"""
        if not self.pila:
            print("  Historial vacío")
            return
        print("\n--- HISTORIAL (Últimas operaciones) ---")
        for i, op in enumerate(reversed(self.pila), 1):
            print(f"  {i}. {op['tipo']}: {op['detalle']}")
        print()

# ==================== 4. COLA (Pedidos de clientes FIFO) ====================
class Pedido:
    """Representa un pedido de un cliente"""
    def __init__(self, id_cliente, productos_solicitados):
        self.id_cliente = id_cliente
        self.productos_solicitados = productos_solicitados  # Lista de (codigo, cantidad)
    
    def __str__(self):
        return f"Cliente {self.id_cliente}: {len(self.productos_solicitados)} productos"

class ColaPedidos:
    """Cola para atender pedidos FIFO"""
    
    def __init__(self):
        self.cola = deque()  # deque para cola eficiente
    
    def agregar_pedido(self, pedido):
        """Agrega un pedido al final de la cola"""
        self.cola.append(pedido)
        print(f"✓ Pedido del {pedido} agregado a la cola")
    
    def atender_siguiente(self):
        """Atiende al siguiente cliente en la cola"""
        if self.cola:
            pedido = self.cola.popleft()
            print(f"\n ATENDIENDO: {pedido}")
            print(f"   Productos solicitados:")
            for codigo, cantidad in pedido.productos_solicitados:
                print(f"     - Código {codigo}: {cantidad} unidades")
            return pedido
        else:
            print("No hay pedidos en la cola")
            return None
    
    def mostrar(self):
        """Muestra los pedidos pendientes"""
        if not self.cola:
            print("  Cola de pedidos vacía")
            return
        print("\n--- COLA DE PEDIDOS (FIFO) ---")
        for i, pedido in enumerate(self.cola, 1):
            print(f"  {i}. {pedido}")
        print(f"  Total pedidos pendientes: {len(self.cola)}\n")

# ==================== 5. ÁRBOL BINARIO DE BÚSQUEDA ====================
class NodoABB:
    """Nodo para Árbol Binario de Búsqueda"""
    def __init__(self, producto, criterio="codigo"):
        self.producto = producto
        self.criterio = criterio  # "codigo" o "nombre"
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    """Árbol Binario de Búsqueda para productos"""
    
    def __init__(self, criterio="codigo"):
        self.raiz = None
        self.criterio = criterio  # "codigo" o "nombre"
    
    def _obtener_valor(self, producto):
        """Obtiene el valor de comparación según el criterio"""
        if self.criterio == "codigo":
            return producto.codigo
        else:
            return producto.nombre.lower()
    
    def insertar(self, producto):
        """Inserta un producto en el ABB"""
        if not self.raiz:
            self.raiz = NodoABB(producto, self.criterio)
            print(f"✓ Producto {producto.nombre} insertado en ABB (por {self.criterio})")
            return
        
        actual = self.raiz
        while True:
            valor_actual = self._obtener_valor(actual.producto)
            valor_nuevo = self._obtener_valor(producto)
            
            if valor_nuevo < valor_actual:
                if actual.izquierdo is None:
                    actual.izquierdo = NodoABB(producto, self.criterio)
                    print(f"✓ Producto {producto.nombre} insertado en ABB")
                    break
                actual = actual.izquierdo
            elif valor_nuevo > valor_actual:
                if actual.derecho is None:
                    actual.derecho = NodoABB(producto, self.criterio)
                    print(f"✓ Producto {producto.nombre} insertado en ABB")
                    break
                actual = actual.derecho
            else:
                print(f"Producto ya existe en el árbol (valor duplicado)")
                break
    
    def buscar(self, valor_buscado):
        """Busca un producto por código o nombre según el criterio"""
        actual = self.raiz
        comparaciones = 0
        
        while actual:
            comparaciones += 1
            valor_actual = self._obtener_valor(actual.producto)
            
            if valor_buscado == valor_actual:
                print(f"Producto encontrado después de {comparaciones} comparaciones: {actual.producto}")
                return actual.producto
            elif valor_buscado < valor_actual:
                actual = actual.izquierdo
            else:
                actual = actual.derecho
        
        print(f"Producto con {self.criterio} = {valor_buscado} no encontrado después de {comparaciones} comparaciones")
        return None
    
    def recorrido_inorden(self, nodo=None, resultado=None):
        """Recorrido inorden (izquierda - raíz - derecha) -> ordenado"""
        if resultado is None:
            resultado = []
        if nodo is None:
            nodo = self.raiz
        
        if nodo:
            self.recorrido_inorden(nodo.izquierdo, resultado)
            resultado.append(nodo.producto)
            self.recorrido_inorden(nodo.derecho, resultado)
        
        return resultado
    
    def mostrar(self):
        """Muestra los productos en orden (inorden)"""
        if not self.raiz:
            print(f"  Árbol vacío (criterio: {self.criterio})")
            return
        productos_ordenados = self.recorrido_inorden()
        print(f"\n--- ÁRBOL BINARIO DE BÚSQUEDA (Inorden - ordenado por {self.criterio}) ---")
        for p in productos_ordenados:
            print(f"  {p}")
        print(f"  Total: {len(productos_ordenados)} productos\n")

# ==================== APLICACIÓN PRINCIPAL ====================
class AplicacionInventario:
    """Aplicación principal que integra todas las estructuras"""
    
    def __init__(self):
        # Inicializar todas las estructuras
        self.inventario_arr = InventarioArreglo()
        self.lista_enlazada = ListaEnlazada()
        self.historial = PilaHistorial(capacidad_maxima=10)
        self.cola_pedidos = ColaPedidos()
        self.abb_codigo = ArbolBinarioBusqueda(criterio="codigo")
        self.abb_nombre = ArbolBinarioBusqueda(criterio="nombre")
        
        # Datos iniciales
        self._cargar_datos_iniciales()
    
    def _cargar_datos_iniciales(self):
        """Carga productos de ejemplo"""
        productos_iniciales = [
            Producto(101, "Laptop", 10, 899.99),
            Producto(102, "Mouse", 50, 25.50),
            Producto(103, "Teclado", 30, 45.00),
            Producto(104, "Monitor", 15, 299.99),
            Producto(105, "Auriculares", 40, 89.99),
            Producto(106, "Camiseta", 100, 15.00),
            Producto(107, "Pantalón", 60, 39.99),
            Producto(108, "Libro Python", 25, 55.00),
            Producto(109, "Lámpara", 20, 35.00),
            Producto(110, "Silla", 12, 120.00),
        ]
        
        # Cargar en arreglo
        self.inventario_arr.cargar_inicial(productos_iniciales.copy())
        
        # Cargar en lista enlazada
        for p in productos_iniciales:
            self.lista_enlazada.agregar(copy.deepcopy(p))
        
        # Cargar en árboles
        for p in productos_iniciales:
            self.abb_codigo.insertar(copy.deepcopy(p))
            self.abb_nombre.insertar(copy.deepcopy(p))
        
        # Registrar operación inicial en historial
        self.historial.push({"tipo": "INICIALIZACIÓN", "detalle": "Carga de 10 productos iniciales"})
    
    def agregar_producto(self, codigo, nombre, cantidad, precio):
        """Agrega un nuevo producto a todas las estructuras"""
        nuevo = Producto(codigo, nombre, cantidad, precio)
        
        # Agregar a arreglo
        self.inventario_arr.productos.append(nuevo)
        
        # Agregar a lista enlazada
        self.lista_enlazada.agregar(copy.deepcopy(nuevo))
        
        # Agregar a árboles
        self.abb_codigo.insertar(copy.deepcopy(nuevo))
        self.abb_nombre.insertar(copy.deepcopy(nuevo))
        
        # Registrar en historial
        self.historial.push({"tipo": "AGREGAR", "detalle": f"Producto: {nombre} (Código: {codigo})"})
        print(f"Producto {nombre} agregado exitosamente\n")
    
    def eliminar_producto(self, codigo):
        """Elimina un producto de todas las estructuras"""
        # Eliminar de lista enlazada
        self.lista_enlazada.eliminar(codigo)
        
        # Eliminar de arreglo
        producto_eliminado = None
        for i, p in enumerate(self.inventario_arr.productos):
            if p.codigo == codigo:
                producto_eliminado = self.inventario_arr.productos.pop(i)
                break
        
        # Registrar en historial
        if producto_eliminado:
            self.historial.push({"tipo": "ELIMINAR", "detalle": f"Producto: {producto_eliminado.nombre} (Código: {codigo})"})
            print(f"Producto eliminado del inventario\n")
        else:
            print(f"No se encontró producto con código {codigo}\n")
    
    def buscar_producto(self, codigo):
        """Busca un producto usando diferentes estructuras"""
        print(f"\nBÚSQUEDA DEL PRODUCTO CON CÓDIGO {codigo}")
        print("-" * 50)
        
        # Búsqueda en lista enlazada
        print("\n1. Búsqueda en LISTA ENLAZADA (búsqueda lineal):")
        self.lista_enlazada.buscar_por_codigo(codigo)
        
        # Búsqueda en Árbol Binario de Búsqueda (por código)
        print("\n2. Búsqueda en ÁRBOL BINARIO (por código):")
        self.abb_codigo.buscar(codigo)
        
        print()
    
    def deshacer_ultima_operacion(self):
        """Deshace la última operación (simulación)"""
        operacion = self.historial.deshacer()
        if operacion:
            print(f"   Se deshizo: {operacion['tipo']} - {operacion['detalle']}")
            print("   (Nota: En un sistema real, aquí se restauraría el estado anterior)\n")
    
    def simular_pedidos(self):
        """Simula una fila de pedidos de clientes"""
        print("\n" + "=" * 60)
        print("SIMULACIÓN DE PEDIDOS (COLA FIFO)")
        print("=" * 60)
        
        # Agregar pedidos de ejemplo
        pedidos_ejemplo = [
            Pedido(1, [(101, 1), (102, 2)]),
            Pedido(2, [(103, 1)]),
            Pedido(3, [(105, 3), (108, 1), (101, 1)]),
            Pedido(4, [(106, 5)]),
            Pedido(5, [(104, 1), (107, 2)]),
        ]
        
        print("\nAgregando pedidos a la cola...")
        for pedido in pedidos_ejemplo:
            self.cola_pedidos.agregar_pedido(pedido)
        
        self.cola_pedidos.mostrar()
        
        print("\nAtendiendo pedidos en orden de llegada...")
        while True:
            input("Presiona Enter para atender al siguiente cliente (o 's' para salir)...")
            pedido = self.cola_pedidos.atender_siguiente()
            if not pedido:
                break
        
        print("\nTodos los pedidos han sido atendidos\n")
    
    def mostrar_todo(self):
        """Muestra el estado de todas las estructuras"""
        print("\n" + "=" * 70)
        print("ESTADO COMPLETO DEL SISTEMA DE INVENTARIO")
        print("=" * 70)
        
        self.inventario_arr.mostrar()
        self.lista_enlazada.mostrar()
        self.historial.mostrar()
        self.cola_pedidos.mostrar()
        self.abb_codigo.mostrar()
        self.abb_nombre.mostrar()
    
    def menu_principal(self):
        """Menú interactivo principal"""
        while True:
            print("\n" + "=" * 60)
            print("SISTEMA DE ADMINISTRACIÓN DE INVENTARIO")
            print("=" * 60)
            print("1. Mostrar todo el inventario")
            print("2. Agregar producto")
            print("3. Eliminar producto")
            print("4. Buscar producto por código")
            print("5. Ordenar inventario (Arreglo)")
            print("6. Deshacer última operación")
            print("7. Simular cola de pedidos (Clientes)")
            print("8. Mostrar árboles (ABB)")
            print("9. Mostrar estado completo")
            print("0. Salir")
            print("-" * 60)
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.inventario_arr.mostrar()
            
            elif opcion == "2":
                print("\n--- AGREGAR PRODUCTO ---")
                try:
                    codigo = int(input("Código: "))
                    nombre = input("Nombre: ")
                    cantidad = int(input("Cantidad: "))
                    precio = float(input("Precio: "))
                    self.agregar_producto(codigo, nombre, cantidad, precio)
                except ValueError:
                    print("✗ Error: Ingrese valores válidos")
            
            elif opcion == "3":
                try:
                    codigo = int(input("Código del producto a eliminar: "))
                    self.eliminar_producto(codigo)
                except ValueError:
                    print("✗ Error: Código inválido")
            
            elif opcion == "4":
                try:
                    codigo = int(input("Código del producto a buscar: "))
                    self.buscar_producto(codigo)
                except ValueError:
                    print("✗ Error: Código inválido")
            
            elif opcion == "5":
                print("\n--- ORDENAR INVENTARIO ---")
                print("1. Ordenar alfabéticamente")
                print("2. Ordenar por precio")
                subop = input("Opción: ")
                if subop == "1":
                    self.inventario_arr.ordenar_alfabeticamente()
                elif subop == "2":
                    self.inventario_arr.ordenar_por_precio()
                else:
                    print("Opción inválida")
                self.inventario_arr.mostrar()
            
            elif opcion == "6":
                self.deshacer_ultima_operacion()
            
            elif opcion == "7":
                self.simular_pedidos()
            
            elif opcion == "8":
                self.abb_codigo.mostrar()
                self.abb_nombre.mostrar()
            
            elif opcion == "9":
                self.mostrar_todo()
            
            elif opcion == "0":
                print("\n¡Gracias por usar el sistema de inventario!")
                break
            
            else:
                print("✗ Opción inválida")

# ==================== EJECUCIÓN PRINCIPAL ====================
if __name__ == "__main__":
    app = AplicacionInventario()
    app.menu_principal()