a = round( float(input('Ingrese un numero real\n')), 3)
b = round(float(input('Ingrese otro numero real\n')), 3)
print('ingrese qué operación desea realizar:\n')
print('ingresando alguno de estos símbolos: +,-,*,/')
op=input('ingrese el símbolo:\t')
if op == '+' :
  res = a + b
  print ('ans:\n', res)
elif op == '-' :
  res = a - b
  print ('ans:\n', res)
elif op == '*' :
  res = a * b
  print ('ans:\n', res)
elif op == '/' :
  res = a / b
  print ('ans:\n', res)
else:
  print('symbol error')

