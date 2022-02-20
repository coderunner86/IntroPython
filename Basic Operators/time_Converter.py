secs = int(input('Ingrese un número en segundos: '))
days = secs*(1/60)*(1/60)*(1/24)
hour = 24*(days%1) 
min = 60*(hour%1)
sec = 60*(min%1)
sec = round(sec)

int_days = int(days)
int_hour = int(hour)
int_min = int(min)
int_sec = int(sec)
str_sec = str(sec)
str_min = str(int_min)
str_hour = str(int_hour)
str_days = str(int_days)

if int_min <10 and int_hour < 10:
  output = "{fdays}:{fhour}:{fmin}:{fsec}\n".format(fdays = str_days, fhour = "0" + str_hour, fmin = "0" + str_min, fsec = str_sec)
  print(output)
    
elif int_hour < 10:
  output = "{fdays}:{fhour}:{fmin}:{fsec}\n".format(fdays = str_days, fhour = "0" + str_hour, fmin = str_min, fsec = str_sec)
  print(output)

elif int_min < 10 : 
  output = "{fdays}:{fhour}:{fmin}:{fsec}\n".format(fdays = str_days, fhour = str_hour, fmin = "0" + str_min, fsec = str_sec)
  print(output)

else:
  output = "{fdays}:{fhour}:{fmin}:{fsec}\n".format(fdays = str_days, fhour = str_hour, fmin = str_min, fsec = str_sec)
  print(output)

  
