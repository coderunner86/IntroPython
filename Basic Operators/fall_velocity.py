vel_inicial = 0
a = 9.8
d = float(input('ingrese el valor de la distancia en metros desde la que suelta el objeto: -> '))
vel_final = (vel_inicial ** 2 + 2 * a * d) ** 0.5
vel_final = round(vel_final,2)
print('velocidad del objeto (m/s): -> ', vel_final)