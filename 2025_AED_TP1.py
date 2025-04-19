# Ingreso de datos

destinatario = str(input("Ingrese el nombre del destinatario de la orden de pago: "))
codigo = str(input("Ingrese el codigo de identificación de la orden de pago: "))
monto = int(input("Ingrese la cantidad en efectivo que se ha solicitado pagar: "))

# Búsqueda de código de identificación 
if "ARS" in codigo:
    moneda_codigo = "ARS", 5
elif "USD" in codigo:
    moneda_codigo = "USD", 7
elif "EUR" in codigo:
    moneda_codigo = "EUR", 7
elif "GBP" in codigo:
    moneda_codigo = "GBP", 9
elif "JPY" in codigo:
    moneda_codigo = "JPY", 9
else:
    moneda_codigo = "Moneda no autorizada", 0

# Si no existe la moneda, no se hace el código.

if moneda_codigo[1] != 0 and monto != 0:
    monto_base = (monto-((monto*moneda_codigo[1])/100))
    monto_base = round (monto_base, 2)
else:
    monto_base = 0

# monto_base mayor a 500.000 SE HACE EL REDONDEO

if monto_base > 500000:
    monto_final = monto_base - ((monto_base*21)/100)
    monto_final = round (monto_final, 2)
else:
    monto_final = monto_base

# Un poco hicimos cosas redundantes pero el programa quiere que los valores que den 0.0 sean 0, un int no float, asi que lo cambié.
# Resultados:

print("Beneficiario: ", destinatario)
print("Moneda: ", moneda_codigo[0])
print("Monto base (descontadas las comisiones):", monto_base)
print("Monto final (descontados los impuestos):", monto_final)