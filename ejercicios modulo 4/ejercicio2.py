from datetime import datetime
date = datetime(2020, 11, 4, 14, 53)
print(date.strftime("%Y/%m/%d %H:%M:%S "))
print(date.strftime("%Y/%B/%d %H:%M:%S %p "))
print(date.strftime("%a, %Y/%b %d "))
print(date.strftime("%A, %Y %B %d "))
print(date.strftime("%A: %d "))
print(date.strftime("Dia del año : %j "))
print(date.strftime("Numero de semana del año : %j "))
