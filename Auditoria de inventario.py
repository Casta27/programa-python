# 1. Matriz: [Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]
inventario = [
    [101, "Laptops", 15, 20],
    [102, "Monitores", 30, 25],
    [103, "Teclados", 8, 15],
    [104, "Ratones", 50, 50],
    [105, "Cables HDMI", 12, 40]
]

# 2. Módulo: Función para determinar la cantidad exacta a pedir
def calcular_reposicion(stock_actual, stock_minimo):
    """
    Evalúa el stock y retorna la cantidad a comprar basándose en la lógica de negocio.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# 3. y 4. Lógica de Negocio y Salida: Procesamiento e impresión de pedidos
def generar_reporte_pedidos(matriz_inventario):
    print("=== REPORTE DE REABASTECIMIENTO ===")
    
    for articulo in matriz_inventario:
        # Desempaquetar los datos de la fila actual
        codigo, nombre, stock_actual, stock_minimo = articulo
        
        # Llamar al módulo para obtener la cantidad a pedir
        cantidad_a_pedir = calcular_reposicion(stock_actual, stock_minimo)
        
        # Imprimir el resultado para cada artículo
        print(f"Artículo: {nombre:<15} | Cantidad a solicitar: {cantidad_a_pedir}")

# Ejecutar el programa
generar_reporte_pedidos(inventario)