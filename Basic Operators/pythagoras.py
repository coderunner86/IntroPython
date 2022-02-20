a = round(float(input('Ingrese el cateto a:\t')),2)
b = round(float(input('Ingrese el cateto b:\t')),2)

square_a = a ** 2
square_b = b ** 2
hyp_c = round((square_a + square_b) ** 0.5, 2)

print('La hipotenusa de un triangulo recto con los catetos dados es:\t', hyp_c)