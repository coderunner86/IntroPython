edad = int(input('Ingrese la edad en años -> '))
estatura = float(input('Ingrese la estatura  en metros -> '))
peso = int(input('Ingrese el peso en kilogramos -> '))
ind_masa_corporal = round(peso / estatura**2, 1)
print('Su índice de masa corporal es: ', ind_masa_corporal)
if edad < 45:
    if ind_masa_corporal < 22.0:
        print('condicion de rieqsgo: Bajo')
    else: ind_masa_corporal >= 22.0
    print('condicion de riesgo: medio')
else:
    if ind_masa_corporal < 22.0:
        print('condicion de riesgo: medio')
    else:  ind_masa_corporal >= 22.0
    print('condicion de riesgo: alto')