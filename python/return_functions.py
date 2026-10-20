def calc_price(price, vat=21):
    return price * (vat / 100 + 1)


price = float(input("Introduce el precio: "))
vat = input("Introduce el IVA (pulsa Enter para usar el 21%): ").lower()
if vat == "":
    vat = 21

elif vat == "no":
    vat = 0

else:
    vat = float(vat)


total = calc_price(price, vat)
print(f"¡El precio del artículo {total:.2f}€ se ha guardado correctamente en la base de datos!")
