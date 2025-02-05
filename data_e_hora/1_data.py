from datetime import date, datetime, time

d = date(2025, 1, 16)  # retorna a data informada
print(d)

print(date.today())  # retorna a data de hoje

data_hora = datetime(2025, 1, 16, 20, 17, 35)  # retorna data e hora informado
print(data_hora)
print(datetime.today())  # retorna data e hora de hoje

hora = time(20, 20, 0)
