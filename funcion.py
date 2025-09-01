def calcuIva(productos):
    ivas = ()
    subtotales = ()
    totales = ()
    for nombre, cantidad, precio in productos:
        subtotal = cantidad * precio
        iva = precio * 0.19
        total = subtotal + (iva * cantidad)
        subtotales += (subtotal,)
        ivas += (iva,)
        totales += (total,)
    return subtotales, ivas, totales