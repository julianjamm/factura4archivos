from datetime import datetime
from tuplas import productos
from diccionario import datos
from funcion import calcuIva

print("="*70)
print(f"              {datos['empresa']}        FACTURA DE COMPRA")
print("="*70)
fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f"Cliente: {datos['cliente']}")
print(f"Fecha:   {fecha}")
print(f"NIT: {datos['nit']}")
print("="*70)

subtotales, ivas, totales = calcuIva(productos)

print("{:<20} {:<10} {:<15} {:<15} {:<15}".format("Producto", "Cantidad", "Precio", "IVA", "Total"))
print("-"*70)

total_general = 0
for i, (nombre, cantidad, precio) in enumerate(productos):
    print("{:<20} {:<10} {:<15} {:<15} {:<15}".format(
        nombre[:20], 
        cantidad,
        f"{precio:,}".replace(",", "."),
        f"{ivas[i]:,.0f}".replace(",", "."),
        f"{totales[i]:,.0f}".replace(",", ".")
    ))
    total_general += totales[i]

print("-"*70)
print(f"{'TOTAL A PAGAR':<60} COP {total_general:,.0f}".replace(",", "."))
print("="*70)
print("¡Gracias por su compra!")