def calcular_iva_porcentaje(cantidad_sin_iva, porcentaje_iva):
    """CALCULA EL TOTAL (CANTIDAD + IVA) DE UNA CANTIDAD DADA Y UN PORCENTAJE DE IVA DADO"""
    iva = (cantidad_sin_iva * porcentaje_iva) / 100
    iva = round(iva, 2)
    total = round(cantidad_sin_iva + iva, 2)
    return "Monto inicial: " + str(cantidad_sin_iva) + ", IVA (" + str(porcentaje_iva) + "%): " + str(iva) + ", Total + IVA: " + str(total)

def calcular_iva_sin_porcentaje(cantidad_sin_iva):
    """CALCULA EL TOTAL (CANTIDAD + IVA) DE UNA CANTIDAD DADA ASUMIENDO UN PORCENTAJE DEL 21%"""
    porcentaje_iva = 21
    iva = (cantidad_sin_iva * porcentaje_iva) / 100
    iva = round(iva, 2)
    total = round(cantidad_sin_iva + iva, 2)
    return "Monto inicial: " + str(cantidad_sin_iva) + ", IVA (" + str(porcentaje_iva) + "%): " + str(iva) + ", Total + IVA: " + str(total)

print(calcular_iva_porcentaje(44.99, 13))
print(calcular_iva_sin_porcentaje(89.99))
